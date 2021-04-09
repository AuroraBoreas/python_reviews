const cls = require("./classes.JS");

function VariableDmo() {
    /*
    
    [Variables]
    ----
    * declaration and definition
        ** pattern: T N V
        ** default value? "undefined"

    * keywords
        ** var
        ** let
        ** const

    * data types
        ** Undefined
        ** Null
        ** String
        ** Number
        ** Integer
        ** Decimal
        ** function
        ** class
        ** symbol
    
    * type conversion
        ** Boolean()
        ** Number()
        ** String()

        ** Number.parseFloat()
        ** Number.parseInt()

    * reflection
        ** IsNaN()
        ** Typeof
    ----

    */ 
    
    var a = 42;
    let b = 69;
    const c = 3.14;
    var bo = true;
    var nu = null;

    console.log(a, typeof a, isNaN(a));
    console.log(b, typeof b, isNaN(b));
    console.log(c, typeof c, isNaN(c));    
    console.log(bo, typeof bo, isNaN(bo));    
    console.log(nu, typeof nu, isNaN(nu));    

    
    // type conversion; by default node JS converts all numbers to strings;
    console.log(String(a));
    console.log(String(b));
    console.log(String(a));

    console.log(Number.parseInt('69'));
    console.log(Number.parseFloat('6.718'));

}

function FunctionDemo() {
    /*
    
    [functions]
    ----
    * concept: a block of reusable code that with output w/o output;
    * structure
        ** return_type
            ** ref
            ** array
            ** val

        ** function name
            ** overloading

        ** args
            *** byRef: class object etc
            *** byVal: numbers, string, boolean
            *** param array

    * category
        ** regular functions
        ** anonymouse functions
        ** lambda expr
        ** function inside function
        ** immediate functions
        ** generator

    ----
    
    */ 

    // regular
    function Add(x, y){
        return x + y;
    }
    console.log(Add(3, 4)); // 7

    // param array ...
    function SUM(...args){
        let sum = 0;
        for(let i=0; i<args.length; ++i)
            sum += args[i]
        return sum;
    }
    console.log(SUM(1, 2, 3));    

    // anonymouse
    const f = function(){
        console.log("anonymouse function says hello");
    }
    f();

    // lambda
    const g = (a, b) => {
        return a * b;
    }
    console.log(g(3, 4)); // 12

    // immediate
    ((a, b, c)=>{
        console.log(a, b, c);
    })(1, 2, 3); // 1, 2, 3   

    // generator
    const f1 = function*(){
        yield 1;
        yield 2;
        yield 3;
    }
    let myF1 = f1();
    console.log(myF1.next());
    console.log(myF1.next());
    console.log(myF1.next());

    function* f2(n){
        yield n;
        yield n + 1;
        yield n + 2;
    }
    let mf2 = f2(10);
    console.log(mf2.next());
    console.log(mf2.next());
    console.log(mf2.next());

}

function StatementDemo() {
    /*
    
    [statement]
    ----
    * operators
        ** A R L A B A C O O
    ----
    
    */ 

    // arithmetic
    let x = 42, y = 69;
    console.log(`x = ${x}, y = ${y}, x + y = ${x + y}`);
    console.log(`x = ${x}, y = ${y}, x - y = ${x - y}`);
    console.log(`x = ${x}, y = ${y}, x * y = ${x * y}`);
    console.log(`x = ${x}, y = ${y}, x / y = ${x / y}`);
    console.log(`x = ${x}, y = ${y}, x % y = ${x % y}`);
    // relational
    console.log(`x = ${x}, y = ${y}, x == y : ${x == y}`);
    console.log(`x = ${x}, y = ${y}, x != y : ${x != y}`);
    console.log(`x = ${x}, y = ${y}, x < y : ${x < y}`);
    console.log(`x = ${x}, y = ${y}, x <= y : ${x <= y}`);
    console.log(`x = ${x}, y = ${y}, x > y : ${x > y}`);
    console.log(`x = ${x}, y = ${y}, x >= y : ${x >= y}`);
    // logic
    console.log(`x = ${x}, y = ${y}, x && y : ${x && y}`);
    console.log(`x = ${x}, y = ${y}, x || y : ${x || y}`);
    console.log(`x = ${x}, y = ${y}, !y : ${!y}`);
    // access
    const numbers = [1, 2, 3];
    console.log(numebrs.length);
    // bitwise
    console.log(`x = ${x}, y = ${y}, x & y : ${x & y}`);
    console.log(`x = ${x}, y = ${y}, x | y : ${x | y}`);
    console.log(`x = ${x}, y = ${y}, x ^ y : ${x ^ y}`);
    console.log(`x = ${x}, ~x : ${~x}`);
    x = x << 2;
    console.log(`x = ${x}, x << 2 : ${x}`);
    y = y >> 2;
    console.log(`y = ${y}, y << 2 : ${y}`);
    // assign
    let a = Number(3.14);
    console.log(a);
    let b = Boolean(true);
    console.log(b);
    let c = String("hello ZL");
    console.log(c);
    let d = 1.618;
    console.log(d);
    // cast: N/A
    
    // operator for storage
    var p1 = new cls.Point(3, 4);
    var p2 = new cls.Point(6, 8);

    console.log(p1.K(p2));  // 2
    delete p1.X;
    
    // operator for other
    var rect1 = lib.Rectangle(3, 4);
    var circ1 = lib.Circle(3.5);

    let res = (rect1.Area() > circ1.Area())? "rectangle": "circle";
    console.log(res);
}

