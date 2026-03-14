import sys
import anthropic
from config import ANTHROPIC_API_KEY, MODEL, MAX_TOKENS, PROMPTS_DIR

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


class BaseAgent:
    def __init__(self, prompt_file: str, agent_name: str):
        self.agent_name = agent_name
        system_path = PROMPTS_DIR / "system.md"
        agent_path = PROMPTS_DIR / prompt_file
        system_context = system_path.read_text(encoding="utf-8") if system_path.exists() else ""
        agent_prompt = agent_path.read_text(encoding="utf-8")
        self.system_prompt = (system_context + "\n\n" + agent_prompt).strip()

    def run(self, user_input: str) -> str:
        message = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_input}],
        )
        return message.content[0].text

    @classmethod
    def cli_entry(cls):
        """Allows running an agent directly: python -m agents.diagnostic 'input here'"""
        if len(sys.argv) < 2:
            print(f"Usage: python -m {cls.__module__} 'your input here'")
            sys.exit(1)
        agent = cls()
        user_input = " ".join(sys.argv[1:])
        print(f"\n--- {agent.agent_name} ---\n")
        print(agent.run(user_input))
