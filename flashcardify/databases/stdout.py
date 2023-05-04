from flashcardify.databases.base import BaseDatabase
from flashcardify.cards.base import Card
from logging import getLogger


class StdoutDatabase(BaseDatabase):
    def __init__(self, path: str = None, card_separator: str = "\n"):
        self.flashcards_path = path
        self.logger = getLogger(__name__)
        self.card_separator = card_separator

    def store(self, card: Card) -> None:
        self.logger.info("Storing flashcard")
        print(card)
