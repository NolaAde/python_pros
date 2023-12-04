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
    