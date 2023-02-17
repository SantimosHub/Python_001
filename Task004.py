# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

choko_lenght = int(input('Введите кол-во долек в длину: '))
choko_width = int(input('Введите кол-во долек в ширину: '))
choko_crack = int(input('Введите сколько долек надо отломить: '))

if choko_crack % choko_width != 0 and choko_crack % choko_lenght != 0 or choko_crack > choko_width * choko_lenght:
    print('Нельзя отломить')
else:
    print('Можно отломить')
