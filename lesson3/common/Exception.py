# Исключения

class BaseException(Exception):
    def __init__(self, code, exc, msg):
        self.code = code
        self.exc = exc
        self.msg = msg

    def __str__(self):
        return self.msg


INVALID_PORT = BaseException(code=400, exc='port_is_invalid', msg='Не верный номер порта')
INVALID_IP = BaseException(code=400, exc='ip_is_invalid', msg='Не верный IP адрес')
INVALID_START_PARAMETERS = BaseException(code=400, exc='invalid_start_parameters', msg='Параметры запуска некорректны')
MESSAGE_ERROR = BaseException(code=400, exc='message_error', msg='Ошибка в приеме сообщения')