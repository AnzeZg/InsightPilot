"""Analytics service for study data aggregation."""

from collections import defaultdict

from sqlalchemy.orm import Session

from app.constants import SAMPLE_QUOTES_LIMIT, TOP_KEYWORDS_LIMIT
from app.crud import interview as interview_crud
from app.models.study import Study
from app.schemas.interview import (
    DemographicBreakdown,
    InterviewTimeline,
    KeywordFrequency,
    ResponseMetrics,
    SentimentDistribution,
    StudyAnalytics,
)


class StudyAnalyticsService:
    """Service for generating study analytics and aggregations."""

    def __init__(self, db: Session):
        self.db = db

    def generate_analytics(self, study_id: int, study: Study) -> StudyAnalytics:
        """
        Generate comprehensive analytics for a study.

        Args:
            study_id: ID of the study
            study: Study model instance

        Returns:
            StudyAnalytics with all aggregated metrics
        """
        interviews = interview_crud.get_interviews_by_study(
            self.db, study_id, load_relations=True
        )

        return StudyAnalytics(
            study_id=study.id,
            study_title=study.title,
            total_interviews=len(interviews),
            completed_interviews=sum(1 for i in interviews if i.completed_at),
            sentiment_distribution=self._calculate_sentiment(interviews),
            top_keywords=self._aggregate_keywords(interviews),
            response_metrics=self._calculate_metrics(interviews),
            demographics=self._process_demographics(interviews),
            timeline=self._build_timeline(interviews),
            sample_quotes=self._extract_quotes(interviews),
        )

    def _calculate_sentiment(self, interviews: list) -> SentimentDistribution:
        """Calculate sentiment distribution across all interviews."""
        counts = {"positive": 0, "neutral": 0, "negative": 0}

        for interview in interviews:
            if interview.insight and interview.insight.sentiment:
                sentiment = interview.insight.sentiment.lower()
                if sentiment in counts:
                    counts[sentiment] += 1

        return SentimentDistribution(
            positive=counts["positive"],
            neutral=counts["neutral"],
            negative=counts["negative"],
            total=sum(counts.values()),
        )

    def _aggregate_keywords(self, interviews: list) -> list[KeywordFrequency]:
        """Aggregate and rank keywords across all interviews."""
        keyword_freq = {}

        for interview in interviews:
            if interview.insight and interview.insight.keywords_json:
                for keyword in interview.insight.keywords_json:
                    keyword_lower = keyword.lower()
                    keyword_freq[keyword_lower] = keyword_freq.get(keyword_lower, 0) + 1

        return [
            KeywordFrequency(keyword=kw, count=count)
            for kw, count in sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[
                :TOP_KEYWORDS_LIMIT
            ]
        ]

    def _calculate_metrics(self, interviews: list) -> ResponseMetrics:
        """Calculate response metrics (length, message count, etc.)."""
        total_interviews = len(interviews)
        completed = sum(1 for i in interviews if i.completed_at)

        if total_interviews == 0:
            return ResponseMetrics(
                avg_message_count=0,
                avg_response_length=0,
                avg_conversation_length=0,
                total_messages=0,
            )

        total_messages = 0
        total_response_length = 0
        user_message_count = 0

        for interview in interviews:
            messages = interview_crud.get_messages_by_interview(self.db, interview.id)
            total_messages += len(messages)

            for msg in messages:
                if msg.role == "user":
                    total_response_length += len(msg.content)
                    user_message_count += 1

        avg_message_count = total_messages / total_interviews
        avg_response_length = (
            total_response_length / user_message_count if user_message_count > 0 else 0
        )
        avg_conversation_length = (
            total_response_length / completed if completed > 0 else 0
        )

        return ResponseMetrics(
            avg_message_count=round(avg_message_count, 2),
            avg_response_length=round(avg_response_length, 2),
            avg_conversation_length=round(avg_conversation_length, 2),
            total_messages=total_messages,
        )

    def _process_demographics(self, interviews: list) -> list[DemographicBreakdown]:
        """Process and aggregate demographic data."""
        demographics_data = {}

        for interview in interviews:
            if interview.interviewee and interview.interviewee.demographics_json:
                for field, value in interview.interviewee.demographics_json.items():
                    if value:
                        if field not in demographics_data:
                            demographics_data[field] = {}
                        key = str(value)
                        demographics_data[field][key] = (
                            demographics_data[field].get(key, 0) + 1
                        )

        return [
            DemographicBreakdown(field=field, values=values)
            for field, values in demographics_data.items()
        ]

    def _build_timeline(self, interviews: list) -> list[InterviewTimeline]:
        """Build interview timeline data."""
        timeline_data = defaultdict(lambda: {"completed": 0, "in_progress": 0})

        for interview in interviews:
            date_key = interview.started_at.strftime("%Y-%m-%d")
            if interview.completed_at:
                timeline_data[date_key]["completed"] += 1
            else:
                timeline_data[date_key]["in_progress"] += 1

        return [
            InterviewTimeline(
                date=date, completed=data["completed"], in_progress=data["in_progress"]
            )
            for date, data in sorted(timeline_data.items())
        ]

    def _extract_quotes(self, interviews: list) -> list[str]:
        """Extract sample notable quotes from interviews."""
        sample_quotes = []

        for interview in interviews:
            if interview.insight and interview.insight.quotes_json:
                sample_quotes.extend(interview.insight.quotes_json[:2])
            if len(sample_quotes) >= SAMPLE_QUOTES_LIMIT:
                break

        return sample_quotes[:SAMPLE_QUOTES_LIMIT]

