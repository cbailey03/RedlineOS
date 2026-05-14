from abc import ABC, abstractmethod


class BaseAnnotation(ABC):
    """Base class for all annotation types."""

    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "BaseAnnotation": ...
