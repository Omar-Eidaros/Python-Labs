takeinput = list(input("Enter a text: "))

vowels = ["a","e","i","o","u","A","E","I","O","U"]
breif = ""
for i in range(len(takeinput)):
    if takeinput[i] in vowels:
        breif += takeinput[i]

print(f"The output: {breif}")
