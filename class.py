class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True  # Книга доступна по умолчанию
    
    def borrow(self):
        if self.available:
            self.available = False
            return f'Книга "{self.title}" успешно выдана.'
        return f'Книга "{self.title}" недоступна.'
    
    def return_book(self):
        self.available = True
        return f'Книга "{self.title}" возвращена.'
    
    def __str__(self):
        return f'{self.title} ({self.year}), автор: {self.author}'


class Library:
    def __init__(self):
        self.books = []  # Список для хранения объектов книг
    
    def add_book(self, book):
        self.books.append(book)
        return f'Книга "{book.title}" добавлена в библиотеку.'
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f'Книга "{title}" удалена из библиотеки.'
        return f'Книга "{title}" не найдена.'
    
    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            return "Доступные книги:\n" + "\n".join(str(book) for book in available_books)
        return "Нет доступных книг."
    
    #поиск книги по автору 
    def search_book(self, author: str):
        for book in self.books:
            if author.lower() == book.author.lower():
                return f'У этой книги автор - {book.author}'        
        return f'Книги этого автора нет в библиотеке'    
    
    #сортирует книги по году выпуска
    def sort_book_for_year(self):
        sort_book_list = sorted(self.books, key= lambda x: x.year, reverse=False)
        return [str(book) for book in sort_book_list]
                

# Тестирование
library = Library()
book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
book2 = Book("Война и мир", "Лев Толстой", 1869)
book3 = Book("Преступление и наказание", "Федор Достоевский", 1557)

print(library.add_book(book1))
print(library.add_book(book2))
print(library.add_book(book3))

print(book1.borrow())
print(library.list_available_books())

print(book1.return_book())
print(library.list_available_books())
print(library.search_book('Лев толстой'))
print(library.search_book('александр пушкин'))
print(library.sort_book_for_year())