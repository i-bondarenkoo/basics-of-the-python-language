
class LibraryItem:
    def __init__(self, title: str, year: int):
        self.__title = title
        self.year = year
        
    def get_title(self):
        return self.__title

    def update_title(self, new_title: str):
        if not new_title.strip():
            raise ValueError("Название не может быть пустым.")
        self.__title = new_title
    


class Book(LibraryItem):
    def __init__(self, title: str, year: int, author: str, pages: int):
        super().__init__(title, year)
        
        self.author = author
        self.pages = pages
    def get_info(self):
        # так как атрибут title приватный использовать его напрямую нельзя
        #лучше всего через get_title метод
        #get_title() именно вызвать
        return f'Книга {self.get_title()} была выпущена в {self.year} году. Она содержит {self.pages} страниц, ее написал {self.author}'
    
    # Почему нельзя обращаться к __title:
    # Механизм name mangling переименовывает __title в _LibraryItem__title, чтобы избежать конфликта имен при наследовании.
    # Это сделано для защиты от случайных изменений приватных атрибутов из подклассов.


class Magazine(LibraryItem):
    def __init__(self, title: str, year: int, issue_number: int):
        super().__init__(title, year)     
        #Номер выпуска  
        self.issue_number = issue_number            
    
    def get_info(self):
        #так делать нельзя
        # return f'Книга была выпущена в {self.year}, ее название {self.__title}, номер выпуска {self.issue_number}'
        return f' Журнал был выпущен в {self.year}, его название {self.get_title()}, номер выпуска {self.issue_number}'
    
    
class DVD(LibraryItem):
    def __init__(self, title: str, year: int, director: str, duration: int):
        super().__init__(title, year)
        #Режиссер                   
        self.director = director
        #продолжительность в минутах
        self.duration = duration
        
    def get_info(self):
        return f'Фильм был выпущен в {self.year}, его название {self.get_title()}, режиссер {self.director}, продолжительность {self.duration} минут.'
  
    
    
library_item = LibraryItem('Batman, dark knight', 2008)

#создаем новый объект класса
book = Book('Мастер и маргарита', 1882, 'Михаил Булгаков', 777)
# вызываем переопределенный метод
print(book.get_info())   
magazine = Magazine('Comics', 2011, 105)
print(magazine.get_info())
dvd = DVD('Ну погоди!', 2005, 'Артем Артемов', 90)
print(dvd.get_info())


        