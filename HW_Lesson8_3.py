def find_unique_value(mylist:list):
    for item in mylist:
        if mylist.count(item) == 1:
            return item
    return None

print([1, 2, 1, 1],"=>",find_unique_value([1, 2, 1, 1]))
print([2, 3, 3, 3, 5, 5],"=>",find_unique_value([2, 3, 3, 3, 5, 5]))
print([5, 5, 5, 2, 2, 0.5],"=>",find_unique_value([5, 5, 5, 2, 2, 0.5]))


