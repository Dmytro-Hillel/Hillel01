import string

my_string = input("Введіть рядок: ")

for char in string.punctuation:
     my_string = my_string.replace(char, ' ')

my_parts = my_string.split(" ")
for it in range(len(my_parts)):
    my_parts[it] = my_parts[it].lower().capitalize()

hashtag = ('#' + ''.join(part.capitalize() for part in my_parts))[:140]
print(hashtag)

