def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        unique_list.append(item)
        return unique_list
    
    unique_list = [1, 2, 2, 3, 4, 3, 1, 2]
    result = remove_duplicates(unique_list)
    print("List without Duplicates:", result)