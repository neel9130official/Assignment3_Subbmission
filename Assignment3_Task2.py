

n=int(input("Enter a number:"))

def sqrt_loop(n, tolerance=1e-10):
    if n < 0:
        return
    guess = n / 2.0
    while abs(guess * guess - n) > tolerance:
        guess = (guess + n / guess) / 2
    return guess
res=sqrt_loop(n)
print(res)

def natural_log(x, terms=100):
    if x <= 0:
        return "Undefined (log only for positive numbers)"
    n = (x - 1) / (x + 1)
    result = 0
    for i in range(terms):
        term = (2 * n ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return result

res2=natural_log(n)
print(res2)

def fact(n):
    if n<2:
        return 1
    else:
        return n*fact((n-1))
pi=3.14
def sine(degree, terms=10):
    x = degree * (pi / 180)
    result = 0
    for i in range(terms):
        sign = (-1) ** i
        term = sign * (x ** (2 * i + 1)) / fact(2 * i + 1)
        result += term
    return result

res3=sine(n)
print(res3)