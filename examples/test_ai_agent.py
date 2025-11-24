#!/usr/bin/env python3
"""
Terminal-based test for the AI Interview Agent. (Created using AI for quick testing)

Usage:
    # Requires OPENAI_API_KEY environment variable
    python examples/test_ai_agent.py
    
    # Custom number of turns
    python examples/test_ai_agent.py --turns 10
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path so we can import from app
sys.path.insert(0, str(Path(__file__).parent.parent))

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

from app.services.ai_agent import AIInterviewAgent


def simulate_interview(max_turns: int = 5):
    """Simulate an interactive interview in the terminal."""

    # Sample study data
    study_title = "User Experience with Mobile Banking Apps"
    study_description = "Understanding how people interact with mobile banking applications and what features they value most."
    study_questions = [
        "What are the most important features in a mobile banking app?",
        "What frustrations do users experience with current banking apps?",
        "How do security concerns affect mobile banking usage?",
        "What improvements would users like to see?",
    ]
    interviewee_name = "Test User"

    # Initialize agent
    print("=" * 60)
    print("AI Interview Agent - Terminal Test")
    print("=" * 60)
    print(f"\nStudy: {study_title}")
    print(f"Max Turns: {max_turns}")
    print("\n" + "=" * 60)

    try:
        agent = AIInterviewAgent()
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nTip: Set OPENAI_API_KEY in your .env file or environment")
        return

    # Start interview with initial message
    print("\n🤖 AI Agent: Getting initial message...\n")

    initial_message = agent.get_initial_message(
        study_title=study_title,
        study_description=study_description,
        study_questions=study_questions,
        interviewee_name=interviewee_name,
    )

    print(f"🤖 AI: {initial_message}\n")

    # Conversation history
    conversation_history = []

    # Interactive conversation loop
    for turn in range(max_turns):
        print(f"--- Turn {turn + 1}/{max_turns} ---")

        # Get user input
        try:
            user_message = input("\n👤 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Interview interrupted. Goodbye!")
            return

        if not user_message:
            print("⚠️  Please enter a message.")
            continue

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Get AI response
        print("\n🤖 AI Agent: Thinking...\n")

        ai_response = agent.get_ai_response(
            study_title=study_title,
            study_description=study_description,
            study_questions=study_questions,
            conversation_history=conversation_history,
            current_turn=turn,
            max_turns=max_turns,
        )

        print(f"🤖 AI: {ai_response}\n")

        # Add AI response to history
        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })

    # Interview complete
    print("\n" + "=" * 60)
    print("✅ Interview Complete!")
    print("=" * 60)
    print(f"\nTotal messages: {len(conversation_history)}")
    print(f"User messages: {len([m for m in conversation_history if m['role'] == 'user'])}")
    print(f"AI messages: {len([m for m in conversation_history if m['role'] == 'assistant'])}")

    # Show conversation summary
    print("\n📝 Conversation Summary:")
    print("-" * 60)
    for i, msg in enumerate(conversation_history, 1):
        speaker = "👤 You" if msg['role'] == 'user' else "🤖 AI"
        content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
        print(f"{i}. {speaker}: {content}")


def test_system_prompt():
    """Test system prompt generation."""
    try:
        agent = AIInterviewAgent()
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        print("\nNote: API key not required for prompt generation test")
        print("Creating dummy agent for demonstration...\n")
        # For testing prompt generation, we can skip the actual API client
        import os
        os.environ.setdefault("OPENAI_API_KEY", "dummy-key-for-prompt-test")
        agent = AIInterviewAgent()

    prompt = agent.generate_system_prompt(
        study_title="Test Study",
        study_description="This is a test study description.",
        study_questions=["Question 1?", "Question 2?"],
        turns_remaining=5,
    )

    print("=" * 60)
    print("System Prompt Test")
    print("=" * 60)
    print(prompt)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Test the AI Interview Agent")
    parser.add_argument(
        "--turns",
        type=int,
        default=5,
        help="Maximum number of turns (default: 5)"
    )
    parser.add_argument(
        "--test-prompt",
        action="store_true",
        help="Just test system prompt generation and exit"
    )

    args = parser.parse_args()

    if args.test_prompt:
        test_system_prompt()
    else:
        simulate_interview(max_turns=args.turns)


if __name__ == "__main__":
    main()

