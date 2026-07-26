def rotate_left_inplace(my_list):
    if not my_list:
        return my_list      
    first_element = my_list[0]
    for i in range(len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    my_list[-1] = first_element
    return my_list
numbers = [10, 20, 30, 40, 50]
print(rotate_left_inplace(numbers))

