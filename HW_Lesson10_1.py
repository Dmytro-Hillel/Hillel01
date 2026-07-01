def my_generator(myfunc, begin, n):
    for _ in range(n):
        yield begin
        begin = myfunc(begin)


def myfunc1(item):
    return item+10


def myfunc2(item):
    return item*2


my_res = my_generator(myfunc1, 10, 3)
print(list(my_res))
my_res = my_generator(myfunc2, 5, 5)
print(list(my_res))
