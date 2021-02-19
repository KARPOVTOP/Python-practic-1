#Вариант 5
#Задание 1.1
import math
import cmath

def function1(x):
    return (x**4 + 68*x**5)/(math.cos(x) - math.exp(x) - 67) - (45*x**5 + x**3)/(x**7+(x/25)) - (x**6 - x**2 - 95)

print("Задание 1.1")
print("1)"f'{function1(-2):.2e}')
print("2)"f'{function1(-11):.2e}')
print()

#Задание 1.2

def function2(x):
    if (x < 70):
        return x + 59*x**6
    if (70 <= x < 99):
        return 53*x**5 + 30*x**3
    if (x >= 99):
        return 92*x**3 + x**7 - 20

print("Задание 1.2")
print("1)"f'{function2(77):.2e}')
print("2)"f'{function2(48):.2e}')
print()

#Задание 1.3

def function3(n):
    x = 0
    y = 0
    for i in range(1, n + 1):
        x = x + (i + math.log(i))
    for i in range(n + 1):
        y = y + (i**5 + i**2)
    return 95 * x + y

print("Задание 1.3")
print("1)"f'{function3(27):.2e}')
print("2)"f'{function3(11):.2e}')
print()

#Задание 1.4

def function4(n):
    if n == 0:
        return 2
    else:
        return 1/22 * (function4(n - 1)**2) - 1/76 * function4(n - 1)

print("Задание 1.4")
print("1)"f'{function4(3):.2e}')
print("2)"f'{function4(16):.2e}')
print()
