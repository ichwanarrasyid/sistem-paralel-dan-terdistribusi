class Person:
    name = " "
    age = 0

    def __init__ (self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def ChangeName(self, name):
        self.name = name

p = Person('didi',21)



print(p.getName())
print(p.getAge())


