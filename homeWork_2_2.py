my_list = []
n = input("Сколько элементов будет список: ")
i = 0
while i <= int(n)-1:
    my_list.append(input("Введите число "))
    i += 1
print (my_list)
l = len (my_list)
if l % 2 == 0:
    e = l - 1
else:
    e = l - 2
i = 0
while i <= e:
    s = my_list.pop(i+1)
    my_list.insert(i, s)
    i+=2
print (my_list)

	

