def greet1(name):
    print(f'안녕하세요 {name} 씨')

greet1('홍길동')

def greet(*args):
    for name in args:
        print(f'안녕하세요 {name} 씨')

greet('james','이순신')