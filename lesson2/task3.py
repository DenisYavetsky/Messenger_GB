# Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
# YAML-формата. Для этого:
# Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
# с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
# Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.

import yaml
from yaml.loader import SafeLoader

dict_yaml = {
    'key1': ['one', 1, True],
    'key2': 10,
    'key3': {4: {5: '\u04E0', 6: '\u14DF'}}
}


def yaml_save(dict_yaml):
    with open('files/file.yaml', 'w', encoding='utf-8') as yaml_file:
        yaml.dump(dict_yaml, yaml_file, default_flow_style=False, allow_unicode=True)


def yaml_read():
    with open('files/file.yaml', 'r', encoding='utf-8') as yaml_file:
        content = yaml.load(yaml_file, Loader=SafeLoader)
    return content


if __name__ == '__main__':
    yaml_save(dict_yaml)
    assert dict_yaml != yaml_read()
