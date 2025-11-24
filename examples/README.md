# Examples

Standalone scripts for testing components independently.

## AI Agent Test

Test the AI interview agent in your terminal before integrating with the web interface.

### Prerequisites

You need an OpenAI API key. Add it to your `.env` file:

```bash
OPENAI_API_KEY=sk-your-api-key-here
```

### Usage

**Basic test (5 turns):**
```bash
python examples/test_ai_agent.py
```

**Custom number of turns:**
```bash
python examples/test_ai_agent.py --turns 10
```

**Test system prompt generation:**
```bash
python examples/test_ai_agent.py --test-prompt
```

### Options

- `--turns N` - Set maximum number of conversation turns (default: 5)
- `--test-prompt` - Display the system prompt and exit

### Example Session

```
AI Interview Agent - Terminal Test
============================================================

Study: User Experience with Mobile Banking Apps
Max Turns: 5

============================================================

🤖 AI: Hello Test User! Thank you for participating...

--- Turn 1/5 ---

👤 You: I really like the fingerprint login feature
🤖 AI: Thank you for sharing that. Can you tell me more...
```
