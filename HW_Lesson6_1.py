import string

my_string = input("Введіть літери через дефіс: ")

if len(my_string) == 3:
    pos_letter1 = string.ascii_letters.find(my_string[0])
    pos_letter2 = string.ascii_letters.find(my_string[2])

    if (pos_letter1 >= 0 and pos_letter2 >= 0) and pos_letter2 >= pos_letter1:
        print(string.ascii_letters[pos_letter1:pos_letter2+1])
