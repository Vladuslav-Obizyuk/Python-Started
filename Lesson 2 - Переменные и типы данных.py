# Дополнительное задание.

# Програма яка питає радіус круга і вираховує площу S = Пr**2.

radius = int(input("Какой радиус кола: "))

if radius >= 0:
    print("Площа = ", 3.14 * radius ** 2)
else:
    print("Введите положительное число")

# -----------------------------------------
# 1) Task.

# Питає два слова і виводить їх через кому.

a = str(input("First word: "))
b = str(input("Second word: "))

print(a, b)
# -----------------------------------------
# 2) Task

# Программа яка питає три целих числа a, b, x і
# виводить True якщо х стоїть між a и b, іначе False.

a = int(input("Number One: "))
x = int(input("Number Two: "))
b = int(input("Number Three: "))

if a < x < b:
    print("True")
else:
    print("False")
