x=[]
a=0
n = int(input('수를 입력하세요 : '))

for i in range(n):
    x.append(i+1)
    a+=i+1
    
print(x)
print(a)