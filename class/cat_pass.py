class Cat:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        
    def meow(self):
        print(f"내 이름은 {self.name}, 색깔은 {self.color}")
    
navi = Cat("navi","red")
mimi = Cat("mimi","gray")
nero = Cat("nero","black")

navi.meow()
mimi.meow()
nero.meow()

navi.color = 'gray'
print(navi.color)