class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
p1=Person("Shruthi",19)
print(p1.name)
print(p1._Person__age)

