from abc import ABC, abstractmethod


class Case(ABC):
    @abstractmethod
    def from_string(self, value: str) -> str:
        """
            Returns a string value converted for case style desired.
        """
        pass

    @abstractmethod
    def from_dict(self, __dict: dict) -> dict:
        """
            Returns a dict with all keys values converted for case style desired.
        """
        pass
