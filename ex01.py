# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на
# вопросы: ✔ Какие вещи взяли все три друга ✔ Какие вещи уникальны, есть только у одного друга ✔ Какие вещи есть у
# всех друзей кроме одного и имя того, у кого данная вещь отсутствует ✔ Для решения используйте операции с
# множествами. Код должен расширяться на любое большее количество друзей

from pprint import pprint

# Для тренировки использовала это:
# Павел, рюкзак, лыжи, ведро, коньки, спички, хлеб
# Игорь, рюкзак, спички, ведро, хлеб, удочка
# Иван, ведро, спички, хлеб, рюкзак, удочка

n = int(input('Введите количество друзей, отправившихся в поход: '))

items = [input('Введите через запятую имя друга и вещи, которые он взял с собой в поход: ') for _ in range(n)]
print(items)

my_dict = {}
for value in items:
    words = [word.strip(",") for word in value.split()]
    key = words[0]
    values = tuple(words[1:])
    my_dict[key] = values
pprint(my_dict)

all_items = list(my_dict.values())
common_items = set(all_items[0])

for items in all_items:
    common_items = common_items.intersection(set(items))
print(f'Все три друга взяли {common_items}')

uniq_items = {}
for name, items in my_dict.items():
    uniq_items[name] = set(items).symmetric_difference(common_items)
print(f'Эти друзья - большие оригиналы, каждый взял уникальные, сильно полезные вещи в походе: {" ".join("{}: {}".format(k, v) for k, v in uniq_items.items())}')

name_not_atribute = []
new_dict = {}
count = 0
for key, value in my_dict.items():
    name_not_atribute.append(key)
    new_dict[key] = []
    for j in value:
        for k in common_items:
            if k == j:
                count += 1
        if count == 1:
            new_dict[key] += [j]
        if count > 1:
            name_not_atribute.remove(key)
        count = 0
print("у этого списка людей отсутствует вещь, которая дублируется у остальных", name_not_atribute)
