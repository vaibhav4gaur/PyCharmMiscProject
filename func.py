def add(i,j):
    return i + j

def call(i,j):
    return add(i,j)

def passed(i,j,fn):
    return fn(i,j)

res = passed(4,5,call)
print(res)

