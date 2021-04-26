"""
# python is a protocol orientated lang
# every top-level function has a corresponding dunder method implemented

[ metaclass ]
===
* what?
A: metaclass is barely a counterpart concept of "System.Object" in C#;
similarly, all classes are derived from metaclass or type in Python;

* why to use?
A:  "BBC"(builtin.__build_class__); 
class Meta<Clsname>(type): __new__();  
__init_subclass__;

we may intercept the process of class construction in Python by using the three approaches above;

* how to use?
A: u have to understand how a class constructs in Python;

```Python

import dis

def _():
    class TS:
        def foo(self):
            return 'foo'


dis.dis(_)

# you could see the building process of class TS;

```

* NOTE:
in Python, class is a block of executable code;
which is totally different from class in C++, C#, Java etc;

it means just like function concept in Python, class is live after definition!
it does not lay down somewhere in memory after class definition in C++;

===

@ZL, 20210426

"""



