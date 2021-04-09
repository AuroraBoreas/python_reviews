@"

PS is a dynamic language;

[variables]
----
* variable
    ** pattern: T N V
    ** initializer

* data types
    ** char
    ** short
    ** integer
    ** long

    ** float
    ** double
    
    ** byte
    ** boolean
    ** decimal

    ** string

* type conversion
    ** implicit
    ** explicit

* type traits
    ** GetType()
----

"@

# extended type system
$a1 = 42;
$a1.GetType();
# or
(42).GetType();

$a2 = "hello world!";
$a2.GetType();

$a3 = (1, 2, 3);
$a3.GetType();

# access object props, same concept in JS;
$user = @{};    # dict obj; 
$user.name = "ZL";
$user.name;

# string is immutable in ps
$str = "hello world";
# $str.Length = 7; # error out
# obj method
$str.Contains("hello"); # true

# array
$fruit = "apple", "orange";
$fruit[0];

# string object-level method
$name = "Zhang Liang";
$name.Contains("Liang");
$name.ToUpper();
$name.ToLower();