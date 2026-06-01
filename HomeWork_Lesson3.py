
# Завдання 3.1 Найпростіший калькулятор
print()
print("Завдання 3.1 Найпростіший калькулятор")
numb1=int(input("Введіть перше число: "))
numb2=int(input("Введіть друге число: "))
Oper=input("Введіть операцію: ")

if Oper=="+":
    print(numb1+numb2)
elif Oper=="-":
    print(numb1-numb2)
elif Oper=="*":
    print(numb1*numb2)
elif Oper=="/":
    if numb2==0:
        print("Помилка. Ділення на нуль")
    else:
        print("Результат операції",numb1/numb2)
else:
    print("Невідома операція")

# Завдання 3.2 Перемістити елемент у списку
print()
print("Завдання 3.2 Перемістити елемент у списку")
mylist=[1,2,3,4,5,6,7]
print(mylist)
len_list=len(mylist)

if len_list==0 or len_list==1:
    print("Кількість:", len_list, "Не змінюємо")
else:
    mylist.insert(0,mylist.pop(len_list-1))
    print(mylist)

# Завдання 3.3 Розділити один список на два списки
print()
print("Завдання 3.3 Розділити один список на два списки")

print("Парна кількість")
mylist=[1,2,3,4,5,6]
len0=len(mylist)
len2=len0//2
len1=len0-len2

list1=mylist[:len1]
list2=mylist[len1:]
print("List: ",mylist)
print("List 1: ",list1)
print("List 2: ",list2)

print("Непарна кількість")
mylist=[1,2,3,4,5,6,7]
len0=len(mylist)
len2=len0//2
len1=len0-len2

list1=mylist[:len1]
list2=mylist[len1:]
print("List: ",mylist)
print("List 1: ",list1)
print("List 2: ",list2)

print("Нульова кількість")
mylist=[]
len0=len(mylist)
len2=len0//2
len1=len0-len2

list1=mylist[:len1]
list2=mylist[len1:]
print("List: ",mylist)
print("List 1: ",list1)
print("List 2: ",list2)