import random

len_list = random.randint(3,10)

mylist = [len_list]
for i in range(len_list-1):
    mylist.append(random.randint(1,10))

mylist2=[]
mylist2.append(mylist[0])
mylist2.append(mylist[2])
mylist2.append(mylist[-2])

print(mylist)
print(mylist2)
