a = lambda x: x+1
print(a(1))


q = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x % 2 == 0), q))
print(b)


w = list(map(lambda x: x + 1, q))
print(w)
