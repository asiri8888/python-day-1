#create the list named temparature
temparatures = [25.5 , 28.1 , 22.9 , 30.2 , 27.8 , 24.3 , 29.5]
print(temparatures)

#add 31.0 to the end of the list
temparatures.append(31.0)
print(temparatures)

#remove third element (index 2) from the list
temp = temparatures.pop(2)
print(temp)
print(temparatures)

#find the maximum and minimum temp in the lsit
max_temparature = max(temparatures)
print (max_temparature)
min_temparature = min(temparatures)
print(min_temparature)

#try to call index out of the list
temp = temparatures.pop(9)
print(temp) 