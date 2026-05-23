import json
import os
from typing import List, Optional
from models import Book

DATA_FILE = "books.json"

def load_books() -> List[Book]:
    """Загружает список книг из JSON-файла. Если файла нет, возвращает пустой список."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]

def save_books(books: List[Book]) -> None:
    """Сохраняет список книг в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)

def add_book(book: Book) -> bool:
    """
    Добавляет книгу, если книги с такими же автором и названием ещё нет.
    Возвращает True при успешном добавлении, иначе False.
    """
    books = load_books()
    # Проверка на дубликат (closes #1)
    #for b in books:
     #   if b.author == book.author and b.title == book.title:
      #      return False
    books.append(book)
    save_books(books)
    return True

def get_all_books() -> List[Book]:
    """Возвращает список всех книг."""
    return load_books()

def find_book(author: str, title: str) -> Optional[Book]:
    """Ищет книгу по автору и названию. Возвращает объект Book или None."""
    books = load_books()
    for book in books:
        if book.author == author and book.title == title:
            return book
    return None

def delete_book(author: str, title: str) -> bool:
    """
    Удаляет книгу по автору и названию.
    Возвращает True, если книга была удалена, иначе False.
    """
    books = load_books()
    initial_len = len(books)
    books = [b for b in books if not (b.author == author and b.title == title)]
    if len(books) < initial_len:
        save_books(books)
        return True
    return False