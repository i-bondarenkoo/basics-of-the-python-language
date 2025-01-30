# с помощью * можно поместить некоторое количество элементов, в переменную а // *a, b = 1, 2, 3
# также с помощью * можно распаковать последовательность, например print(*[1, 2, 3]) -> 1 2 3
#args - позиционные аргументы, распаковываются в кортеж(неизменяемый типа)
# kwargs - именованные аргументы, распаковываются в словарь
*a, b = 1, 2, 3

def example(a, b, c):
    print(a)
    print(b)
    print(c)

def my_print(*args, **kwargs):
    print(f'Got keywords: {kwargs}')
    for arg in args:
        print(str(arg))

if __name__ == '__main__':
    # print(f'{a=}')
    # print(f'{b=}')
    #именованные аргументы
    # example(a=1, b=2, c=3)
    my_print(1, 2, 3, 4, number=2)