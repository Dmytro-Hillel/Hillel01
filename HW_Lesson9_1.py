def popular_words (text:str, words:list) -> list:
    text_list=text.lower().split()
    my_res = {}

    for word in words:
        q_word = text_list.count(word)
        my_res[word] = q_word
    return my_res


res = popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])

print(res)
