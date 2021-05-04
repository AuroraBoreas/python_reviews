
const cls = require('myclass.js');

function variableDemo() {
    /*
    [ variable ]
    ===
    * concept: box
    * pattern: T N V
    * feature:
        ? primitive types: CSIL, FD, BBD
        ? type limits: overflow, underflow
        ? type traits: typeof, isXXX
        ? type conversion: implicit and explicit; downcasting and upcasting
        ? initializatino: late or early binding;
        ? variable template
        
        ? storage: static, const, auto, register
    ===
    */ 

    // declaration and initializtion
    var x1 = 69;
    let x2 = true;
    const pi = 3.14;

    // type traits
    console.log(`x1: ${x1}, type : ${typeof x1}`);
    console.log(`x2: ${x2}, type : ${typeof x2}`);
    console.log(`pi: ${pi}, type : ${typeof pi}`);

    // type conversion
    x1 = Number(42);
    x2 = String(x2);
    let x3 = Boolean(1);

    // parse
    let r1 = parseFloat(String(3.1415));
    let r2 = parseInt(String(69));
    console.log(`r1: ${r1}`);
    console.log(`r2: ${r2}`);
    
    return null;
}

function functionDemo() {
    /*
    [ function ]
    ===
    * concept: blackbox
    * pattern: T N P
    * feature:
        ? function inside function
        ? class inside function
        ? decorator
        ? generator

        ? function template
        ? function pointer
        
        ? regular function
        ? anonymous function
        ? lambda
        ? immediate function
        
        ? return_type: ByVal, ByRef, ByPtr
        ? args_type: ByVal, ByRef, ByPtr
    ===
    */ 

    function fibonacci(n) {
        return n < 2? 1 : fibonacci(n-1) + fibonacci(n-2);
    }

    function factorial(n) {
        return n < 2? 1 : n * factorial(n-1);
    }

    const f1 = function(x) {
        return x * x;
    }

    const f2 = (x, y)=>{
        return x * x + y * y;
    }

    (function(x) {
        console.log(x);
    })(69);

    function* gen(n) {
        yield n;
        yield n + 1;
        yield n + 2;
    } 

    var g1 = gen(10);
    console.log(g1.next());
    console.log(g1.next());
    console.log(g1.next());

    function LovePerson() {
        class Person {
            constructor(name, age, sex) {
                this.name = name;
                this.age = age;
                this.sex = sex;
            }

            ToString() {
                return `\nName: ${this.name}\nAge: ${this.age}\nSex: ${this.sex}`;
            }
        }

        return new Person("ZL", "35", "male");
    }

    let rv = LovePerson();
    console.log(rv.ToString());
}

