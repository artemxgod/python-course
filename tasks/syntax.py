# Задача 1: Четные и нечетные числа
# Напиши функцию, которая принимает список чисел и возвращает два списка: один с четными числами, другой с нечетными.

def split_even_odd(input_list):
    even_list, odd_list = [], []

    for num in input_list:
        if num & 1  == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list

input_list = list(map(int, input("enter numbers: ").split()))
print(split_even_odd(input_list))

# Задача 2: Объединение и сортировка списков
# Напиши функцию, которая принимает два списка чисел, 
# объединяет их в один, удаляет дубликаты и сортирует результат по возрастанию.

def merge_and_sort(list1, list2):
    # Объединяем два списка
    output = list1 + list2
    # Преобразуем в множество для удаления дубликатов, затем обратно в список
    unique = list(set(output))
    # Сортируем список
    unique.sort()
    return unique

# Пример использования функции
print(merge_and_sort([1, 2], [4, 2]))  # [1, 2, 4]
