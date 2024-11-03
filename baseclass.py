from abc import ABC, abstractmethod
from pathlib import Path


class TextProcessor(ABC):
    @abstractmethod
    def load(self, path: Path) -> None:
        raise NotImplementedError

    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def save(self, path: Path) -> None:
        raise NotImplementedError