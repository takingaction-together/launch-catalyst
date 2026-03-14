from agents.base import BaseAgent


class DiagnosticAgent(BaseAgent):
    def __init__(self):
        super().__init__("diagnostic.md", "Strategic Diagnostic Agent")


if __name__ == "__main__":
    DiagnosticAgent.cli_entry()
