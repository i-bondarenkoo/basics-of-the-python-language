# # # генератор чисел
# # def squares_generator(n):
# #     for i in range(1, n + 1):
# #         yield i ** 2
        
# # for elem in squares_generator(7):
# #     print(elem)     
    

# # # генератор фибоначчи
# # def fibonacci_generator():
# #     a, b = 0, 1
# #     while True:
# #         yield a
# #         a, b = b, a + b  
        
# # fib_gen = fibonacci_generator()
# # for _ in range(10):
# #     print(next(fib_gen))     

# # # Генератор четных чисел в диапазоне  
# def gen_even_numbers(start, stop):
#     for i in range(start, stop + 1):
#         if i % 2 == 0:
#             yield i
        
# # создадим переменную в которой будет храниться 
# # ссылка на объект генератора
# # чтобы вызывать ее через next()
# obj = gen_even_numbers(1, 5)    
# print(obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# gen_even_numbers = (i for i in range(start, stop + 1) if i % 2 == 0)
#---------------------------------------------------------------------



# # # Создай генератор, который будет выдавать по одному символу из переданной строки.
# def gen_char(string):
#     for char in string:
#         yield char
        
# chars = gen_char('abcdefg')
# print(chars)
# print(next(chars))   
#gen_char = (char for char in string)
#------------------------------------------------------------------------     

# # Напиши генератор, который возвращает все делители заданного числа n.
# def gen_get_devider_number(n):
#     devider = 1
#     while devider <= n:
#         if n % devider == 0:
#             yield devider
#         devider += 1
            
# deviders = gen_get_devider_number(100)  
# print(next(deviders))         
# print(next(deviders))   
# print(next(deviders))    
# print(next(deviders))    
# print(next(deviders))    
  
    
# # Создай генератор, который бесконечно возвращает числа, начиная с 1, увеличивая каждое следующее число на 1.  
# def gen_numbers():
#     index = 1
#     while True:
#         yield index
#         index += 1
        
# generator = gen_numbers()        
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# # Напиши генератор, который возвращает элементы переданного списка в обратном порядке.
# def gen_get_reverse_list(lst):
#     for i in range(len(lst( -1, -1, -1))):
#         yield lst[i]
        
        
# gen = gen_get_reverse_list([1, 4, 6, 2, 6, 8, 0, 1, 3])        
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))        

# # Напиши генератор, который читает файл построчно и возвращает только те строки, которые содержат определённое слово или фразу.
# def gen_get_string():
#     with open('text.txt', 'r', encoding='utf-8') as file:
#         for string in file:
#             string = string.strip()
#             if  'Python' in string:
#                 yield string
                
# test = gen_get_string()
# try: 
#     while True:
#         print(next(test))
# except StopIteration as SI:
#     print('Строки с совпадением закончились')            

# Создай декоратор, который будет автоматически выводить сообщение в консоль каждый раз, когда вызывается функция. 
# В сообщении укажи имя функции и значения всех её аргументов (позиционных и именованных).
# import time
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         stop_time = time.time()
#         if stop_time - start_time > 1:
#             print(f'Функция выполнена быстро')
#         elif stop_time - start_time < 1:
#              print(f'Функция выполнена медленно')
#         return result
#     return wrapper
         
# @decorator
# def get_sum(n):
#     array = sum([i for i in range(1, n+ 1)])  
#     return array
    
    
# print(get_sum(7))    
# print(get_sum(2))
# import datetime

# def daytime_greeting(func):
#     def wrapper(*args, **kwargs):
#         hour = datetime.datetime.now().hour
#         greeting = ""
#         if 6 <= hour < 12:
#             greeting = "Доброе утро"
#         elif 12 <= hour < 18:
#             greeting = "Добрый день"
#         else:
#             greeting = "Добрый вечер"
#         # Включаем результат оригинальной функции в итоговый вывод
#         return f"{greeting}, {func(*args, **kwargs)}"
#     return wrapper

# @daytime_greeting
# def greet(name):
#     return f"{name}!"

# print(greet("Алиса"))

array = sum([i for i in range(1, 10)])
print(array)
