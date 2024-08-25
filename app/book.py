from app.display import DisplayStrategy
from app.print import PrintStrategy
from app.serializer import SerializeStrategy


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self._display_strategy = None
        self._print_strategy = None
        self._serialize_strategy = None

    @property
    def display_strategy(self) -> DisplayStrategy:
        return self._display_strategy

    @display_strategy.setter
    def display_strategy(self, strategy: DisplayStrategy) -> None:
        self._display_strategy = strategy

    def display(self) -> None:
        if self._display_strategy:
            self._display_strategy.display(self.content)
        else:
            raise ValueError("No display strategy set")

    @property
    def print_strategy(self) -> PrintStrategy:
        return self._print_strategy

    @print_strategy.setter
    def print_strategy(self, strategy: PrintStrategy) -> None:
        self._print_strategy = strategy

    def print(self) -> None:
        if self._print_strategy:
            self._print_strategy.print(self.content, self.title)
        else:
            raise ValueError("No print strategy set")

    @property
    def serialize_strategy(self) -> SerializeStrategy:
        return self._serialize_strategy

    @serialize_strategy.setter
    def serialize_strategy(self, strategy: SerializeStrategy) -> None:
        self._serialize_strategy = strategy

    def serialize(self) -> str:
        if self._serialize_strategy:
            return self._serialize_strategy.serialize(self.content, self.title)
        else:
            raise ValueError("No serialize strategy set")
