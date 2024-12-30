class Car:
    def __init__(self,id,name):
        self.id= id
        self.name = name

    def show(self):
        print(self.id)
        print(self.name)

Obj1 = Car('10101','BMW')
Obj1.show()
