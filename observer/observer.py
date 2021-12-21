from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from subject import Subject


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject, event: str) -> None:
        pass
