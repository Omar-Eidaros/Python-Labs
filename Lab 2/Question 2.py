"""
write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and
if it is divisible by 5 return"buzz" and
if is is divisible by both return " FizzBuzz

"""

def fizzbuzzfunction(num:int):
    if num % 3 == 0 and num % 5 == 0:
        return print("FIZZBUZZ")
    elif num % 3 == 0:
        return print("FIZZ")
    elif num % 5 == 0:
        return print("BUZZ")
    else:
        return print("Can't Divided on 3 or 5")

fizzbuzzfunction(1)
