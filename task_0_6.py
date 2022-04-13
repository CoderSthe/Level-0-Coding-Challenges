def maximum(num_1, num_2, num_3):
    
    if num_1 > num_2:
        if num_1 > num_3:
            max_num = num_1
        else:
            max_num = num_3
    else:
        max_num = num_2

    return max_num

print("The maximum value is: ", maximum(10, 5, 8))
