from agents.base import BaseAgent


class LearnAgent(BaseAgent):
    def __init__(self):
        super().__init__("learn.md", "Sprint Logger")


if __name__ == "__main__":
    LearnAgent.cli_entry()
