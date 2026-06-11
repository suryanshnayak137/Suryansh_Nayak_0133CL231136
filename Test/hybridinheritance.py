class Father:
    def property(self):
        print("Father: I own property")
    def business(self):
        print("Father: I run a business")

class Son(Father):
    def study(self):
        print("Son: I love to study")
class Daughter(Father):
    def dance(self):
        print("Daughter: I love to dance")
class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild: I love gaming")

gc = GrandChild()
gc.property()
gc.business()
gc.study()
gc.dance()
gc.gaming()