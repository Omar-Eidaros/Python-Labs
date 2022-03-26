
myList = []

for i in range(0,5):
     i = int(input("Please enter a value: "))
     myList.append(i)

myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)


