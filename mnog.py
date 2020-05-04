# Cегодня мы попробуем выступить в роли детектива.
# У нас есть множества:
# людей, которые пользуется машиной той же марки, что и убийца;
# людей, которые живут недалеко от мест преступления;
# людей, у которых работа недалеко от мест преступления.

# Обычно имена неуникальны, однако предположим,
# что это номера соцстраховок.

# д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом

chevrolet_owner = {'sam', 'edit', 'semen', 'petr'}
work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}
live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

print("Живут или работают рядом:")
for name in (live_near | work_near): print(name)

suspects = live_near & work_near & chevrolet_owner
print("\nГлавные подозреваемые:")
if suspects:
    for name in suspects: print(name)
else:
    print("Пока некого подозревать.")


