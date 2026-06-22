def correct_sentence(mystr:str):
    mystr.rstrip()
    if not mystr[len(mystr) - 1] == ".":
        mystr = mystr+"."

    if not mystr[0].isupper():
        mystr = mystr[0].upper() + mystr[1:]

    return mystr


print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))