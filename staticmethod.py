class Math:
    def __init__(self,num):
        self.num = num

    @staticmethod
    def add(a,b):
        return a+b
    
print(Math.add(1,5))