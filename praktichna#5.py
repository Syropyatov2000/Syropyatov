filename = "praktichna#5"
# Відкриття файлуfd = open(filename, "w")
# Запис у файлfor i in range(10):
# A = i*18
# fd.write("%i\t%.1f\n" % (i, A))
# Закриття файлу
# fd.close()
# Читання з файлу
# import csv
# import sys
# filename = "mydata.txt"
# Відкриття файлу
# fd = open(filename, "r")
# Читання даних
# reader = csv.reader(fd, delimiter="\t")
# Виведення змісту файлу
# for row in reader:
# print(row)
# Закриття файлуfd.close()

>>>
>>> d = {}
>>> d
{}
>>> d = {'dict': 1, 'dictionary': 2}
>>> d
{'dict': 1, 'dictionary': 2}

>>>
>>> d = dict(short='dict', long='dictionary')
>>> d {'short': 'dict', 'long': 'dictionary'}
>>> d = dict([(1, 1), (2, 4)]) >>> d {1: 1, 2: 4}
>>>
>>> d = dict.fromkeys(['a', 'b'])
>>> d
{'a': None, 'b': None}
>>> d = dict.fromkeys(['a', 'b'], 100)
>>> d
{'a': 100, 'b': 100}
