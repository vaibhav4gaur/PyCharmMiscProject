# Iterator
'''list = [1,2,3,4,5]

iterator = iter(list)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator))

# GENERATOR
def fn():
    yield 1
    yield 2
    yield 3

values = fn()
print(values.__next__())
print(values.__next__())
print(next(values))

def squares():
    n = 1
    while n<=5:
        squares = n ** 2
        yield squares
        n = n + 1

values = squares()
for i in values:
    print(i)'''


















