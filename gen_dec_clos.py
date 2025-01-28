
def gen_numbers(lst):
    return (x for x in lst if x % 2 == 0)
generator = gen_numbers([2, 5, 7, 9, 11, 14, 20])
for i in generator:
    print(i)

# Создай декоратор count_calls, который считает, сколько раз вызвали обёрнутую функцию. 
# Число вызовов выводится каждый раз перед выполнением функции.


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.calls} раз")
        result = func(*args, **kwargs)
        return result
    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello():
    print('Hello')
    
say_hello() 
say_hello()  
say_hello()


def add_suffix(str):
    def suffix(func):
        def wrapper(*args, **kwargs):
            print(f'Декоратор добавляет суффикс!')
            result = func(*args, **kwargs)
            return f'{result} {str}'
        return wrapper
    return suffix

def add_prefix(string):
    def prefix(func):
        def wrapper(*args, **kwargs):
            print(f'Декоратор добавляет префикс!')
            result = func(*args, **kwargs)
            return f'{string} {result}'
        return wrapper
    return prefix


@add_suffix("!!!")
@add_prefix("Hello, ")
def greet(name):
    return name

print(greet('Alice'))

# Напиши функцию accumulator, которая возвращает замыкание. 
# Замыкание должно принимать одно число и добавлять его к общему накопленному значению, а затем возвращать текущую сумму.

def outer():
    total = 0
    def inner(x):
        nonlocal total
        total += x
        return total
    return inner

acc = outer()   
print(acc(10)) 
print(acc(20)) 
print(acc(-100))

import time
def delayed(digit: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'Декоратор откладывает выполнение функции')
            time.sleep(digit)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@delayed(5)
def greet(name):
    return f"Hello, {name}!"
    
print(greet('Alice'))    