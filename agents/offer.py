from agents.base import BaseAgent


class OfferAgent(BaseAgent):
    def __init__(self):
        super().__init__("offer.md", "Offer & Positioning Agent")


if __name__ == "__main__":
    OfferAgent.cli_entry()
