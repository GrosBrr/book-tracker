from models import Book
from typing import List

def average_rating(books: List[Book]) -> float:
    """Средняя оценка по всем книгам. Если книг нет, возвращает 0.0."""
    if not books:
        return 0.0
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)

def author_stats(books: List[Book]) -> dict:
    """
    Статистика по авторам: количество прочитанных книг.
    Возвращает словарь {автор: количество}.
    """
    stats = {}
    for book in books:
        stats[book.author] = stats.get(book.author, 0) + 1
    return stats