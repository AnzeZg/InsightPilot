"""Generate insights from completed interviews using LLM analysis."""

import json
import logging
from typing import Any

from sqlalchemy.orm import Session

from app.constants import DEFAULT_AI_MODEL, INSIGHT_GENERATION_TEMPERATURE
from app.crud import interview as interview_crud
from app.models.interview import Message
from app.services.openai_factory import create_openai_client

logger = logging.getLogger(__name__)


class InsightGenerator:
    """Generate insights from completed interviews using LLM."""

    def __init__(self):
        """Initialize the insight generator with OpenAI client."""
        self.client = create_openai_client()

    def generate_insights(self, db: Session, interview_id: int) -> dict[str, Any]:
        """
        Analyze interview using LLM and extract structured insights.

        Args:
            db: Database session
            interview_id: ID of the interview to analyze

        Returns:
            Dictionary containing:
                - summary: Brief summary of key points
                - sentiment: Overall sentiment (positive/neutral/negative)
                - keywords: List of important keywords/phrases
                - themes: List of main themes discussed
                - notable_quotes: List of meaningful user quotes
                - engagement_level: Assessment of participant engagement
                - key_insights: List of notable insights for researchers

        Raises:
            ValueError: If OpenAI API key is not configured
            Exception: If LLM analysis fails completely
        """
        messages = interview_crud.get_messages_by_interview(db, interview_id)

        if not messages:
            logger.warning(f"No messages found for interview {interview_id}")
            return self._empty_insights()

        conversation = self._format_conversation(messages)

        prompt = f"""Analyze this research interview and provide structured insights.

INTERVIEW TRANSCRIPT:
{conversation}

Provide your analysis in the following JSON format:
{{
  "summary": "2-3 sentence summary of the key points discussed",
  "sentiment": "positive/neutral/negative",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "themes": ["main theme 1", "main theme 2"],
  "notable_quotes": ["quote 1", "quote 2", "quote 3"],
  "engagement_level": "high/medium/low",
  "key_insights": ["insight 1", "insight 2"]
}}

Guidelines:
- Summary should capture the main discussion points concisely
- Sentiment reflects the overall tone of participant responses
- Keywords should be single words or short phrases (2-3 words max)
- Themes are broader topics or patterns in the conversation
- Notable quotes should be the most insightful or detailed participant responses
- Engagement level based on response depth and thoughtfulness
- Key insights are important takeaways for researchers

Focus on the participant's responses, not the interviewer's questions.
"""

        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_AI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert qualitative research analyst extracting insights from research interviews. Provide accurate, objective analysis in valid JSON format.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=INSIGHT_GENERATION_TEMPERATURE,
                response_format={"type": "json_object"},
            )

            insights = json.loads(response.choices[0].message.content)
            logger.info(f"Generated insights for interview {interview_id}")

            return self._validate_insights(insights)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse LLM response as JSON: {e}")
            return self._fallback_extraction(messages)

        except Exception as e:
            logger.error(f"LLM insight generation failed: {e}")
            return self._fallback_extraction(messages)

    def _format_conversation(self, messages: list[Message]) -> str:
        """
        Format messages into a readable transcript.

        Args:
            messages: List of Message objects

        Returns:
            Formatted conversation string
        """
        lines = []
        for msg in messages:
            speaker = "AI Interviewer" if msg.role == "assistant" else "Participant"
            lines.append(f"{speaker}: {msg.content}")
        return "\n\n".join(lines)

    def _validate_insights(self, insights: dict[str, Any]) -> dict[str, Any]:
        """
        Validate and normalize LLM output.

        Args:
            insights: Raw insights from LLM

        Returns:
            Validated and normalized insights
        """
        validated = {
            "summary": str(insights.get("summary", "No summary available"))[:1000],
            "sentiment": insights.get("sentiment", "neutral").lower(),
            "keywords": insights.get("keywords", [])[:20],
            "themes": insights.get("themes", [])[:10],
            "notable_quotes": insights.get("notable_quotes", [])[:5],
            "engagement_level": insights.get("engagement_level", "medium").lower(),
            "key_insights": insights.get("key_insights", [])[:10],
        }

        if validated["sentiment"] not in ["positive", "neutral", "negative"]:
            validated["sentiment"] = "neutral"

        if validated["engagement_level"] not in ["high", "medium", "low"]:
            validated["engagement_level"] = "medium"

        return validated

    def _fallback_extraction(self, messages: list[Message]) -> dict[str, Any]:
        """
        Basic extraction if LLM fails.

        Args:
            messages: List of Message objects

        Returns:
            Basic insights extracted without LLM
        """
        logger.warning("Using fallback insight extraction")

        user_messages = [msg for msg in messages if msg.role == "user"]

        if not user_messages:
            return self._empty_insights()

        user_texts = [msg.content for msg in user_messages]
        meaningful_responses = [text for text in user_texts if len(text) > 50]

        summary = " ".join(user_texts[:3])[:500] if user_texts else "No responses recorded"

        quotes = sorted(meaningful_responses, key=len, reverse=True)[:3]

        return {
            "summary": summary,
            "sentiment": "neutral",
            "keywords": [],
            "themes": [],
            "notable_quotes": quotes,
            "engagement_level": "medium",
            "key_insights": ["Interview completed but detailed analysis unavailable"],
        }

    def _empty_insights(self) -> dict[str, Any]:
        """
        Return empty insights structure for interviews with no messages.

        Returns:
            Empty insights dictionary
        """
        return {
            "summary": "No conversation recorded",
            "sentiment": "neutral",
            "keywords": [],
            "themes": [],
            "notable_quotes": [],
            "engagement_level": "low",
            "key_insights": [],
        }
