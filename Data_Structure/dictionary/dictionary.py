dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

# key , value
# key : can only be strings and numbers (can't list, tuple)

# add item
dic['email'] = 'dic@gmail.com'
print(dic)

dic[3] = '3'
print(dic)

# get value by key
print(dic.get('name'))
print(dic['name'])

## fail to get value by key
print(dic.get('tel'))   # return None
# print(dic['tel'])     # error

# change value by key
dic['name'] = 'pay'
print(dic)

# del
del dic[3]
print(dic)

# make key/value/item list
a = dic.keys()
b = dic.values()
c = dic.items()
print(a)
print(b)
print(c)

# check key (not value)
print('name' in dic)
print('1118' in dic)

# convert list to dictionary
## a : key , b : value
new_dict = dict(zip(a,b))
print(new_dict)
## a,b : item
new_dict = dict((a,b))
print(new_dict)


# iterate dictionary with 'for' loop
for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

for key, value in dic.items():
    print(f"key : {key}, value : {value}")

for i in dic:
    print(i)


# clear
dic.clear()
print(dic)