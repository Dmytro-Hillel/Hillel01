mytemplate = ("yes","y")

MyAnswer = mytemplate[0]
while MyAnswer.lower() in mytemplate:
    numb1 = int(input("Введіть перше число: "))
    numb2 = int(input("Введіть друге число: "))
    Oper = input("Введіть операцію: ")

    if Oper == "+":
        print(numb1+numb2)
    elif Oper == "-":
        print(numb1-numb2)
    elif Oper == "*":
        print(numb1*numb2)
    elif Oper == "/":
        if numb2==0:
            print("Помилка. Ділення на нуль")
        else:
            print("Результат операції",numb1/numb2)
    else:
        print("Невідома операція")

    MyAnswer = input("Продовжити?")