function statementDemo() {
    /*
    [ statement ]
    ===
    * concept: relation
    * pattern: link / symbol
    * feature:
        ? Arithmetic:
            - unary
            - binary
        ? Relational:
            - ==
            - >
            - <
        ? Logical:
            - !
            - &&
            - ||
        ? Access
            - .
            - ->
        ? Bitwise
            - <<, >>
            - ~
            - &
            - |
            - ^
        ? Assign:
            - =
            - {}
            - ()
        ? Cast
            - dynamic_cast<T*>(U*);
            - static_cast<T*>(U*);
            - const_cast<T*>(U*);
            - reinterpret_cast<T*>(U*);
        ? Op for storage:
            - new
            - delete
        ? Op for other
            - ternary: ?:, (), {}
    ===
    */
    
    let x = 42, y = 69;

    // A
    console.log(`x: ${x}, y: ${y}, x + y : ${x + y}`);
    console.log(`x: ${x}, y: ${y}, x - y : ${x - y}`);
    console.log(`x: ${x}, y: ${y}, x * y : ${x * y}`);
    console.log(`x: ${x}, y: ${y}, x / y : ${x / y}`);
    console.log(`x: ${x}, y: ${y}, x % y : ${x % y}`);
    
    // R
    console.log(`x: ${x}, y: ${y}, x == y : ${x == y}`);
    console.log(`x: ${x}, y: ${y}, x != y : ${x != y}`);
    console.log(`x: ${x}, y: ${y}, x < y : ${x < y}`);
    console.log(`x: ${x}, y: ${y}, x <= y : ${x <= y}`);
    console.log(`x: ${x}, y: ${y}, x > y : ${x > y}`);
    console.log(`x: ${x}, y: ${y}, x >= y : ${x >= y}`);
    
    // L
    console.log(`x: ${x}, y: ${y}, !x : ${!x}`);
    console.log(`x: ${x}, y: ${y}, x && y : ${x && y}`);
    console.log(`x: ${x}, y: ${y}, x || y : ${x || y}`);
    
    // A
    console.log(`pi: ${Math.PI}`);
    
    // B
    console.log(`x: ${x}, ~x : ${~x}`);
    x = 42; x <<= 2;
    console.log(`x: ${x}, x << 2 : ${x}`);
    x = 42; x >>= 2;
    console.log(`x: ${x}, x >> 2 : ${x}`);
    x = 42; y = 69;
    console.log(`x: ${x}, y: ${y}, x & y : ${x & y}`);
    console.log(`x: ${x}, y: ${y}, x | y : ${x | y}`);
    console.log(`x: ${x}, y: ${y}, x ^ y : ${x ^ y}`);

    // A
    x = Number(42);
    console.log(`x: ${x}`);

    // [x] Cast

    // Op for storage
    var d1 = new Date();
    console.log(`d1: ${d1.toUTCString()}`);
    delete d1;

    // Op for other
    var s = x % 2 == 1? "odd" : "even";
    console.log(`x: ${s}`);

    return null;
}

function controlflow() {
    /*
    [ controlflow ]
    ===
    * concept: flow
    * pattern: flow
    * feature:
        ? if...else if...else;
        ? switch...case...default;
        ? try...catch...finally;
    ===
    */ 
    let rnd = new cls.Random(1, 10);
    
    if(rnd % 2 == 0) {
        console.log(`value: ${rnd} is an even integer`);
    }
    else {
        console.log(`value: ${rnd} is an odd integer`);
    }

    function IsLeapYear(year) {
        return (year%4 == 0 && year%100 != 0) || (year%400 == 0);
    }

    function setDate(y, m, d) {
        if (y < 1) { return false; }
        if (m < 1 || m > 12) { return false; }
        if (d < 1 || d > 31) { return false; }
        
        switch (m) {
            case 2: if(IsLeapYear(y)) {
                        if(d > 29) { return false; }
                    }
                    else {
                        if(d > 28) { return false; }
                    }
                    break;
            case 4:
            case 6:
            case 9:
            case 11: if(d > 31) { return false; }            
        }

        return true;
    }

    console.log(setDate(2021, 12, 30)); // true

    return null;
}

function loopDemo() {
    /*
    [ loop ]
    ===
    * concept: loop
    * pattern: loop
    * feature:
        ? for(;;)
        ? foreach: for( in ), for( of );
        ? while
        ? do...while
    ===
    */

    var numbers = [ 1, 2, 3 ];
    
    for(let i=0; i < numbers.length; ++i) {
        console.log(`numbers[${i}]: ${numbers[i]}`);
    }

    for(let elem of numbers) {
        console.log(elem);
    }

    // u got amazed by the result? :^)
    for(let elem in numbers) {
        console.log(elem);
    }

    let i = 0;
    while(i < numbers.length) {
        console.log(`numbers[${i}]: ${numbers[i]}`);
        i++;
    }

    i = numbers.length - 1;
    do {
        console.log(`numbers[${i}]: ${numbers[i]}`);
        --i;
    } while (i > 0);

    return null;
}

