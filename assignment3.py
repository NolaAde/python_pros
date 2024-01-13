def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    
my_list = [1, 2, 2, 3, 4, 3, 1, 2]
result = remove_duplicates(my_list)
print("List without Duplicates:", result)

def remove_even_numbers(input_list):
    i = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            input_list.pop(i)
        else:
            i += 1
    return input_list
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = remove_even_numbers(numbers)
print("List without even numbers:", result)

