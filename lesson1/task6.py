# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое

with open("files/test_file.txt") as file:
    print(file.encoding)

with open("files/test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')
