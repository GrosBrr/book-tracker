from models import Book
from storage import add_book, get_all_books, delete_book
from stats import average_rating, author_stats
from datetime import date

def main_menu():
    while True:
        print("\n=== Трекер прочитанных книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            author = input("Автор: ").strip()
            title = input("Название: ").strip()
            rating_str = input("Оценка (1–5): ").strip()
            date_str = input("Дата прочтения (ГГГГ-ММ-ДД): ").strip()

         
            try:
                rating = int(rating_str)
                if not (1 <= rating <= 5):
                    raise ValueError
                date.fromisoformat(date_str)  
            except ValueError:
                print("Ошибка: оценка должна быть целым числом от 1 до 5, дата — в формате ГГГГ-ММ-ДД.")
                continue

            book = Book(author, title, rating, date_str)
            if add_book(book):
                print("Книга добавлена.")
            else:
                print("Такая книга уже есть в списке!")

        elif choice == "2":
            books = get_all_books()
            if not books:
                print("Список книг пуст.")
            else:
                for i, b in enumerate(books, 1):
                    print(f"{i}. {b.author} – {b.title} | Оценка: {b.rating} | Дата: {b.date_read}")

        elif choice == "3":
            books = get_all_books()
            avg = average_rating(books)
            print(f"Средняя оценка: {avg}")

        elif choice == "4":
            books = get_all_books()
            stats = author_stats(books)
            if not stats:
                print("Нет данных для статистики.")
            else:
                for author, count in stats.items():
                    print(f"{author}: {count} книг(а)")

        elif choice == "5":
            author = input("Автор книги для удаления: ").strip()
            title = input("Название: ").strip()
            if delete_book(author, title):
                print("Книга удалена.")
            else:
                print("Книга не найдена.")

        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()