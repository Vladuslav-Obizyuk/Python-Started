# Дополнительное завдание.

# зробити калькулятор який може +, -, *, /, в степінь, синус, косинус и тагнес числа.
import math

operation = input("""
+
-
*
/
**
sin
cos
tan 
Select operation: """)

x = int(input("Enter first number: "))

y = int(input("Enter second number: "))


if operation == "+":
    print("Result: ", x + y)
elif operation == "-":
    print("Result: ", x - y)
elif operation == "*":
    print("Result: ", x * y)
elif operation == "/":
    print("Result: ", x / y)
elif operation == "**":
    print("Result: ", x ** y)
elif operation == "sin":
    print("Result from the first number: ", math.sin(x))
elif operation == "cos":
    print("Result from the first number: ", math.cos(x))
elif operation == "tan":
    print("Result from the first number: ", math.tan(x))
else:
    print("Unsupported operation")


# ------------------------------------------------------------------
# 1) Task.

# Программа яка питається ім`я і якщо воно сходиться з моїм то видає вибране повідомленя.

name = input("Enter your name: ")

if name == "Vlad":
    print("What`s up. You have entered", name)
else:
    print("Your name differs from mine")
