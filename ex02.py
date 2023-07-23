# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

my_list = [1, 3, 4, 4, 4, 5, 6, 6, 8, 3, 9, 7, 9]

count = 0
set_list = []

for i in my_list:
    for j in my_list:
        if i == j:
            count += 1
            if j not in set_list and count > 1:
                set_list.append(j)
    count = 0

print(my_list, set_list, sep='\n')
