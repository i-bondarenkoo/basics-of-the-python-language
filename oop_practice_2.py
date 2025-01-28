# Разработай систему учёта техники на предприятии, где различаются основные категории техники: 
#     Компьютеры и Принтеры. Общая информация 
#     (например, серийный номер, производитель) 
#     хранится в базовом классе, а специфичные атрибуты и методы — в наследуемых.

#общий класс для всей техники
class Equipment:
    
    def __init__(self, serial_number: int, fabricator: str):
        self.serial_number = serial_number
        #производитель
        self.fabricator = fabricator
    
    def get_info_about_equipment(self):
        return f' Оборудование с серийным номером: {self.serial_number} произведено в {self.fabricator}'   
        
class Computer(Equipment):
    
    def __init__(self, serial_number: int, fabricator: str, operation_system: str = "Unknown", processor_core: int = 1):
        super().__init__(serial_number, fabricator)   
        self.operation_system = operation_system
        self.processor_core =  processor_core
    
    def check_system(self):
        if self.processor_core < 4:
            return (f'Вам всё же стоит задуматься о замене процессора. У вашего процессора всего {self.processor_core} ядра. '
                        f'В современном мире этого может не хватать для комфортной работы.')
        elif self.operation_system:
            return (f'Ваша система {self.operation_system}. Ваш процессор содержит {self.processor_core} ядер, '
                        f'чего достаточно для современных задач.')
        else:
            return 'Информация о системе или процессоре отсутствует.'

        
            
class Printer(Equipment):
    
    def __init__(self, serial_number: int, fabricator: str, printer_type: str = "Лазерный", print_speed: int = 10):
        super().__init__(serial_number, fabricator)
        
        if print_speed <= 0:
            raise ValueError('Скорость печати должна быть положительным числом')
        
        #тип принтера лазерный/струйный
        self.printer_type = printer_type
        #скорост печати страниц в минуту
        self.print_speed = print_speed  
        
    
    def get_info(self):
        if not self.printer_type:
            return "Информация о типе принтера отсутствует."
        if self.print_speed <= 0:
            return "Некорректная скорость печати."

        return (
    f"Ваш принтер произведен в {self.fabricator}, "
    f"имеет {self.printer_type} тип и способен печатать до {self.print_speed} страниц в минуту."
)
       
def check_serial_number(func):
    def wrapper(self, serial_number, *args, **kwargs):
        # Проверяем, есть ли серийный номер в списке
        if serial_number in [item.serial_number for item in self.computer_list] or \
           serial_number in [item.serial_number for item in self.printer_list]:
            return func(self, serial_number, *args, **kwargs)
        else:
            return f"Оборудование с серийным номером {serial_number} не найдено."
    return wrapper        
        
class Inventory:
    
    def __init__(self):
        self.computer_list: list[Computer] = []
        self.printer_list: list[Printer] = []      
        
    def  add_equipment_computer(self, equipment: Computer):
        #Проверка на тип объекта
        if not isinstance(equipment, Computer):
            raise ValueError('Тут должен передаваться объект типа Computer')
        self.computer_list.append(equipment)
        # return self.computer_list
    
    def add_equipment_printer(self, equipment: Printer):
        #проверка на тип объекта
        if not isinstance(equipment, Printer):
            raise ValueError('Тут должен быть объект типа Printer')
        self.printer_list.append(equipment)
        # return self.printer_list      
    
    @check_serial_number
    def delete_num_for_serial_number(self, serial_number: int):
        # Здесь выполняется удаление
        for equipment in self.computer_list:
            if equipment.serial_number == serial_number:
                self.computer_list.remove(equipment)
                return f'Оборудование с номером {serial_number} было успешно удалено из компьютеров.'
        
        for equipment in self.printer_list:
            if equipment.serial_number == serial_number:
                self.printer_list.remove(equipment)
                return f'Оборудование с номером {serial_number} было успешно удалено из принтеров.'
            
            
            

    def show_list_equipment(self):
        # Выводит информацию о каждом объекте в списке компьютеров и принтеров
        computer_info = "\n".join([f"Компьютер с серийным номером {comp.serial_number}, Производитель: {comp.fabricator}" for comp in self.computer_list])
        printer_info = "\n".join([f"Принтер с серийным номером {printer.serial_number}, Производитель: {printer.fabricator}" for printer in self.printer_list])
        
        return f"Список компьютеров:\n{computer_info}\n\nСписок принтеров:\n{printer_info}"

    
# Создание объектов
# obj_eq = Equipment(111, 'Россия')  # Базовое оборудование
obj_comp1 = Computer(222, 'Индия', 'Виндовс 7', 4)  # Компьютер с операционной системой и процессором
obj_print1 = Printer(555, 'Канада', 'Струйный', 25)  # Принтер с типом и скоростью печати
obj_comp2 = Computer(666, 'Америка', 'Виндовс 11', 16)  # Еще один компьютер с ОС и процессором
obj_print2 = Printer(777, 'Австралия', 'Лазерный', 35)  # Принтер с типом и скоростью печати

# Создание инвентаря
obj_invent = Inventory()

# Проверка информации и добавление в инвентарь
# print(obj_eq.get_info_about_equipment())
print(obj_comp1.check_system())
print(obj_print1.get_info())
print(obj_comp2.check_system())
print(obj_print2.get_info())

# Добавление объектов в инвентарь
obj_invent.add_equipment_computer(obj_comp1)
obj_invent.add_equipment_computer(obj_comp2)
obj_invent.add_equipment_printer(obj_print1)
obj_invent.add_equipment_printer(obj_print2)

# Удаление оборудования по серийному номеру и вывод инвентаря
print(obj_invent.delete_num_for_serial_number(111))
print(obj_invent.show_list_equipment())


