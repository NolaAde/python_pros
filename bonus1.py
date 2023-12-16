def caculate_statistics(number):

    count = len(number)

    total = sum(number)

    mean = total / count if count > 0 else 0

    sorted_number = sorted(number)

    if count % 2 == 0:
        
        median = (sorted_number[count // 2 - 1] + sorted_number[count // 2] / 2)
    else:
        median = sorted_number[count // 2]
    
    minimum = min(number) if count > 0 else 0
    maximum = max(number) if count > 0 else 0
    
    print("Total count:", count)
    print("Sum:", total)
    print("Mean (Average)", mean)
    print("Median:", median)
    print("Minimum", minimum)
    print("Maximum", maximum)

number_list = [7, 12, 5, 21, 8, 10, 15]
caculate_statistics(number_list)