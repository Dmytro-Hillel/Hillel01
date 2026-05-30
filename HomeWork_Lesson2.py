
# Завдання 2.1 Квадрат числа
print("Завдання 2.1. Квадрат числа")
number=int(input("Введіть число: "))
print("квадрат числа: ", number ** 2)

# Завдання 2.2 Середнє 3 чисел
print()
print("Завдання 2.2. Середнє 3 чисел")
number1=input("Перше число: ")
number2=input("Друге число: ")
number3=input("Третє число: ")
print("Середнє: ",(int(number1)+int(number2)+int(number3))/3)

# Завдання 2.3 Перетворення хвилин у години
print()
print("Завдання 2.3. Перетворення хвилин у години")
number=input("Введіть кількість хвилин: ")
hours=int(number)//60
minutes=int(number)%60
print("Годин: ",hours,"Хвилин: ",minutes)

# Завдання 2.4 Розрахунок знижки
print()
print("Завдання 2.4. Розрахунок знижки")
price=int(input("Введіть ціну: "))
minus=int(input("Введіть знижку: "))
sum=price-(price*(minus/100))
print("Ціна зі знижкою: ",sum)
print()

# Завдання 2.5 Остання цифра числа
print()
print("Завдання 2.5. Остання цифра числа")
number=int(input("Введіть число: "))
print("Остання цифра: ",number%10)

# Завдання 2.6 Периметр прямокутника
print()
print("Завдання 2.6. Периметр прямокутника")
leg=int(input("Введіть длину: "))
wid=int(input("Введіть ширину: "))
print("Периметр: ", (leg+wid)*2)

# Завдання 2.7 Виведення числа в стовпчик
print()
print("Завдання 2.7. Виведення числа в стовпчик")
number=int(input("Введіть число з 4 цифр: "))

print(number%10)
print(number//10%10)
print(number//100%10)
print(number//1000%10)

