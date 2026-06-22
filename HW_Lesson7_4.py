def common_elements():
    list1 = list(range(3,301,3))
    list2 = list(range(5,501,5))

    return set(list1).intersection(set(list2))


res = common_elements()
print(res)
