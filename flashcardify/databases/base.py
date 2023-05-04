from abc import ABC, abstractmethod
from flashcardify.cards.base import Card


class BaseDatabase(ABC):
    @abstractmethod
    def store(self, flashcard: Card) -> None:
        pass
