a = [0,1,2,4,3]

# indexing
print(a[3])

# index
print(a.index(1))

# slice
print(a[1:3])

# append
a.append('6')
print(a)

# insert
a.insert(0,'7')
print(a)

# del
del a[1]
print(a)

# remove
a.remove('6')
print(a)

# pop
b = a.pop(0)
print(a)
print(b)

# sort
a.sort()
print(a)

# reverse
a.reverse()
print(a)

# count
print(a.count(2))

# clear
a.clear()
print(a)

# extend
a.extend([3,4])
print(a)