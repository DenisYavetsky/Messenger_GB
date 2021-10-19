# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

s1 = b'class'

print(type(s1))     # <class 'bytes'>
print(len(s1))      # 5

s2 = b'function'

print(type(s2))     # <class 'bytes'>
print(len(s2))      # 8

s3 = b'method'

print(type(s3))     # <class 'bytes'>
print(len(s3))      # 6