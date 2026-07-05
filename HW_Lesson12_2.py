
def mycube(stop: int):
    start = 2
    while True:
        curr = start ** 3
        start += 1
        if curr > stop:
            break
        yield curr


def generate_cube_numbers(mylimit: int):
        myres = []
        for it in mycube(mylimit):
            myres.append(it)

        return myres


print(generate_cube_numbers(10))
print(generate_cube_numbers(100))
print(generate_cube_numbers(1000))
