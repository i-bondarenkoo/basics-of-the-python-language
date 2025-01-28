# Условие задачи:
# Представим, что ты разрабатываешь систему управления пользователями для платформы. У тебя есть три типа пользователей:

# User — обычный пользователь.
# Admin — администратор, который может блокировать пользователей.
# Manager — менеджер, который управляет проектами и имеет доступ к определённым ресурсам.

from abc import ABC, abstractmethod
import re
class BaseUser(ABC):
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
    # Возвращает список прав пользователя  
    @abstractmethod  
    def get_permissions(self):
        pass    
    #проверка с помощью регулярных выражений на правильность почты
    @staticmethod
    def is_valid_email(email):
        if not isinstance(email, str):
            return False
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))
   
        
    
class User(BaseUser):
    def __init__(self, username: str, email: str):
        super().__init__(username, email)  
    
    def get_permissions(self):
        return f'У класса {self.__class__.__name__} нет прав для управления системой'
    
    @classmethod
    def create_guest_user(cls):
        return cls('guest', 'guest@example.com')
    
    def __str__(self):
        return "".join(f'Пользователь {self.username}, почтовый адрес {self.email}') 
    
    def __repr__(self):
        return "".join(f'Пользователь {self.username!r}, почтовый адрес {self.email!r}')
    
class Admin(BaseUser):
    def __init__(self, username: str, email: str):
        super().__init__(username, email) 
        self._blocked_users: list[BaseUser] = []   
        
    def get_permissions(self):
        return f'У класса {self.__class__.__name__} есть права управлять системой'
    
    def block_user(self, username: User):
        if not isinstance(username, User):
            return f'Ошибка, не верные данные'
        if username not in self._blocked_users:
            self._blocked_users.append(username)  
        return f'Пользователь {username} добавлен в список заблокированных'   
    
    # Всё работает, но лучше возвращать копию списка (например, self._blocked_users[:]), чтобы защищать закрытую переменную от прямой модификации извне.
    def get_blocked_users(self):
        return self._blocked_users[:]
    
    def __str__(self):
        return "".join(f'Пользователь {self.username}, почтовый адрес {self.email}, список заблокированных пользователей {self._blocked_users}')
    
    def __repr__(self):
        return "".join(f'Пользователь {self.username!r}, почтовый адрес {self.email!r} , список заблокированных пользователей {self._blocked_users!r}')
    
class Manager(BaseUser):
    def __init__(self, username: str, email: str):
        super().__init__(username, email)     
        # список проектов
        self._projects: list[Project] = [] 
    # класс объявлен ниже, поэтому аннотация в качестве строки 
    # либо объявить класс до его использования   
    def get_permissions(self):
        return f'У класса {self.__class__.__name__} нет прав управления системой'
    
    def add_project(self, project: 'Project'):
        if not isinstance(project, Project):
            raise ValueError("Можно добавлять только объекты класса Projects.")
        self._projects.append(project)
        return f'Проект успешно добавлен в список'
    
    def get_projects(self):
        return self._projects
    
    def __str__(self):
        return "".join(f'Пользователь {self.username}, почтовый адрес {self.email}, список проектов {self._projects}')
    
    def __repr__(self):
        return "".join(f'Пользователь {self.username!r}, почтовый адрес {self.email!r} , список проектов {self._projects!r}')
            
        
class Project:
    def __init__(self, name_project: str, price_project: int, run_time_project: int):     
        self.name_project = name_project
        self.price_project = price_project
        self.run_time_project = run_time_project
    
    def get_info_about_project(self):
        return f'Проект - {self.name_project}, в него заложена смета на {self.price_project} и время выполнения проекта {self.run_time_project} дней'   
    
    def __str__(self):
        return "".join(f'Имя проекта {self.name_project} смета для проекта {self.price_project}, время выполнения проекта - {self.run_time_project} дней') 
    
    def __repr__(self):
        return "".join(f'Имя проекта {self.name_project!r} смета для проекта {self.price_project!r}, время выполнения проекта - {self.run_time_project!r} дней') 
    
user1 = User('John', 'john@mail.com')
user2 = User('John', 'john') 
print(user1.get_permissions())
print(user2.get_permissions())
# print(user1.is_valid_email('john@mail.com'))
# print(user2.is_valid_email('john'))
# print(user1.create_guest_user())
admin1 = Admin('Carlos', 'carlos@mail.ru')
admin2 = Admin('Sergey', 'serg@example.com')
# print(admin1.is_valid_email('carlos@mail.ru'))
# print(admin2.is_valid_email('serg@example.com'))
# print(admin1.get_permissions())
print(admin1.block_user('Carlos')) #ошибка нет 2 аргумента
print(admin1.block_user(user1))
# print(admin1.block_user(user2))
print(admin1.get_blocked_users())
manager1 = Manager('Mattiew', 'mat@example.com')
manager2 = Manager('Stepan', 'stepan@example.com')
project1 = Project('Cтроительство дома', 1_000_000_000, 365)
project2 = Project('Cтроительство бани', 1_000, 5)
project3 = Project('Cтроительство небоскреба', 1_000_000, 36)
project4 = Project('Cтроительство дачи', 1_000_000, 35)
project5 = Project('Cтроительство забора', 1_000, 3)
print(manager1.add_project(project1))
print(manager1.add_project(project2))
print(manager2.add_project(project3))
print(manager2.add_project(project4))
print(manager2.add_project(project5))
print(project1.get_info_about_project())
print(project2.get_info_about_project())
print(manager1.get_projects())
print(manager2.get_projects())

           