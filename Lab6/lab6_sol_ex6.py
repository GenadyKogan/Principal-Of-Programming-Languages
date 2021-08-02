def compose(f, g):
    return lambda x: f(g(x))

def incr(x):
    return x+1


def square(x):
    return x ** 2


def repeated(f, n):
    def f_after_repeat(x):
        if n == 1:
            return f(x)
        y = f
        for i in range(n - 1):
            y = compose(f, y)
        return y(x)
    return f_after_repeat


print(repeated(incr, 4)(2))
print(repeated(square, 2)(5))
