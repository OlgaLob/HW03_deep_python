# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def complect(capacity, items):
    if items[0][1] > capacity:
        return complect(capacity, items[1:])
    include_item = complect(capacity - items[0][1], items[1:])
    include_item.append(items[0])
    exclude_item = complect(capacity, items[1:])
    if sum(item[1] for item in include_item) > sum(item[1] for item in exclude_item):
        return include_item
    else:
        return exclude_item


items_dict = {
    'соль': 1,
    'фонарик': 2,
    'консервы': 4,
    'вода': 3,
    'палатка': 8,
    'спальный мешок': 6
}
max_capacity = 15
items_list = list(items_dict.items())
possible_combinations = complect(max_capacity, items_list)

for item, weight in possible_combinations:
    print(f'Вещь: {item}, Масса: {weight}')
