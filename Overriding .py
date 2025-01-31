class a:
    def disp(self):
        print("this is parent class")

class b(a):
    def disp(self):
        super().disp()
        print("this is child class")

obj = b()
obj.disp()