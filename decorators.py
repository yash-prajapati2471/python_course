def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Good Night")
    return mfx

@greet
def hello():
    print("my name is yash")

@greet
def add(a,b):
    print(a+b)

hello()
add(1,2)
