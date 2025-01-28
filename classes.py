
#класс транспортное средство
class Vehicle:
    
    #конструктор
    def __init__(self, make: str, model: str, year: int):
        #марка
        self.make = make
        self.model = model
        self.year = year
        
    def get_info(self):
        return f' Марка машины - {self.make}, модель автомобиля - {self.model}, год выпуска автомобиля - {self.year}'
            
class Car(Vehicle):
    
    def __init__(self, make: str, model: str, year: str, doors: int):
        super().__init__(make, model, year)
        #количество дверей
        self.doors = doors
    
    def get_info(self):
        return f' Ваша автомобиль {self.model}, марки {self.make} имеет {self.doors} двери.'
    
class Truck(Vehicle):
    
    def __init__(self, make: str, model: str, year: str, cargo_capacity : int):
        super().__init__(make, model, year)
        #грузоподъемность
        self.cargo_capacity  = cargo_capacity                          
        
        
    def get_info(self):
        return f' Ваш автомобиль {self.model} может поднять/перевезти {self.cargo_capacity} килограмм.'

class Fleet:
    
    def __init__(self):
        self.list_vihicles = []
        
    
    def add_vehicle(self, vehicle):
        self.list_vihicles.append(vehicle)
        return f' Ваш автомобиль успешно добавлен в список.'
    
    
    def remove_vehicle(self, index):
        try:
            remove_vehicle = self.list_vihicles.pop(index)
            return f'Объект {remove_vehicle.get_info()} успешно удален из списка'
        except IndexError:
            return 'Объекта с таким индексом нет в списке.'
    
    
    def list_info(self):
        return [item.get_info() for item in self.list_vihicles]
    
    
    def search_vehicle(self, info_about_machine: str, value):
        for item in self.list_vihicles:
            # Если атрибут с таким названием существует
            if hasattr(item, info_about_machine):
                attribute_value = getattr(item, info_about_machine)
                # Если значение атрибута совпадает с искомым значением
                if attribute_value == value:
                    # Проверяем, есть ли метод get_info и вызываем его, если он есть
                    if hasattr(item, 'get_info'):
                        return item.get_info()
                    else:
                        return f'Информация о машине не доступна.'
        return f'Автомобиля с параметром {info_about_machine}: {value} нет в списке.'
        
            
        
    def update_vehicle(self, index, field, new_value):
        try:
            #Получаем объект по индексу
            vehicle = self.list_vihicles[index]
            # Проверяем, что у автомобиля есть атрибут с таким названием
            if hasattr(vehicle, field):
                #обновляем значение
                setattr(vehicle, field, new_value)
                return f'Автомобиль обновлен. Новый {field}: {new_value}.'
            else:
                return f'Нет такого поля {field} в автомобиле.'
        except IndexError:
            return f'Объекта с таким индексом нет в списке.'    
        
        
# Создание объектов
vehicle1 = Vehicle("Toyota", "Corolla", 2020)
vehicle2 = Vehicle("Ford", "Focus", 2021)

car1 = Car("Honda", "Accord", 1999, 4)
car2 = Car("BMW", "X5", 2015, 5)

truck1 = Truck("Scania", "FH", 2017, 60000)
truck2 = Truck("Volvo", "FH16", 2018, 80000)

# Создание объекта для автопарка
fleet = Fleet()

# Добавление автомобилей в автопарк
print(fleet.add_vehicle(vehicle1))
print(fleet.add_vehicle(vehicle2))
print(fleet.add_vehicle(car1))
print(fleet.add_vehicle(truck1))
print(fleet.add_vehicle(car2))
print(fleet.add_vehicle(truck2))

# Просмотр информации о всех автомобилях в автопарке
print(fleet.list_info())

# Поиск автомобиля по параметру (например, по модели)
print(fleet.search_vehicle("model", "Accord"))

# Обновление информации об автомобиле
print(fleet.update_vehicle(1, "year", 2000))

# Удаление автомобиля из автопарка
print(fleet.remove_vehicle(2))

# Снова просмотр информации об автомобилях в автопарке после удаления
print(fleet.list_info())

      