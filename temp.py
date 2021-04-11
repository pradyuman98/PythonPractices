def celsius_to_farehenite(temp):
    new_temp= temp*9/5+32
    file=open("Read Me.txt",'a+')
    file.write("\n"+str(new_temp))
    c=file.read()
    print(c)
    return new_temp
temp= int(input(print("Enter temp:-")))

if temp < -273:
   print("Not possible")
else:
     print(celsius_to_farehenite(temp))
