#method overloading

class Demo:
    def show(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("No arguments")
