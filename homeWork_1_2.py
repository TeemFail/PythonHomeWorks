tiU = int (input ("Введите время в секундах "))
tiH = tiU//3600
tiM = (tiU - tiH*3600)//60
tiS = tiU - tiH*3600 - tiM*60
print (f"время {tiH}  час {tiM} минут {tiS} секунд")

    

