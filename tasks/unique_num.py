def unique_elements(input_list):
    output = []

    for num in input_list: 
        if num not in output:
            output.append(num)

    return output

# Запрашиваем ввод списка чисел у пользователя и преобразуем его в список целых чисел
input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split())) 
print(unique_elements(input_list))

def unique_num(input_list):
    """
    Calculates the unique number in a list by XORing all the elements in the list.

    Args:
        input_list (list): A list of integers.

    Returns:
        int: The unique number in the list.
    """
    # Initialize the result to 0.
    res = 0

    # Iterate over each element in the list.
    for num in input_list:
        # XOR the current number with the result.
        res ^= num
    
    # Return the result.
    return res


print(unique_num(input_list))