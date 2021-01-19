km1day = int (input ("Сколько километров первый день "))
kmRez = int (input ("Какой результат в километрах  "))
i = 0 
tot = km1day
while tot <= kmRez:
    tot = tot + km1day/100*10
    i += 1
print ("Прогресс будет достигнут на ", str (i), " день")