class A():
    def M1(self):
        print("PRINT M1 from A")

class B(A):
    def M2(self):
        print("PRINT M2 from B")

class C(A):
    def M3(self):
        print("PRINT M3 from C")

class D(B,C):
    def M4(self):
        print("PRINT M4 from B and C")

class E(B):
    def M5(self):
        print("PRINT M5 from B")

class F(E):
    def M6(self):
        print("PRINT M6 from E")

print(D.mro())









