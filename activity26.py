from activity25 import taga_triangle
from activity25 import box
from activity25 import sum
from activity25 import my_factorial
import os

while True:
    print("MINI MENU")
    print("SELECT AN OPTION")
    print("1 - Triangle")
    print("2 - Sum")
    print("3 - Box")
    print("4 - Factorial")
    print("5 - EXIT")
    choose = int(input("Which option to go -----> "))

    if choose == 1:
        os.system('cls')
        print("Taga Triangle")
        size = int(input("Size ng Triangle ---> "))
        taga_triangle(size)
        continue
    elif choose == 2:
        os.system('cls')
        print("Simple Summation")
        num1 = int(input("number 1 ---> "))
        num2 = int(input("number 2 ----> "))
        print(f"the sum of {num1} and {num2} is {sum(size)}")
        continue
    elif choose == 3:
        os.system('cls')
        print("BOX")
        size = int(input("Size ng box"))
        box(size)
        continue
    elif choose == 4:
        os.system('cls')
        print("FACTORIAL")
        num = int(input("input any number ---> "))
        print((f"The factorial of {num} is {my_factorial(num)}"))
        continue
    elif choose == 5:
        print("SYSTEM EXIT")
        break
    else:
        print("INVALID CHOICE")
        continue