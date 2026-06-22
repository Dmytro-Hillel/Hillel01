def add_one(my_list:list):
    res_num = ""
    for item in my_list:
        if not isinstance(item, int):
            return None
        res_num += str(item)

    res_num = int(res_num)
    res_num += 1
    res_num = str(res_num)

    my_res = []
    for item in res_num:
        my_res.append(int(item))

    return my_res

print(add_one([1,2,3,4]))
print(add_one([9,9,9]))
print(add_one([0]))
print(add_one([9]))


