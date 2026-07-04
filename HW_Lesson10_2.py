import string

def replace_punkts(text):
    punctuation = string.punctuation.replace("'", "")

    symb_repl = []
    for symb in text:
        if symb in punctuation:
            symb_repl.append(symb)

    for symb in symb_repl:
        text = text.replace(symb, " ")
    return (text)


def first_word(mystring:str)->str:
    # mystring = mystring.replace(' ', '')
    # punctuation = string.punctuation
    # punctuation = punctuation.replace("'", "")
    # print(punctuation)
    return list(map(replace_punkts,mystring))



print(replace_punkts("просто текст! Еще текст."))
