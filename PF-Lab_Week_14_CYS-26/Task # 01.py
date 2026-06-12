def num_square(n):
    return n*n
print(num_square(3))

a = lambda x: x * x
print(a(3))

add = lambda a, b: a + b
print(add(5, 3))

a = [1, 2, 3, 4]
result = list(map(lambda x: x * x, a))
print(result)