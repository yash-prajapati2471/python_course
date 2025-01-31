#single_inheritence
# class yash:
#     def yash_method(self):
#         print("hello yash")
        
# class jay(yash):
#     def jay_method(self):
#         print("hello jay")
        
# obj = jay()
# obj.yash_method()
# obj.jay_method()



#multiple_inheritance
# class yash:
#     def yash_method(self):
#         print("hello yash")
        
# class jay:
#     def jay_method(self):
#         print("hello jay")
        
# class raj(yash,jay):
#     def raj_method(self):
#         print("hello raj")
        
# obj = raj()
# obj.yash_method()
# obj.jay_method()
# obj.raj_method()
    
    
#multi_level
# class yash:
#     def yash_method(self):
#         print("hello yash")
        
# class jay(yash):
#     def jay_method(self):
#         print("hello yash")
        
# class raj(jay):
#     def raj_method(self):
#         print("hello yash")
        
# obj = raj()
# obj.yash_method()
# obj.jay_method()
# obj.raj_method()


#Hierarchical Inheritance

class animal:
    def sparrow(self):
        print("hello sparrow")

class nikhil(animal):
    def dog(self):
        print("hello dog")

class cat(nikhil):
    def cat(self):
        print("hello cat")

obj1 = cat()
obj2 = nikhil()

obj1.sparrow()
obj1.dog()
obj1.cat()