function ControlflowDemo() {
    /*
    
    [control flow]
    ----
    * if...else if...else
    * switch case default
    * try...catch...finally--
    
    */

    class MDate
    {
        // field
        _year;
        _month;
        _day;
        // ctor
        constructor(year=1, month=1, day=1){
            if(!this.SetDate(year, month, day))
            { _year = _month = _day = 1; }

            this._year = year;
            this._month = month;
            this._day = day;
        }
        // helper
        IsLeapYear(year){
            return (year%4 == 0 && year%400 != 0)||(year%400 == 0);
        }

        SetDate(year, month, day) {
            if(year < 0) { return false; }
            if(month < 0 || month > 12) { return false; }
            if(day < 0 || day > 31) { return false; }
            switch(month)
            {
                case 2: if(this.IsLeapYear(year))
                        {
                            if(day > 29) { return false; }
                        }
                        else
                        {
                            if(day > 28) { return false; }
                        }
                        break;
                case 4:
                case 6:
                case 9:
                case 11: if(day > 30) { return false; }
            }

            return true;
        }
        // getter
        get Year()  { return this._year; }
        get Month() { return this._month; }
        get Day()   { return this._day; }
        // setter
        set Year(val) { this._year = val; }
        set Month(val){ this._month = val; }
        set Day(val)  { this._day = val; }
        // methods
        ToString(){ return `${this.Year}-${this.Month}-${this.Day}`; }
        // comparison
        Gt(other){
            if(this.Year != other.Yera)
            { return this.Year > other.Year; }
            else if(this.Month != other.Month)
            { return this.Month > other.Month; }
            else
            { return this.Day > other.Day; }
        }
        
        Equal(other){
            return (this.Year == other.Year && this.Month == other.Month && this.Day == other.Day);
        }
        
        SetToday(){
            let today = new Date();
            this._year = today.getFullYear();
            this._month = today.getMonth();
            this._day = today.getDay();
        }

        static Delta(val){
            try {
                throw new Error("error out"); 
            } catch (error) {
                console.log(error);
            } finally
            {
                console.log(val);
            }            
        }
    }

    let d1 = new MDate();
    d1.SetToday();
    let d2 = new MDate();
    console.log(d1.Equal(d2));
    MDate.Delta(100);
}

function LoopDemo() {
    /*
    
    [Loop]
    ----
    * for
    * for...of
    * for...in
    * forEach
    * while
    * do...while
    ----
    */ 

    var numbers = [1, 2, 3, 4];
    var dates = [
        new MD(),
        new MD(2020, 1, 12),
        new MD(2019, 3, 31),
    ];

    for(let i=0; i<numbers.length; ++i)
    {
        console.log(i);
    }

    for(let i of dates)
    {
        console.log(i.ToString());
    }

    for(let i in numbers)
    {
        console.log(i);
    }

    let i = 0;
    while(i < dates.length)
    {
        console.log(dates[i].ToString());
    }

    i = 0;
    do {
        console.log(dates[i].ToString());
    } while (i < dates.length);

}

function ClassDemo() {
    /*
    
    [class]
    ----
    * concept: a group of hard-coupling data members and methods;
    * keywords
        ** "class"
        ** "static"
        ** "extends"
        ** "constructor"
    * pillars:
        ** Abstraction
        ** Encapsulation
        ** Inheritance
        ** Polymorphism
    ----
    
    */
    var shapes = [
        new lib.Rectangle(3, 4),
        new lib.Circle(3.5),
        new lib.Rectangle(4, 5),
        new lib.Rectangle(6, 7),
        new lib.Circle(4),
    ];

    for(let shape in shapes)
    {
        console.log(typeof(shape), shape.Area());
    }
}

function ContainerDemo() {
    /*
    
    [containers]
    ----
    * seq:
        ** array

    * ada:
        ** queue
        ** stack
        ** dequeue

    * ass:
        ** set
        ** map 
    ----
    
    */ 

    // array
    var integers = new Array(1, 2, 3);
    console.log(integers.length);

    // set
    // union, intersection, difference, symmetricdifference;
    // implements
    
    function union(set1, set2){
        let _tmp = new Set(set1);
        for(let i of set2)
        {
            if(!set1.has(i))
            {
                _tmp.add(i);
            }
        }
        
        return _tmp;
    }
    
    function difference(set1, set2){
        let _tmp = new Set(set1);
        for(let i of set2)
        {
            if(set1.has(i))
            {
                _tmp.delete(i);
            }
        }
        
        return _tmp;
    }
    
    function symmentricDifference(set1, set2){
        let _tmp = new Set(set1);
        for(let i of set2)
        {
            if(set1.has(i))
            {
                _tmp.delete(i);
            }
            else
            {
                _tmp.add(i);
            }
        }
        
        return _tmp;
    }
    
    function intersection(set1, set2){
        let _tmp = new Set();
        for(let i of set2)
        {
            if(set1.has(i))
            {
                _tmp.add(i);
            }
        }
        
        return _tmp;
    }
    
    var set1 = new Set([1, 2, 3, 4, 5]);
    var set2 = new Set([4, 5, 6, 7, 8]);
    console.log(set1.size, set2.size);

    console.log(union(set1, set2)); // {1, 2, 3, 4, 5, 6, 7, 8};
    console.log(difference(set1, set2)); // {1, 2, 3};
    console.log(symmentricDifference(set1, set2)); // {1, 2, 3, 6, 7, 8};
    console.log(intersection(set1, set2));  // {4, 5}

    // map
    var m1 = new Map();
    m1.set(1, "apple");
    m1.set(2, "orange");
    m1.set(3, "pearl");

    m1.forEach((item)=>{
        console.log(item);
    });
    
}

exports.VariableDmo = VariableDmo;
exports.FunctionDemo = FunctionDemo;
exports.StatementDemo = StatementDemo;
exports.ControlflowDemo = ControlflowDemo;
exports.LoopDemo = LoopDemo;
exports.ClassDemo = ClassDemo;
exports.ContainerDemo = ContainerDemo;
