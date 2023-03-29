class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def introduce(self):   
        print(f"안녕하세요, 저는  {self.name}이고, 나이는 {self.age}입니다. 제 키는 {self.height}입니다.")
    
    def yell(self):
        print("아?")

class Developer(Person):
    keyboard = "기계식"

    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def yell(self):
        print("어?")
    
developer = Developer("임소현", 24, 163)
developer.introduce()
developer.yell()

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease

designer = Designer("임소현", 24, 163, "N")
designer.introduce()
designer.yell()

class ProductManager(Person):
    def __init__(self, name, age, height):
        super().__init__(name, age, height)
    
    def yell(self):
        print("개발자님 여기 오류있어요")
    
    def aging(self):
        self.age += 2
        self.height -= 5
        print("개발자를 새로 뽑아야 하나...")
        Developer.keyboard = "멤브레인"
    
productManager = ProductManager("임소현", 24, 163)
productManager.introduce()
productManager.yell()
productManager.aging()
productManager.introduce()


