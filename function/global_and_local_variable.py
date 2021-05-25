def print_sum():
    global a,b
    a=100
    b=200
    result = a + b
    print(f"print_sum() 내부 : a = {a}, b = {b}, result = {result}")

a=10
b=20
result = a+b
print(f"print_sum() 이전 : a = {a}, b = {b}, result = {result}")

print_sum()
result = a+b
print(f"print_sum() 외부 : a = {a}, b = {b}, result = {result}")