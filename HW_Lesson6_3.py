my_numb = input("Введіть число: ")

for char in my_numb:
    if not char.isdigit():
        print("Помилка. Невірне число")
        exit()

my_numb = int(my_numb)

while my_numb > 9:
    temp = my_numb
    res = 1

    while temp > 0:
        digit = temp % 10
        res *= digit
        temp //= 10

    my_numb = res

print(my_numb)