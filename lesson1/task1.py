# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
# соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

s1 = 'сокет'
s1_unicode = '\u0441\u043e\u043a\u0435\u0442'
print(type(s1_unicode))   # <class 'str'>

s2 = 'декоратор'
s2_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(s2_unicode))   # <class 'str'>

s3 = 'разработка'
s3_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(type(s3_unicode))   # <class 'str'>
