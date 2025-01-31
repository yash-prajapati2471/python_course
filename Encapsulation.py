class a:
    _a = 10 #private 
    __b = 20 #protected

    def yash(self):
        print("a",self._a)
        print("b",self.__b)

obj = a()
obj.yash()