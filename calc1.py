from math import *

def calc(num1, num2, num3):
    if pow(num1, num2) == num3:
        return("correct")
    elif pow(num1, num2) <= num3:
        return("less\n" + str(num1) + " ^ " + str(num2) + " = " + str(pow(num1, num2)))
    else:
        return("more\n" + str(num1) + " ^ " + str(num2) + " = " + str(pow(num1, num2)))

try:
    num1 = float(input("num 1 "))
    num2 = float(input("num 2 "))
    num3 = float(input("result "))
    print(calc(num1, num2, num3))
except ValueError as er1:
    print(er1)
except OverflowError as er2:
     print(er2)
