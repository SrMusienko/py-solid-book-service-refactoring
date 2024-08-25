from app.book import Book
from app.display import ConsoleDisplayStrategy, ReverseDisplayStrategy
from app.print import ConsolePrintStrategy, ReversePrintStrategy
from app.serializer import JsonSerializeStrategy, XmlSerializeStrategy


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            match method_type:
                case"console":
                    book.display_strategy = ConsoleDisplayStrategy()
                case "reverse":
                    book.display_strategy = ReverseDisplayStrategy()
            book.display()

        elif cmd == "print":
            match method_type:
                case "console":
                    book.print_strategy = ConsolePrintStrategy()
                case "reverse":
                    book.print_strategy = ReversePrintStrategy()
            book.print()

        elif cmd == "serialize":
            match method_type:
                case "json":
                    book.serialize_strategy = JsonSerializeStrategy()
                case "xml":
                    book.serialize_strategy = XmlSerializeStrategy()
            return book.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
