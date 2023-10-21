import math


class Multiplication:
    def rec_int_mult(self, x, y, n):
        if n == 1:
            return x * y

        a, b = x // 10 ** math.ceil(n / 2), x % 10 ** math.floor(n / 2)
        c, d = y // 10 ** math.ceil(n / 2), y % 10 ** math.floor(n / 2)

        ac = self.rec_int_mult(a, c, n // 2)
        bd = self.rec_int_mult(b, d, n // 2)
        ad = self.rec_int_mult(a, d, n // 2)
        bc = self.rec_int_mult(b, c, n // 2)

        return 10 ** n * ac + 10 ** (n // 2) * (ad + bc) + bd

    def karatsuba(self, x, y, n):
        if n == 1:
            return x * y

        a, b = x // 10 ** math.ceil(n / 2), x % 10 ** math.floor(n / 2)
        c, d = y // 10 ** math.ceil(n / 2), y % 10 ** math.floor(n / 2)

        ac = self.karatsuba(a, c, n // 2)
        bd = self.karatsuba(b, d, n // 2)
        adbc = self.karatsuba(a + b, c + d, n // 2) - ac - bd

        return 10**n * ac + 10 ** (n // 2) * adbc + bd


class MultiplicationPow2:
    def rec_int_mult(self, x, y, n):
        if n == 1:
            return x * y

        a, b = x // 10 ** (n // 2), x % 10 ** (n // 2)
        c, d = y // 10 ** (n // 2), y % 10 ** (n // 2)

        ac = self.rec_int_mult(a, c, n // 2)
        bd = self.rec_int_mult(b, d, n // 2)
        ad = self.rec_int_mult(a, d, n // 2)
        bc = self.rec_int_mult(b, c, n // 2)

        return 10**n * ac + 10 ** (n // 2) * (ad + bc) + bd

    def karatsuba(self, x, y, n):
        if n == 1:
            return x * y

        a, b = x // 10 ** (n // 2), x % 10 ** (n // 2)
        c, d = y // 10 ** (n // 2), y % 10 ** (n // 2)

        ac = self.karatsuba(a, c, n // 2)
        bd = self.karatsuba(b, d, n // 2)
        adbc = self.karatsuba(a + b, c + d, n // 2) - ac - bd

        return 10**n * ac + 10 ** (n // 2) * adbc + bd


def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    n = len(str(x))
    print(Multiplication().rec_int_mult(x, y, n))
    print(Multiplication().karatsuba(x, y, n))
    print(x * y)

    x = 124
    y = 5678
    n = len(str(x))
    print(Multiplication().rec_int_mult(x, y, n))
    print(Multiplication().karatsuba(x, y, n))
    print(x * y)


if __name__ == "__main__":
    main()
