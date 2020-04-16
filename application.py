def c(input):
    out = 0
    for i in range(4000):
        out += i * 7 * input
    return out


def b(input):
    out = 0
    for i in range(4000):
        out += i * 5 * input
    out += 5 * c(input)
    return out


def a(input):
    out = 0
    for i in range(8000):
        out += i * 3
    out += i * 3 * b(input)
    return out