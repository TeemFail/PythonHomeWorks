my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = input("Введите месяц в цифровом формате ")
if 12<int(n) or int(n)<0:
    print ("нет таких месяцев")
d = 1 + my_list.index(int(n))
if int(d)<=2 or int(d)>10:
    print ("зима")
elif int(d)<=5 and int(d)>2:
    print ("весна")
elif int(d)<=8 and int(d)>5:
    print ("лето")
if int(d)<=10 and int(d)>8:
    print ("осень")    
    
print ("а теперь через dict")

my_dict = {1:"зима",2:"весна",3:"лето",4:"осень"}
n = input("Введите месяц в цифровом формате ")
if 12<int(n) or int(n)<0:
    print ("нет таких месяцев")
if int(n)<=2 or int(n)>10:
    w = 1
elif int(n)<=5 and int(n)>2:
    w = 2
elif int(n)<=8 and int(n)>5:
    w = 3
if int(n)<=10 and int(n)>8:
    w = 4
m = my_dict[w]
print (m)

    
    



	

