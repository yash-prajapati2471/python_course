from abc import ABC,abstractmethod

class car(ABC):
    def show(self):
        print("hello show")

    @abstractmethod
    def yash(self):
        pass

class maruti(car):
    def yash(self):
        print("hello yash")

class bmw(car):
    def yash(self):
        print("hello jay")

obj1 = maruti()
obj1.show()
obj1.yash()

obj2 = bmw()
obj2.show()
obj2.yash()



    