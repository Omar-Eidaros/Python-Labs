""""
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.

"""

def myfunction(length:int, start:int ):
    mylist = []
    for item in range(start,(start + length +1)):
        mylist.append(item)

    print(mylist)

myfunction(10,2);
