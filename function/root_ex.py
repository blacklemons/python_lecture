def root_ex(a,b,c):
    x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    return x1, x2

a =  int(input('이차항의 계수 : '))
b =  int(input('일차항의 계수 : '))
c =  int(input('상수 : '))

x , y = root_ex(a,b,c)

print(f"해는 {x}, {y} 이다.\n타입은 {type(x)}, {type(y)} 이다.")