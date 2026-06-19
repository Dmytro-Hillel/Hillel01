import string
import keyword

my_string = input("Введіть рядок: ")

punctuation = string.punctuation.replace("_", "")
punctuation +=" "

myres=True

if my_string == "":
    myres=False

if myres:
    if my_string[0].isdigit() or my_string in keyword.kwlist or "__" in my_string:
        myres = False

if myres:
    for char in my_string:
        if char.isspace() or char.isupper() or char in punctuation:
             myres = False

print(myres)

