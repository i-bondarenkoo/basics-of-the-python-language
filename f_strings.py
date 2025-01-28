import datetime

a = 'Hello'
b = 'World'

if __name__ == '__main__':
    print(f'{a} {b}')
    pi = 3.14592
    result = 121
    print(f'{pi:.3f}')
    print(f'{result:06}')
    #заполнить форматирование
    print(f'{result:0^6}')
    print(f'{result:0>6}')
    print(f'{result:0<6}')
    digit = 123456789
    print(f'{digit:,}')
    # работа с датами и временем
    today = datetime.datetime.now()
    print(f'{today:%d-%m-%Y %H:%M}')
    # посчитать процент
    real = 86
    full = 100
    print(f'{real/full:.2%}')