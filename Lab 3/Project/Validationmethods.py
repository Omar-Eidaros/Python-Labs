import re


def checkdate(date):
    regex = "[\d]{1,2}/[\d]{1,2}/[\d]{4}"
    while True:
        if re.match(regex,date):
            return date
        else:
            print("Invalid Date Format!!, Date should be in this format [dd/mm/yyyy]")
            date = input("Re-Enter Date: ")
            continue
