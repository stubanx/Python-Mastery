
## Assignment: Implementing Data Abstraction in Python

### Problem Statement:
You are tasked with designing a simple library management system. The system should handle different types of media, such as books, DVDs, and e-books. Your goal is to demonstrate data abstraction by creating an abstract class and its concrete subclasses.

### Requirements:
1. Create an abstract class called `MediaItem` with the following abstract methods:
    - `get_title()`: Returns the title of the media item.
    - `get_type()`: Returns the type of media (e.g., "Book," "DVD," or "E-book").
    - `get_details()`: Returns additional details specific to the media item (e.g., author for books, director for DVDs).

2. Implement three concrete subclasses:
    - `Book`: Represents a physical book. It should have attributes for title, author, and ISBN.
    - `DVD`: Represents a DVD. It should have attributes for title, director, and release year.
    - `EBook`: Represents an electronic book. It should have attributes for title, author, and file format (e.g., PDF, EPUB).

3. Create instances of each subclass and demonstrate the following:
    - Accessing the title, type, and details of each media item.
    - Showcasing how data abstraction allows users to interact with the essential information without knowing the internal implementation details.

### Example Usage:
```python
from abc import ABC, abstractmethod

class MediaItem(ABC):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_details(self):
        pass

class Book(MediaItem):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_title(self):
        return self.title

    def get_type(self):
        return "Book"

    def get_details(self):
        return f"Author: {self.author}, ISBN: {self.isbn}"

# Similar implementations for DVD and EBook classes

# Example usage
book = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
print(f"Title: {book.get_title()}")
print(f"Type: {book.get_type()}")
print(f"Details: {book.get_details()}")
```

### Assessment:
 create your own instances of `DVD` and `EBook` classes, and demonstrate how data abstraction simplifies interactions with these media items. explore additional attributes and methods for each subclass.

Remember, data abstraction allows us to focus on the essential aspects of an object while hiding the underlying complexity. Happy coding! 📚🎥💻⁶⁷

