from flashcardify.databases.base import BaseDatabase
from flashcardify.cards.base import Card
from logging import getLogger


class TextfileDatabase(BaseDatabase):
    def __init__(self, path: str = None, card_separator: str = "\n"):
        self.flashcards_path = path
        self.logger = getLogger(__name__)
        self.card_separator = card_separator

    def store(self, flashcard: Card) -> None:
        with open(self.flashcards_path, "r") as f:
            for line in f:
                if line == f"{flashcard.front}\t{flashcard.back}":
                    self.logger.info("Flashcard already exists")
                    return

        with open(self.flashcards_path, "a") as f:
            self.logger.info("Storing flashcard")
            f.write(f"{self.card_separator}{flashcard.front}\t{flashcard.back}")
