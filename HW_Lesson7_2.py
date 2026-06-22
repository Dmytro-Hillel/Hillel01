def second_index(str1:str, str2:str):
    if str1 == "":
        return None
    if str2 == "":
        return None
    pos_begin = str1.find(str2)
    if not pos_begin == -1:
        pos_res = str1.find(str2,pos_begin+1)
        if pos_res == -1:
            return None
        else:
            return pos_res
    else:
        return None

# str1 = input("Введіть перший рядок: ")
# str2 =input("Введіть другий рядок: ")

# print(second_index(str1,str2))
print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello, hello", "lo"))