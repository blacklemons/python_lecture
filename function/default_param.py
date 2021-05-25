def print_sign(a=1,b=2,c=3):
    for i in range(a):
        print("!!!")
    for i in range(b):
        print("@@@")
    for i in range(c):
        print("###")
    print("")

print_sign()
print_sign(2)
print_sign(b=1)
print_sign(2,c=0,b=2)

# print_sign(2,b=0,2) # error

# positional argument can't follows keyword argument
# so align positional arguments before keyword arguments