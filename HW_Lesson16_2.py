import math

class Fraction:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __mul__(self, other):
        new_fraction = Fraction(self.a * other.a, self.b * other.b)
        return self.reduce(new_fraction)

    def __add__(self, other):
        new_fraction = self.calc_comon_denominator(other)
        return self.reduce(Fraction(new_fraction[0].a + new_fraction[1].a, new_fraction[0].b))

    def __sub__(self, other):
        new_fraction = self.calc_comon_denominator(other)
        return self.reduce(Fraction(new_fraction[0].a - new_fraction[1].a, new_fraction[0].b))

    def __eq__(self, other):
        new_fraction = self.calc_comon_denominator(other)
        if new_fraction[0].a == new_fraction[1].a:
            return True
        else:
            return False

    def __gt__(self, other):
        new_fraction = self.calc_comon_denominator(other)
        if new_fraction[0].a > new_fraction[1].a:
            return True
        else:
            return False

    def __lt__(self, other):
        new_fraction = self.calc_comon_denominator(other)
        if new_fraction[0].a < new_fraction[1].a:
            return True
        else:
            return False

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

    @staticmethod
    def reduce(myfraction):
        mymax_self = math.gcd(int(myfraction.a), int(myfraction.b))
        return Fraction(myfraction.a // mymax_self, myfraction.b // mymax_self)

    def get_min_denominator(self, other):
        return math.lcm(self.b, other.b)

    def calc_comon_denominator(self, other):
        denom = self.get_min_denominator(other)
        f1_up = denom / self.b * self.a
        f2_up = denom / other.b * other.a
        return Fraction(f1_up, denom), Fraction(f2_up, denom)


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 7, 6'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3'
f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 1, 6'
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')




