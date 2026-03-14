from agents.base import BaseAgent


class AssetsAgent(BaseAgent):
    def __init__(self):
        super().__init__("assets.md", "Asset & Execution Agent")


if __name__ == "__main__":
    AssetsAgent.cli_entry()
