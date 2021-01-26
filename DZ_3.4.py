def x_pow (x, y):
    return x ** y
print(x_pow(2, 8))


def y_pow(a, n):
    res = 1
    for i in range(abs(n)):
       res *= a
    if n >= 0:
       return res
    else:
      return 1 / res
print(y_pow(2, 9))



