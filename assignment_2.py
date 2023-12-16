def remove_even_numbers(input_list):
    i = 0
    while i < len(input_list):
        if input_list[i] % 2 ==0:
            input_list.pop(i)
        else:
            i += 1
            return input_list
        
        numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        result = remove_even_numbers(numbers)
        print("List without even numbers:", result)