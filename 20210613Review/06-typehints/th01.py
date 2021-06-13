"""
@ what
type hints are one instinct feature in static lang: C/C++, C#, Java, Swift etc;

@ why
function annotation is important.
it relieves the pain of using user-defined funtions in compile time; 

* less confusion;
* expressive;

@ how
using the builtin *typing* module; 

- first impression
    ~ just mimic builtin / primitive types:
        $ CSIL
        $ FD
        $ BBD

    ~ collections: 
        $ tuple
        $ list
        $ dict
        $ set

    ~ user-defined types:
        $ class
        $ struct
        $ enum
        $ union

    ~ library:
        $ sqlite3.Cursor etc

- mimic
    ~ type alias

- style
    ~ mimic class, capitalized

@ZL, 20210613

"""

# mimic builtin types
def greeting(name: str)->str:
    return "hello " + name

# type alias
Url = str
def retry(url: Url, retry_count: int)->None:
    pass

from typing import Any, Type, TypeVar, Iterable, Tuple

# combo
T      = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inner_product(v: Vector[T])->T:
    return sum(x * y for x, y in v)

def dialate(v: Iterable[Tuple[T, T]], scale: T)->Iterable[Tuple[T, T]]:
    return ((x * scale, y * scale) for x, y in v)

from typing import Callable

# passing function
def feeder(get_next_item: Callable[[str], str])->None:
    pass

def async_query(on_success: Callable[[int], None], on_error: Callable[[int, Exception], None])->None:
    pass

# passing function w/o specifying list of args using eclipse literal ...
def partial(func: Callable[..., str], *args)->Callable[..., str]:
    pass

# generic
from typing import Mapping, Set

class Employee: pass

def notify_by_email(employees: Set[Employee], overrides: Mapping[str, str])->None:
    ...

from typing import TypeVar, Sequence
T = TypeVar('T')

def first(l: Sequence[T])->T:
    return l[0]

from typing import Text
AnyStr = TypeVar('AnyStr', Text, bytes)
def concat(x: AnyStr, y: AnyStr)->AnyStr:
    return x + y

class MyStr(str): ...
x = concat(MyStr('apple'), MyStr('pie'));

# or using Any as an alternative
from typing import Any, List
def count_truthy(elements: List[Any])->int:
    return sum(1 for e in elements if e)

# each type variable args to Generic must be distinct.
from typing import TypeVar, Generic
U = TypeVar('U')
class Pair(Generic[U, U]): ... # ! invalid

if __name__ == "__main__":
    feeder(greeting)
