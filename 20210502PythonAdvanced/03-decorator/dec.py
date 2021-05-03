"#python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented" 

def display(func):
    def wrapper(*args, **kwargs):
        rv = func(*args, **kwargs)
        print(rv)
    return wrapper

def fibonacci(n: int)->int:
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)

def factorial(n: int)->int:
    return 1 if n < 2 else n * factorial(n-1)

@display
def my_fib(n: int)->int:
    return fibonacci(n)
    
@display
def my_fact(n: int)->int:
    return factorial(n)

if __name__ == '__main__':
    my_fib(5) # 8
    my_fact(5) # 120