import string
import keyword

my_string = input("Введіть рядок: ")

punctuation = string.punctuation.replace("_", "__")
punctuation +=" "

myres=True
if my_string == "":
    myres=False

myres = (not my_string[0].isdigit()) & (my_string not in keyword.kwlist)

if myres:
    for char in my_string:
        if char in punctuation or  (char.isspace() or char.isupper()):
            myres=False

print(myres)
