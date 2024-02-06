def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
    
my_list = [1, 2, 2, 3, 4, 3, 1, 2]
result = remove_duplicates(my_list)
print("List without Duplicates:", result)