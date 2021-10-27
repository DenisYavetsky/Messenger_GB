import json
import re
import sys
from socket import socket, AF_INET, SOCK_STREAM
from time import time

from common.Exception import INVALID_PORT, INVALID_START_PARAMETERS, INVALID_IP, MESSAGE_ERROR
from common.Messages import send_message, get_message
from common.Variables import (MAX_PORT, MIN_PORT, DEFAULT_PORT, ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE,
                              ERROR)


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''

    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    presence = {
        ACTION: PRESENCE,
        TIME: time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return presence


def main():
    '''Загружаем параметы коммандной строки'''

    if len(sys.argv) >= 2:
        server_address = sys.argv[1]
        patt = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        if re.match(patt, server_address):
            server_port = sys.argv[2] if len(sys.argv) == 3 else DEFAULT_PORT
            if not server_port.isdigit() or (int(server_port) < MIN_PORT or int(server_port) > MAX_PORT):
                # если порт не число или вне диапазона
                raise INVALID_PORT
        else:
            # неверный IP адрес
            raise INVALID_IP
    else:
        # если некорректны параметры запуска
        raise INVALID_START_PARAMETERS

    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))

    presence_msg = create_presence()
    send_message(transport, presence_msg)

    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (MESSAGE_ERROR, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
