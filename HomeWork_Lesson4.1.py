
# mylist = [0, 1, 0, 12, 3]
# mylist = [0]
# mylist = [1, 0, 13, 0, 0, 0, 5]
mylist = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

count_0 = mylist.count(0)
while count_0 > 0:
    mylist.append(mylist.pop(mylist.index(0)))
    count_0 -= 1
print(mylist)