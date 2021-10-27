# 1) Task
# Функція яка виводить привітання для користувача з заданим ім`ям.
# Якщо ім`я не зазначено то виволить привітання для користувача з моїм іменем.

your_name = input("Enter your name: ")

def hello(name='Vlad'):
    if your_name == "":
        print('Hello', name, '!')
    else:
        print('Hello, ', your_name, '!')

hello()

# --------------------------------------------------

# доп задание
# Создайте программу которая состоит из функции,
# которая принимает три числа и возвращает их среднее арифметическое,
# и главного цикла, спрашивающего у пользователя числа
# и вычисляющего их средние значение при помощи созданой функции

a = int(input("Enter (a): "))
b = int(input("Enter (b): "))
c = int(input("Enter (c): "))

numbers = [a, b, c]

def mean(numbers_array):
    add = 0
    for i in range(0, len(numbers_array)):
        add += numbers_array[i]
    add = round(add / len(numbers_array), 2)
    return add

print(mean(numbers))


