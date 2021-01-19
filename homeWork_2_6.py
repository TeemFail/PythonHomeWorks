i = 1
strukt = []
ua = input ("Введем данные? н - отмена ")
while ua != "н":
    tov = input(" Продукт: ")
    pr = input(" Стоимость: ")
    mas = input(" Количество: ")
    ed = input(" Ед.измерения: ")
    strukt.append((i, {"продукт": tov,
                         "стоимость": pr,
                         "количество": mas,
                         "еденицы": ed}))
    ua = input ("Введем данные? н - отмена ")
    i += 1

print(strukt)

print ("""
	
	аналитика
	
	""")
	
aTov = []
aPr = []
aMas = []
aEd = []
i = 0
for i in range (len(strukt)):
    t = strukt[i][1]["продукт"]
    aTov.append (t)
    p = strukt[i][1]["стоимость"]
    aPr.append (p)
    m = strukt[i][1]["количество"]
    aMas.append (m)
    e = strukt[i][1]["еденицы"]
    aEd.append (e)
    i += 1
print (" продукты: ", aTov)
print (" стоимость: ", aPr)
print (" количество: ", aMas)
print (" еденицы: ", aEd)


        

            
        



    
    



	

