"""AI Agent service for conducting research interviews."""

from app.constants import (
    AI_FREQUENCY_PENALTY,
    AI_INITIAL_MAX_TOKENS,
    AI_MAX_TOKENS,
    AI_PRESENCE_PENALTY,
    AI_TEMPERATURE,
    DEFAULT_AI_MODEL,
)
from app.services.openai_factory import create_openai_client


class AIInterviewAgent:
    """AI agent that conducts research interviews based on study context."""

    def __init__(self, api_key: str | None = None):
        """
        Initialize the AI agent.

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var or settings)
        """
        self.client = create_openai_client(api_key)
        self.model = DEFAULT_AI_MODEL

    def generate_system_prompt(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        turns_remaining: int,
    ) -> str:
        """
        Generate the system prompt for the AI agent.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions to explore
            turns_remaining: Number of turns remaining in the interview

        Returns:
            System prompt string
        """
        questions_text = "\n".join([f"- {q}" for q in study_questions])

        return f"""You are an AI research interviewer conducting a study titled: "{study_title}"

Study context: {study_description}

Research questions to explore:
{questions_text}

Your role:
- Ask thoughtful, open-ended questions related to the research topics
- Follow up on interesting responses with deeper questions
- Be conversational, empathetic, and professional
- Stay focused on the research questions
- Probe deeper when responses are vague or brief
- Guide the conversation naturally between topics
- You have {turns_remaining} questions remaining in this interview

Conversation guidelines:
- Ask ONE question at a time
- Keep questions concise (2-3 sentences maximum)
- Acknowledge the previous response before asking the next question
- Transition smoothly between topics
- If this is the last turn, thank them and provide a graceful closing
- Be encouraging and appreciative of their time

Remember: Your goal is to gather authentic, detailed insights related to the research questions."""

    def get_ai_response(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        conversation_history: list[dict],
        current_turn: int,
        max_turns: int,
    ) -> str:
        """
        Get AI response based on conversation context.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions
            conversation_history: List of previous messages with
                format [{"role": "user"|"assistant", "content": "..."}]
            current_turn: Current turn number (0-indexed)
            max_turns: Maximum number of agent turns allowed

        Returns:
            AI-generated response string
        """
        turns_remaining = max_turns - current_turn

        system_prompt = self.generate_system_prompt(
            study_title=study_title,
            study_description=study_description,
            study_questions=study_questions,
            turns_remaining=turns_remaining,
        )

        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(conversation_history[-10:])

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=AI_TEMPERATURE,
                max_tokens=AI_MAX_TOKENS,
                presence_penalty=AI_PRESENCE_PENALTY,
                frequency_penalty=AI_FREQUENCY_PENALTY,
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return self._get_error_fallback(str(e))

    def get_initial_message(
        self,
        study_title: str,
        study_description: str,
        study_questions: list[str],
        interviewee_name: str,
    ) -> str:
        """
        Generate the first message to start the interview.

        Args:
            study_title: Title of the research study
            study_description: Description of the study
            study_questions: List of research questions
            interviewee_name: Name of the interviewee

        Returns:
            Opening message string
        """
        system_prompt = (
            f'You are an AI research interviewer starting an interview '
            f'for a study titled: "{study_title}"\n\n'
            f'Study context: {study_description}\n\n'
            f"The participant's name is {interviewee_name}.\n\n"
            "Generate a warm, welcoming opening message that:\n"
            "1. Thanks them for participating\n"
            "2. Briefly mentions what the study is about\n"
            "3. Asks your first research question\n"
            "4. Keep it concise (3-4 sentences total)\n\n"
            "Be friendly and professional."
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "system", "content": system_prompt}],
                temperature=AI_TEMPERATURE,
                max_tokens=AI_INITIAL_MAX_TOKENS,
            )

            return response.choices[0].message.content.strip()

        except Exception:
            return (
                f"Hello {interviewee_name}! Thank you for participating in "
                f"this research study about {study_title}. I'm excited to "
                f"hear your thoughts. To begin, could you share your "
                f"initial perspective on this topic?"
            )

    def _get_error_fallback(self, error_message: str) -> str:
        """Provide a graceful fallback response when API fails."""
        print(f"AI Agent Error: {error_message}")
        return "Thank you for your response. Could you tell me more about that?"
