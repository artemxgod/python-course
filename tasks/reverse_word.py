def reverse_words(input_str):
    out = input_str.split()  # Разделяет строку на слова, игнорируя лишние пробелы
    out.reverse()  # Переворачивает порядок слов в списке
    delim = " "  # Определяем разделитель, в данном случае пробел
    return delim.join(out)  # Объединяет слова обратно в строку с пробелами между ними

input_str = input("Enter a string: ")
print(reverse_words(input_str))
