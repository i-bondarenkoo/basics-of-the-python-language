# # Перевернуть строку
# def reverse_str(string):
#     result = string[::-1]
#     return result
    
# print(reverse_str('Python'))    
# print(reverse_str('Hello'))   

# #Проверка полиндрома
# def is_palindrome(a):
#     reverse_a = a[::-1]
#     if reverse_a == a:
#         return True
#     return False
#     #более простое решение
#     # return a == a[::-1] более 
# print(is_palindrome("level"))
# print(is_palindrome("world"))

# def count_words(str_word):
    
#     list_word = str_word.split()
#     return len(list_word)
# print(count_words("Hello world! This is Python."))  
    
    
# def remove_duplicates(list_digit):
#    uniq_digit = set(list_digit)
#    return list(map(int, uniq_digit))
#     # return list(set(list_digit))
   
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))   

# def find_max(spisok):
#     digit = 0
#     # Начальное значение - самое маленькое возможное
#     # digit = float('-inf')
#     for i in spisok:
#         if i > digit:
#             digit = i
#     return digit    
#     # return max(spisok)    
#     # return reduce(lambda x, y: x if x > y else y, spisok)
    
# print(find_max([3, 1, 4, 1, 5, 9]))    

# def shift_list(lst, k):

#     end_list = lst[-k:]
#     first_list = lst[:-k]
#     return  end_list + first_list

        
# print(shift_list([1, 2, 3, 4, 5], 2))    

# def char_frequency(stroka):
#     result_dict = {}
#     for char in stroka:
#         if char in result_dict:
#             result_dict[char] += 1
#         else:
#             result_dict[char] = 1    
#     return result_dict         
    
# print(char_frequency("hello"))    


# def invert_dict(dict_in):
#     new_dict = {}
#     for k, v in dict_in.items():
#         new_dict[v] = k
#     return new_dict    
        
# print(invert_dict({"a": 1, "b": 2, "c": 3}))    



# def second_largest(listing):
#     max_of_list = float('-inf')
#     max_2 = float('-inf')
#     if len(listing) < 2:
#         return None
#     for i in listing: 
#         if i > max_of_list:
#             max_2 = max_of_list
#             max_of_list = i
    
#     return max_2 if max_2 != float('-inf') else None          
    
# print(second_largest([1, 2, 3, 4, 5]))
# print(second_largest([1, 1, 1, 1]))
# print(second_largest([7, 9, 4, 6, 5]))   

# def find_missing(lst, n):
#     result = []
#     lst_set = set(lst)
#     list_range = list(range(1, n + 1))

#     # for i in list_range:
#     #     if i not in lst_set:
#     #         result.append(i)
#     # return result        
#     #вариант с генератором
#     return [i for i in list_range if i not in lst_set]        
    
# print(find_missing([1, 3, 5], 5) )
# print(find_missing([2, 4], 5))
# print(find_missing([1, 2, 3], 5))  
  
  
def get_even_numbers(spisok):
    
    
     return (i for i in spisok if i % 2 == 0)




print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers([7, 8, 9, 10, 11])) 
print(get_even_numbers([1, 3, 5])) 
