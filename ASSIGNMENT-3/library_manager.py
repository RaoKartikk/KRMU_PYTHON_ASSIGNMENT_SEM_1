"""Book Archive Controller - CSE Python Assignment"""

import json
import logging
from pathlib import Path

# Logger Setup
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("logs/archive.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("archive")

# Custom Exceptions
class BookMissing(Exception): pass
class AlreadyIssued(Exception): pass
class NotYetIssued(Exception): pass


class Book:
    """Represents a book with metadata & issue status"""

    def __init__(self, isbn, title, writer, year, state="available"):
        self._isbn = isbn
        self._title = title
        self._writer = writer
        self._year = year
        self._state = state

    def __str__(self):
        return f"{self._isbn} - {self._title} ({self._writer}, {self._year}) [{self._state}]"

    @property
    def isbn(self): return self._isbn

    @property
    def status(self): return self._state

    def to_dict(self):
        return {
            "isbn": self._isbn,
            "title": self._title,
            "writer": self._writer,
            "year": self._year,
            "state": self._state
        }

    def issue(self):
        if self._state == "issued":
            raise AlreadyIssued(f"{self._title} is already taken!")
        self._state = "issued"
        log.info(f"Issued -> {self._title}")

    def return_book(self):
        if self._state != "issued":
            raise NotYetIssued(f"{self._title} has not been issued yet!")
        self._state = "available"
        log.info(f"Returned -> {self._title}")


class LibraryInventory:
    """Inventory system storing books using ISBN keys"""

    def __init__(self, file="books.json"):
        self._file = Path(file)
        self._store = {}
        self._load()

    def add_book(self, book: Book):
        self._store[book.isbn] = book
        log.info(f"Added -> {book.isbn}")
        self._save()

    def search_by_isbn(self, isbn):
        return self._store.get(isbn)

    def search_by_title(self, title):
        title = title.lower()
        return [bk for bk in self._store.values() if title in bk._title.lower()]

    def display_all(self):
        return list(self._store.values())

    def issue_book(self, isbn):
        bk = self.search_by_isbn(isbn)
        if not bk:
            log.error(f"Not found: {isbn}")
            raise BookMissing("ISBN not present")

        bk.issue()
        self._save()

    def return_book(self, isbn):
        bk = self.search_by_isbn(isbn)
        if not bk:
            log.error(f"Not found: {isbn}")
            raise BookMissing("ISBN not present")

        bk.return_book()
        self._save()

    def _save(self):
        try:
            with self._file.open("w") as f:
                json.dump(
                    {i: b.to_dict() for i, b in self._store.items()},
                    f,
                    indent=2
                )
            log.info("Archive updated")
        except IOError as e:
            log.error(f"Unable to save: {e}")

    def _load(self):
        if not self._file.exists():
            log.info("No archive found. Creating new file.")
            return

        try:
            data = json.load(self._file.open())
            for isbn, info in data.items():
                self._store[isbn] = Book(
                    info["isbn"], info["title"], info["writer"],
                    info["year"], info.get("state", "available")
                )
            log.info(f"Loaded {len(self._store)} entries")
        except json.JSONDecodeError:
            log.error("Archive corrupted, starting fresh.")


# CLI SYSTEM
def menu():
    print("\n=== BOOK ARCHIVE MENU ===")
    print("1. Add Book\n2. Issue Book\n3. Return Book\n4. Show All\n5. Search\n6. Quit")


def main():
    lib = LibraryInventory()
    log.info("Program started")

    while True:
        try:
            menu()
            choice = input("Select option (1-6): ").strip()

            if not choice.isdigit():
                print("Enter numeric choice 1-6")
                continue

            choice = int(choice)

            if choice == 1:
                isbn = input("ISBN: ")
                name = input("Title: ")
                writer = input("Author: ")
                year = int(input("Published Year: "))
                lib.add_book(Book(isbn, name, writer, year))
                print("Book added successfully.")

            elif choice == 2:
                isbn = input("ISBN to issue: ")
                try:
                    lib.issue_book(isbn)
                    print("Book issued.")
                except (BookMissing, AlreadyIssued) as e:
                    print(e)

            elif choice == 3:
                isbn = input("ISBN to return: ")
                try:
                    lib.return_book(isbn)
                    print("Book returned.")
                except (BookMissing, NotYetIssued) as e:
                    print(e)

            elif choice == 4:
                all_books = lib.display_all()
                if not all_books:
                    print("No books stored.")
                else:
                    for idx, bk in enumerate(all_books, 1):
                        print(f"{idx}. {bk}")

            elif choice == 5:
                print("1. Search by ISBN\n2. Search by Title")
                s = input("Choice: ")
                if s == "1":
                    bk = lib.search_by_isbn(input("ISBN: "))
                    print(bk if bk else "No match")
                else:
                    res = lib.search_by_title(input("Title: "))
                    if res:
                        for b in res:
                            print(b)
                    else:
                        print("No results")

            elif choice == 6:
                print("Exiting...")
                log.info("Program terminated")
                break

            else:
                print("Invalid option")

        except KeyboardInterrupt:
            print("\nProgram closed.")
            break
        except Exception as err:
            print(f"Error: {err}")
            log.error(err)


if __name__ == "__main__":
    main()
