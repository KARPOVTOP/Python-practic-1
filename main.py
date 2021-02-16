#Вариант 5
#Задание 1.1
import math


def function1(x):
    return (x**4 + 68*x**5)/(math.cos(x) - math.e**x - 67) - (45*x**5 + x**3)/(x**7+(x/25)) - (x**6 - x**2 - 95)

print("1)"f'{function1(-2):.2e}')
print("2)"f'{function1(-11):.2e}')

#Задание 1.2

def function2(x):
    if (x < 70):
        return x + 59*x**6
    if (70 <= x < 99):
        return 53*x**5 + 30*x**3
    if (x >= 99):
        return 92*x**3 + x**7 - 20

print("1)"f'{function2(77):.2e}')
print("2)"f'{function2(48):.2e}')

#Задание 1.3

def function3(n):
    x = 0
    y = 0
    for i in range(n + 1):
        x = x + (i**6 + math.sin(i) - 14)
    for i in range(n + 1):
        y = y + (i**4 - math.sin(i))
    return x + y

print("1)"f'{function3(69):.2e}')
print("2)"f'{function3(43):.2e}')

#Задание 1.4

def function4(n):
    if n == 0:
        return 4
    else:
        return math.cos(function4(n - 1)) - 1/96 * function4(n - 1)**3

print("1)"f'{function4(14):.2e}')
print("2)"f'{function4(10):.2e}')
