from src.lib import Foo
import timeit

def client_code() -> None:
    f: Foo = Foo(5)
    f.bar()
    print(f.add(7))
    x = f.add(2)
    print(type(x))
    del f
    
def dll_performance() -> None:
    res: float = timeit.timeit(stmt='Sum(range(1000))', setup='from src.lib import Sum', number=1000)
    print(res)

def main() -> None:
    client_code()
    dll_performance()

if __name__ == '__main__':
    main()