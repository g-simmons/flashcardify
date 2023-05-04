from dataclasses import dataclass
from typing import Optional
import json
import yaml


@dataclass
class Card:
    front: str
    back: Optional[str] = None

    def __str__(self):
        return yaml.dump(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def write(self):
        pass

    def read(self, card: str):
        pass
