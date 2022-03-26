takeinput = input("Enter a number: ")

if takeinput.isdigit():
    value = int(takeinput)

    for i in range(1,value+1):
        print(f"{value} * {i} = {value * i}")
else:
    print("ReEnter the Value!!")


