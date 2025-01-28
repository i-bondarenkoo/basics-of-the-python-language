# # # closures
# # # Напиши функцию counter(), которая возвращает другую функцию. 
# # # Эта вложенная функция должна каждый раз при вызове увеличивать счетчик на 1 и возвращать его текущее значение.


# # # count в Python является локальной переменной, а внутри inner ты пытаешься её изменить. 
# # # Чтобы Python понял, что ты ссылаешься на переменную из внешнего замыкания, нужно использовать ключевое слово nonlocal.
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

#объект который хранит ссылку на функцию в памяти
count = counter()
print(count())
print(count())
print(count())

# # # Напиши функцию prefixer(prefix), которая принимает строку-префикс и возвращает функцию. 
# # # Эта возвращаемая функция должна добавлять переданный префикс к строкам, которые в неё передают

def prefixer(prefix):

    def inner(name):
        return f'{prefix} {name}'
    return inner

add_hello = prefixer('Hello,')
print(add_hello('Alice'))
print(add_hello('Bob'))

# # # # Напиши декоратор, который перед вызовом функции выводит сообщение 
# # # # "Вызов функции <имя функции>" и затем возвращает результат работы функции.

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции {func.__name__}')
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def gen_list():
    return [x for x in range(10) if x % 2 != 0]

print(gen_list())


# # # Напиши декоратор, который вызывает функцию 3 раза и возвращает результат её последнего выполнения.

def three_times_repeat(func):
    def wrapper(*args, **kwargs):
        result = None
        for _ in range(3):
            result = func(*args, **kwargs)
        return result
    return wrapper


@three_times_repeat
def  greet(name):
    print(f'Hello, {name}')
    return f'Done greeting {name}'

print(greet('Alice'))
print(greet('Alice'))
print(greet('Alice'))

# # # Напиши декоратор с параметром delay, который задаёт задержку (в секундах) перед выполнением функции.
import time
def dec_param(digit: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(digit)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@dec_param(5)
def gen_list():
    return [x for x in range(10) if x % 2 != 0]

print(gen_list())

# # #Напиши декоратор с параметром min_value, который проверяет, чтобы все числовые аргументы функции были не меньше min_value. 
# # # Если хотя бы одно значение меньше, выдавать исключение ValueError.

def dec_min_value(min_value: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)) and arg < min_value:
                    raise ValueError(f'Параметр {arg} меньше минимального значения {min_value}')
            for key, value in kwargs.items():
                if isinstance(value, (int, float)) and value < min_value:
                    raise ValueError(f'Параметр {key}={value} меньше минимального значения {min_value}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@dec_min_value(4)
def add(a: int, b: int):
    return a + b

print(add(5, 4))

# # # Напиши генератор even_numbers(start, stop), который возвращает только чётные числа в диапазоне от start до stop.
def gen_digit(start, stop):
    return (e for e in range(start, stop) if e % 2 == 0)

get = gen_digit(1, 7)
for i in get:
    print(i)


# # Напиши генератор arithmetic_progression(start, step), который бесконечно генерирует числа, начиная с start, с шагом step.
def gen_arithmetic_progression(start, step):
    current = start
    while True:
        yield current
        current += step

generator = gen_arithmetic_progression(1, 2)
for i in generator:
    print(i)        