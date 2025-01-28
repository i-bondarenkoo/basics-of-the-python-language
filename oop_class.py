
from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number
    
    @abstractmethod
    def get_info():
        pass    
    

class Car(Transport):
    def __init__(self, name: str, number: int, color: str, number_of_seats: int):
        super().__init__(name, number)
        self.color = color
        self.number_of_seats = number_of_seats
    # Переопределение метода абстрактного класса    
    def get_info(self):            
        return f'Автомобиль - {self.name}, имеет регистрационный номер - {self.number}, {self.color} цвет. Количество мест для пассажиров {self.number_of_seats}.'
    
    def __str__(self):
        return self.get_info()
    
    # для списка объектов потребуется дополнительная обработка, чтобы использовать строковые представления ваших объектов
    def __repr__(self):
        return self.__str__()

     
class Bus(Transport):
    def __init__(self, name: str, number: int, total_passanger_capacity: int):
        super().__init__(name, number)
        #количество пассажиров
        self.total_passanger_capacity = total_passanger_capacity
    
    # также переопределим абстрактный метод
    def get_info(self):
        return f'Автобус - {self.name}, имеет регистрационный номер - {self.number} и количество мест для пассажиров {self.total_passanger_capacity}.'    
    
    def __str__(self):
        return self.get_info()
    
    # для списка объектов потребуется дополнительная обработка, чтобы использовать строковые представления ваших объектов
    def __repr__(self):
        return self.__str__()


class TransportPark:
    def __init__(self):
        # список объектов Transport
        self.vehicles: list[Transport] = []
       
    def add_vehicle(self, vehicle: Transport):
        self.vehicles.append(vehicle)
        return f'Транспорт успешно добавлен'
    # список всех объектов
    def list_all_vehicles(self):
        if not self.vehicles:
            return "В парке нет транспортных средств"
        return "\n".join(str(elem) for elem in self.vehicles)
    
    #удаление объекта
    def remove_vehicle_by_number(self, number: str):
        if not number:
            return f'Ошибка, некорректное значение'
        for elem in self.vehicles:
            if elem.number == number:
                self.vehicles.remove(elem)
                return f'Элемент успешно удален'
        return f'Совпадений не найдено'
  
    #поиск по номеру
    def find_vehicle_by_number(self, number: str) -> Transport | str:
        if not number:
            return f'Ошибка, укажите номер транспортного средства'
        for elem in self.vehicles:
            if elem.number == number:
                return elem
        return f'Совпадений не найдено'    
    
    #поиск по типу Car Bus
    def find_type_transport(self, type_transport: Transport):
        array = []
        for elem in self.vehicles:
            if isinstance(elem, type_transport):
                array.append(elem)  
        if not array:
            return f'Совпадений не найдено для типа {type_transport.__name__}'           
        return array   
    
    # фильтрация по атрибуту, если есть совпадение 
    def filter_by_attribute(self, attribute: str, value: str | int):
        array = []
        for elem in self.vehicles:
            #проверяем существует ли такой атрибут
            if hasattr(elem, attribute):
                #если существует, в теле получаем его значение
                if getattr(elem, attribute) == value:
                    array.append(elem)
        if not array:
            return f'Совпадений не найдено для атрибута '    
        return array     
    
    # обновить атрибут по номеру
    def update_attribute_for_number(self, number: str, attribute: str, new_value: int):
        if type(number) != str:
            return f'Ошибка, введено не корректное число. Число должно быть целым'
        if not attribute and type(attribute) != str:
            return f'Атрибут не указан или задано неверное значение'
        for elem in self.vehicles:
            if elem.number == number:
                if hasattr(elem, attribute):
                    setattr(elem, attribute, new_value)
                return elem 
            
    #  посчитать количество средств каждого типа       
    def count_transport_for_transport_type(self):
        count_obj_car = 0
        count_obj_bus = 0
        for elem in self.vehicles:
            if isinstance(elem, Car):
                count_obj_car +=1
            elif isinstance(elem, Bus):
                count_obj_bus += 1     
        return f'Количество объектов класса Car: {count_obj_car}, Количество объектов класса Bus: {count_obj_bus} '      
    
    # удалить объекты определенного типа
    def del_object_by_type_obj(self, type: Transport):
        #есть ли объекты указанного типа в списке
        object_to_delete = [elem for elem in self.vehicles if isinstance(elem, type)]       
        # если нет
        if not object_to_delete:
            return f'Такого типа объекта нет в списке'
        #удаляем
        for obj in object_to_delete:
            self.vehicles.remove(obj)
        return self.vehicles, f'Объекты типа: {self.__class__.__name__} успешно удалены.'    
    
    #найти транспорт с атрибутами, соответствующими диапазону значений
    def search_transport_by_value(self, attribute: str, min_value: int, max_value: int):
        for elem in self.vehicles:
            # Проверка для машины (Car)
            if isinstance(elem, Car) and attribute == "number_of_seats":
                value = elem.number_of_seats
            # Проверка для автобуса (Bus)
            elif isinstance(elem, Bus) and attribute == "total_passanger_capacity":
                value = elem.total_passanger_capacity
            else:
                continue  # Если атрибут не соответствует типу, пропускаем

            # Если значение существует и оно целое
            if isinstance(value, int):
                if min_value < value < max_value:
                    return f'Значение объекта {elem} с атрибутом {attribute} находится в диапазоне ({min_value}, {max_value}).'

        return f'Значение атрибута {attribute} не находится в диапазоне для объектов.'

       
car1 = Car('BMW X5', 'a123bc', 'Green', 4)
car2 = Car('Audi Q8', 'z234fa', 'Blue', 4)
car3 = Car('Suzuki', 'a561by', 'Yellow', 7)
bus1 = Bus('MAZ', 'a222ab', 60)
bus2 = Bus('Pazik', 'a431qe', 35)

park = TransportPark()
park.add_vehicle(car1)
park.add_vehicle(car2)
park.add_vehicle(car3)
park.add_vehicle(bus1)
park.add_vehicle(bus2)
# print(park.list_all_vehicles())
# print("----------")
# print(park.remove_vehicle_by_number('a561by'))
# print("----------")
# print(park.list_all_vehicles())
# print("----------")
# print(park.find_vehicle_by_number('a123bc'))
# print("----------")
# print(park.find_vehicle_by_number('a123bd'))
# print("----------")
# print(park.find_type_transport(Car))
# print("----------------")
# print(park.filter_by_attribute('name', 'Audi Q8'))
# print(park.update_attribute_for_number('a123bc', 'color', 'Dark Light'))
print(park.count_transport_for_transport_type())
# print(park.del_object_by_type_obj(Car))
print(park.search_transport_by_value('number_of_seats', 5, 10)) 
print(park.search_transport_by_value('total_passanger_capacity', 30, 40))   
print(park.search_transport_by_value('123', 5, 10)) 



                 