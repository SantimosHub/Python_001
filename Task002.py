# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number_of_boats = int(input('Введите число корабликов: '))
if number_of_boats % 6 == 0:
    pite_or_serg_boats = int(number_of_boats / 6)
    kate_boats = pite_or_serg_boats * 4
    print(f'Петя:{pite_or_serg_boats} Катя:{kate_boats} Сережа:{pite_or_serg_boats}')
else:
    print('С таким колличеством корабликов задача не решается.')
