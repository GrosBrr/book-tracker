class Book:
    """Модель книги."""
    def __init__(self, author: str, title: str, rating: int, date_read: str):
        self.author = author
        self.title = title
        self.rating = rating
        self.date_read = date_read

    def to_dict(self) -> dict:
        """Сериализация в словарь для JSON."""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "date_read": self.date_read
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Десериализация из словаря."""
        return Book(
            author=data["author"],
            title=data["title"],
            rating=data["rating"],
            date_read=data["date_read"]
        )

    def __repr__(self):
        return f"Book({self.author!r}, {self.title!r}, {self.rating}, {self.date_read!r})"