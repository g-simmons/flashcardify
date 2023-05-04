from dataclasses import dataclass
from flashcardify.databases import Database
from flashcardify.cards import Card
from flashcardify.models import Model
from dataclasses import dataclass
from typing import List
import yaml


@dataclass
class Config:
    models: List[Model]
    databases: List[Database]
    styles: List[str]
    syntaxes: List[str]

    @classmethod
    def from_file(cls, path: str):
        """
        Read yaml sections from config file
        """

        with open(path, "r") as f:
            config = yaml.safe_load(f)

        return cls(
            models=config["models"],
            databases=config["databases"],
            styles=config["styles"],
            syntaxes=config["syntaxes"],
        )

    def write(self, path: str):
        """
        Write yaml sections to config file
        """
        with open(path, "w") as f:
            yaml.dump(self.__dict__, f)


def configure_flashcardify():
    pass


# write a config file to ~/.flashcardify/config.yaml
# config has sections:
# databases
# one database can have is_default: true
# models
# one model can have is_default: true
# styles
# one style can have is_default: true
# syntaxes
# one syntax can have is_default
