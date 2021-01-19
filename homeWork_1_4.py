m = input (" введите число ")
n = len (m)
t = 0
i = 0
while i != n:
    if int (t) < int (m[i]):
        t = m[i]
        i = i + 1
    else:
        i = i + 1
print ("Самая большая цифра", str(t))
        
   
