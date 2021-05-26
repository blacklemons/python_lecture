class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f'Cat(name = {self.name}, age = {self.age})'

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    
navi = Cat("navi",10)
nero = Cat("nero",5)

navi.set_age(20)
print(navi.get_age())

print(navi)
print(nero)