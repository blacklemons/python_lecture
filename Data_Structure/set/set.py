s1 = set([1,2,3])
print(s1)

s2 = set("HELLO")
print(s2)

s3 = set([2,3,4])
print(s3)

# access item
print("H" in s2)

# convert to list
l1 = list(s1)
print(l1)

l2 = list(s2)
print(l2)

# add
## item
s2.add('A')
print(s2)
## set
s2.update(s3)
print(s2)

# remove
## remove
s2.remove('A')
print(s2)
## discard
s2.discard(2)
print(s2)
## pop
x = s2.pop()
print(x)
print(s2)

# convert to set from list
new_s1 = set(l1)
print(new_s1)

# len
print(len(s1))

# Intersection
print(s1&s3)
print(s1.intersection(s3))

# Difference
print(s1-s3)
print(s1.difference(s3))
print(s3-s1)
print(s3.difference(s1))

# union
print(s1|s3)
print(s1.union(s3))

# Symmetric difference
print(s1^s3)
print(s1.symmetric_difference(s3))