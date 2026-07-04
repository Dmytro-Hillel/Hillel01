
def is_prime(number: int):
    if number < 2:
        return False

    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False

    return True


def prime_generator(mylimit: int):
    number = 2

    while number <= mylimit:
        if is_prime(number):
            yield number

        number += 1


print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
