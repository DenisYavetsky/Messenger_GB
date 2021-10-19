# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s1 = b'attribute'
print(type(s1))       # <class 'bytes'>

# s2 = b'класс'       # bytes can only contain ASCII literal characters
s2 = bytes('класс', 'utf-8')
print(type(s2))       # <class 'bytes'>

# s3 = b'функция'     # bytes can only contain ASCII literal characters
s3 = 'функция'.encode('utf-8')
print(type(s3))       # <class 'bytes'>
