sizes = [5,7,300,90,24,50,75]
print("Hello, my name is Manh and these are my ship sizes")
print(sizes)
biggest = sizes[1]
pos = 0
for i in range(len(sizes)):
 if sizes[i] >= biggest:
     biggest = sizes[i]
print("My biggest sheep has size",biggest)
sizes[sizes.index(biggest)] = 8
print("After shearing, here is my flock")
print("")

for i in range (1,5):
 w = [ size + 50 for size in sizes]
 sizes = w
 print("Month", i , ":")
 print("One month has passed, now here is my flock sizes")
 print(w)
 biggest = sizes[1]
 for i in range(len(sizes)):
     if sizes[i] >= biggest:
         biggest = sizes[i]
 print("My biggest sheep has size",biggest)
 sizes[sizes.index(biggest)] = 8
 print("After shearing, here is my flock")
 print("")

total = 0
for i in range (len(sizes)):
 total = total + sizes[i]
print("My flock has size in total:",total)
money = total *2
print("I would get",total,"*2 =", total*2,"$") 
