# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).
s_list = ['разработка', 'администрирование', 'protocol', 'standard']
for s in s_list:
    s_enc = s.encode('utf-8')
    s_dec = s_enc.decode()
    print(s_dec)

