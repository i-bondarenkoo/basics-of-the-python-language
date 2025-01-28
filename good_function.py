# data = []
# value = 8

# def solution():
#     import random 
#     for i in range(5):
#         result = ''.join(str(random.randint(0, 9)) for _ in range(value))
#         print(result)
#         data.append(result)
#     print(data)
#     for index in range(len(data)):
#         if '5' in data[index]:
#             data[index] = data[index].replace('5', '6')
#     with open('test.txt', 'w') as file:
#         file.write('\n'.join(data))
        
        
# if __name__ == '__main__':
#     solution()     

import random
data = []
def generate_digit(value: int) -> str:
    for i in range(5):
        return ''.join(str(random.randint(0, 9)) for _ in range(value))     
        
def replace_fives(a_list: list, value: str) -> str:
    return [elem.replace('5', value) for elem in a_list]      

def replace_fives_inplace(a_list: list, value: str):
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('5', value)
        
def file_write(filename: str, data: str):
    with open(filename, 'w') as file:
        file.write(data)
   
   
if __name__ == '__main__':
    # pins = [generate_digit(8) for _ in range(5)]
    # pins_witout_fives = replace_fives(pins, '6')
    # str_list = '\n'.join(pins_witout_fives)
    # print(pins_witout_fives)
    # file_write('test1.txt', str_list)
    #другая функция
    pins = [generate_digit(8) for _ in range(5)]
    replace_fives_inplace(pins, '6')
    str_list = '\n'.join(pins)
    print(pins)
    file_write('test1.txt', str_list)