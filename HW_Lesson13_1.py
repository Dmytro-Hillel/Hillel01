def delete_tag():
    file_in = open("draft.html", "rt")
    text_in = file_in.read()
    file_in.close()

    skip = False
    text_out = ""
    for symbol in text_in:
        if symbol == "<":
            skip = True
            continue
        if symbol == ">":
            skip = False
            continue

        if not skip:
            text_out = text_out + symbol

    file_out = open("cleaned.txt", "wt")
    file_out.write(text_out)
    file_out.close()


delete_tag()
