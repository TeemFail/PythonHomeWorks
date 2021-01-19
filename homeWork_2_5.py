my_list = [7, 5, 3, 3, 2]
print ("существующий список ",my_list) 
a = int(input ("дополните список "))
i = 0
for i in range (len(my_list)):
    if my_list [i] >= a:
        i += 1
    else:
        my_list.insert (i, a)
        break
print (my_list) 
        

            
        



    
    



	

