from abc import ABC, abstractmethod


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, content: str, title: str) -> None:
        pass


class ConsolePrintStrategy(PrintStrategy):
    def print(self, content: str, title: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrintStrategy(PrintStrategy):
    def print(self, content: str, title: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
