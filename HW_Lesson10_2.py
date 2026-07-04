import string


def replace_punkts(text: str) -> str:
    symb_repl = set(string.punctuation.replace("'", "")) & set(text)

    for symb in symb_repl:
        text = text.replace(symb, " ")
    return (text)


def first_word(mystring: str)->str:
    my_temp_str = replace_punkts(mystring)

    return list(my_temp_str.split())[0]


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))