a_list = [0, 0, 1, True]

if any(a_list):
    # 2 способа вывести true значения
    print(list(filter(None, a_list)))
    print([e for e in a_list if e])
    
    
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Cat {self.name=}, {self.age=}'        

if __name__ == '__main__':
    # all проверяет все последовательность, и выводит true
    # если все элементы являются true, пустой список тоже true
    # потому что функция проверяет элементы внутри, а у пустого списка нет элементов
    print(all(a_list))
    # если хотя бы 1 элемент true - функция вернет true
    print(any(a_list))
    cats = [Cat('Tom', 4), Cat('Angela', 3), Cat('Bob', 6)]
    print(max(cats, key=lambda cat: cat.age))
    # iter()
    ints = [int(e) for e in iter(input, '')]
    print(ints)