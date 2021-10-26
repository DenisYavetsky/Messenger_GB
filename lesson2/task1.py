# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
# в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().
import re
import csv

files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
params = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data(files: list) -> list:
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for file in files:
        with open('files/' + file, 'r', encoding='windows-1251') as f:
            for line in f:
                for i, p in enumerate(params):
                    res = re.match(p, line)
                    if type(res) == re.Match:
                        main_data[i].append(line.split(':')[1].strip())
    main_data.insert(0, params)
    # main_data по заданию получается вот такой, что потом неудобно записывать в файл
    # [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'],
    # ['LENOVO', 'ACER', 'DELL'],
    # ['Microsoft Windows 7 Профессиональная', 'Microsoft Windows 10 Professional', 'Microsoft Windows 8.1 Professional'],
    # ['00971-OEM-1982661-00231', '00971-OEM-1982661-00231', '00971-OEM-1982661-00231'],
    # ['x64-based PC', 'x64-based PC', 'x86-based PC']]
    return main_data


def write_to_csv():
    data = get_data(files_list)
    with open('files/info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data[0])
        for i in range(3):
            row = data[1][i], data[2][i], data[3][i], data[4][i]
            csv_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv()
