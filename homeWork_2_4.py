my_list = input("Введите фразу ")
my_list_new = my_list.split()
i = 0
n = 1
for i in range (len(my_list_new)):
    if len (my_list_new[i])>9:
        print (n, ".", my_list_new[i][0:9])
    else:     	
        print (n, ".", my_list_new [i])
    n += 1
    i += 1



    
    



	

