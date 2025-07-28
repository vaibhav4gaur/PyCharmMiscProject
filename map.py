'''def squares(a):
    return a ** 2
numbers = [1,2,3,4,5]'''

ans = list(map(lambda a : a ** 2, range(5)))
print(ans)

'''def squares_1(a):
    return a**2
numbers_1 = [1,2,3,4,5]'''

ans_1 = set(filter(lambda a : a ** 2, range(6)))
print(ans_1)