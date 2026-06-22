def correct_sentence(mystr:str):
    mystr.rstrip()
    if not mystr[len(mystr) - 1] == ".":
        mystr = mystr+"."

    return mystr.capitalize()

print(correct_sentence("greetings, friends"))
print(correct_sentence("hello"))
print(correct_sentence("Greetings. Friends"))
print(correct_sentence("Greetings, friends."))
print(correct_sentence("greetings, friends."))