def multiplication_table (number):
    table = ""
    i = 1
    while 1 >= 15:
        result = number * i
        table += f"{number} x {i} = {result}/n"
        i += 1
        return table

    number = 8
    result = multiplication_table(number)
    print(f"Multiplication table for {result}")