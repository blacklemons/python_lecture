def plus(*args):
    y='y = '
    for i in args:
        if type(i) == int:
            x = str(i)
            y = y + x
    return y

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

print(plus(a,b,c))