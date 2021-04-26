"# Python is a protocol orientated lang; \n# every top-level function has a corresponding dunder method implemented;" 

class API:
    def func1(self):
        print('func1')
    
    def func2(self):
        print('func2')
     
    def func3(self):
        print('func3')
     
    def __call__(self):
        print('control in obj')
        self.func1()
        yield
        print('control in obj')
        self.func2()
        yield
        print('control in obj')
        self.func3()

if __name__ == '__main__':
    api = API()
    for ap in api():
        print('control in main')
        ap