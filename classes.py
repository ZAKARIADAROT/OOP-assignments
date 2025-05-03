# OOP Concepts: Encapsulation, Inheritance, Polymorphism

# Base class: Book (with Encapsulation)
class Book:
    def __init__(self, title, author, pages):
        self.__title = title       # Private attribute
        self.__author = author     # Private attribute
        self.pages = pages

    # Getter methods (Encapsulation)
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def read(self):
        print(f"Reading '{self.__title}' by {self.__author}...")

# Subclass: EBook inherits from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    # Polymorphism: Override read method
    def read(self):
        print(f"Opening eBook '{self.get_title()}' on your device... ({self.file_size}MB)")

# Subclass: PrintedBook inherits from Book
class PrintedBook(Book):
    def __init__(self, title, author, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type  # e.g., hardcover or paperback

    # Polymorphism: Override read method
    def read(self):
        print(f"Flipping through the physical pages of '{self.get_title()}' ({self.cover_type}).")

# Example usage
if __name__ == "__main__":
    ebook = EBook("Python Basics", "Alice Smith", 250, 5)
    printed = PrintedBook("Learn SQL", "John Doe", 300, "Hardcover")

    ebook.read()       # Polymorphic behavior
    printed.read()     # Polymorphic behavior