function classDemo() {
    /*
    
    [ class ]
    ===
    * concept: simulator
    * pattern: simulator
    * feature:
        ? Abstract
        ? Encapsulation
        ? Inheritance
        ? Polymorphism

        ? SRP
        ? OCP
        ? LSP
        ? ISP
        ? DIP
        ? Delimiter(least known principle)

        ? accessibility: public, private, extern, friend
        ? components:
            ?? ctor

            ?? default ctor
            ?? dtor
            ?? copy ctor
            ?? copy assignment ctor
            ?? move ctor
            ?? move assignment ctor 
    ===    
    */
    
    let rect = new lib.Rectangle(3, 4);
    console.log(rect.ToString(), rect.circumference(), rect.area());
    delete rect;

    let circ = new lib.Circle(4);
    console.log(circ.ToString(), circ.circumference(), rect.area());
    delete circ;

    return null;
}

function ioDemo() {
    const FS = require('fs');
    let data = "hello ZL!";
    // write
    FS.writeFile('demo.txt', data, (error)=>{ if(error) { throw err; } });
    // read
    FS.readFile('demo.txt', (error, text)=>{
        if(error) { throw err; }
        console.log(text.ToString());
    });

    return null;
}

function datastructureDemo() {
    /*
    [ datastructure ]
    ===
    * concept: container
    * pattern: container
    * feature:
        ? seq:
            ?? array
            ?? list
            ?? forward_list
            ?? dequeue
        ? adapter:
            ?? stack
            ?? priority_queue
            ?? queue
        ? associative:
            ?? map
            ?? multimap
            ?? set
            ?? multiset

    ===
    */ 
    
    // array or list
    var numbers = [ 1, 2, 3 ];
    let rv = numbers.filter((n)=>{ return n%2 == 1; });
    console.log(rv); // [1, 3];

    numbers.shift(1);
    console.log(numbers);

    numbers.push(4);
    console.log(numbers);

    // dict
    var obj = {
        'name' : 'ZL',
        'age'  : 35,
        'sex'  : 'male'
    };

    console.log(obj.name);
    
    // HashMap
    var m1 = new Map();
    m1.set(1, "ZL");
    m1.set(2, 'TS');
    m1.set(3, "SCY");
    console.log(m1);
    delete m1;

    // set
    var s1 = new Set([1, 2, 3, 1]);
    s1.forEach((elem)=>{
        console.log(elem * 2);
    })

    return null;
}

function algorithmDemo() {
    /*
    [ algorithm ]
    ===
    * concept: calculation
    * pattern: calculation
    * feature:
        ? iterator and const_iterator
            ?? forward only iterator
            ?? bidirection iterator
            ?? input iterator
            ?? output iterator

        ? capacity
        ? access
        ? modification
        ? list observation
        ? bucket
        ? hash policy
    ===    
    */ 

    function intersection(s1, s2) {
        let tmp = new Set();
        for(let elem of s2) {
            if (s1.has(elem)) {
                tmp.add(elem);
            }
        }
        return tmp;
    }

    function union(s1, s2) {
        let tmp = new Set(s1);
        for(let elem of s2) {
            if(!s1.has(elem)) {
                tmp.add(elem);
            }
        }
        return tmp;
    }

    function difference(s1, s2) {
        let tmp = new Set(s1);
        for(let elem of s2) {
            if(s1.has(elem)) {
                tmp.delete(elem);
            }
        }
        return tmp;
    }

    function symmetricDifference(s1, s2) {
        let tmp = new Set(s1);
        for(let elem of s2) {
            if(s1.has(elem)) {
                tmp.delete(elem);
            }
            else {
                tmp.add(elem);
            }
        }
        return tmp;
    }

    var s1 = new Set([ 1, 2, 3, 4, 5 ]);
    var s2 = new Set([ 4, 5, 6, 7, 8 ]);

    console.log(intersection(s1, s2));
    console.log(difference(s1, s2));
    console.log(symmetricDifference(s1, s2));
    console.log(union(s1, s2));


    return null;
}


exports.variableDemo = variableDemo;
exports.functionDemo = functionDemo;
exports.statementDemo = statementDemo;
exports.controlflow = controlflow;
exports.loopDemo = loopDemo;
exports.classDemo = classDemo;
exports.ioDemo = ioDemo;
exports.datastructureDemo = datastructureDemo;
exports.algorithmDemo = algorithmDemo;
