my_set = {11,44,19,100,11,100,'код','сервер','код', True, True, False, True}
print(my_set)
my_set.add('сыр')
my_set.discard(44)
print(my_set)

my_dict = {'Мари' : 2006, 'Настя' : 2013, 'Дима' : 1999, 'Никита': 1984}
print('Словарь:', my_dict)
print('Год рождения Мари:', my_dict['Мари'])
print('Год рождения Никита:', my_dict.get('Никита', 'нет такого ключа'))
my_dict.update({'Слава' : 2001, 'Катя' : 2009})
removed_year = my_dict.pop('Слава')
print('Значение удалённого элемента \'Слава\':', removed_year)
print('Изменённый словарь:', my_dict)

print()
