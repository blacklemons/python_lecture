t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# delete element
## del t2[0] # error

# change element
## t2[0] = 3 # error

# indexing
print(t3[1])

# slice
print(t4[:2])

# extend
## +
print(t4+t5)
## *
print(t3*2)

# len
print(len(t5))