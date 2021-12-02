def myfun(w):
    return lambda a:a/w
x=myfun(4)
y=myfun(5)

print(x(10))
print(y(12))