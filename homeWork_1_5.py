veer = int (input ("Введите значение выручки "))
izd = int (input ("Введите значение издержек "))
pr = veer - izd
ren = round((pr / veer),3)

if veer > izd:
    print ("Предприятие прибыльное")
    print ("Рентабельность: " + str(ren))    
else:
    print ("Предприятие убыточное")

ch = int (input ("Введите количество работающих "))
pFo = round ((pr / ch), 1)
print ("Прибыль на каждого ", pFo)