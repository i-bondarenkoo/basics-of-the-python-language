#анонимная функция
#можно писать все, что допустимо после return в def(обычной функции)
#не выполняется до вызова ()!!!

from operator import attrgetter, itemgetter
# возвести в квадрат
square = lambda x: x**2
# четный/нечетный элемент
even_odd = lambda digit: 'Even' if digit % 2 == 0 else 'Odd'
# квадраты четных чисел
ints = list(range(10))
result = list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints)))

#отсортировать ключи по алфавиту
a_dict = {
    'a': 3,
    'b': 2,
    'd': 1,
    'c': 4,
}
res = sorted(a_dict.items(), key=lambda x: x[0])
# x[0] - сортирует по ключам
# x[1] - сортирует по значениям
# еще один способ фильтрации по ключу, но без лямбда функции
# res = sorted(a_dict.items(), key=itemgetter(1))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'    

if __name__ =='__main__':
    print(square(3))
    print(even_odd(4))
    print(even_odd(5))
    print(result)
    print(res)
    cats = [Cat('Tom', 42), Cat('Angela', 3)]
    # сортируем по ключу, в этом примере по возрасту
    print(sorted(cats, key=lambda cat: cat.age))
    # еще один способ фильтрации но без лямбда функции
    # print(sorted(cats, key=attrgetter('age')))
