using System;
using System.Collections.Generic;
using System.Text;
using System.Threading;
using System.Threading.Task;

using MyTypes;
using CarLibrary;

namespace CSharpReview
{

    public class Program
    {
        public static void Main(string[] args)
        {
            VariableDemo();
            FunctionDemo();
            
            StatementDemo();
            ControlflowDemo();

            LoopDemo();
            ClassDemo();

            ContainerDemo();
            FileIODemo();

            ThreadingDemo();
            AsyncDemo();

            System.Console.WriteLine("Press any key to continue..");
            Console.ReadLine();
        }

        private static void VariableDemo()
        {
            /*
            
            [variable]
            ----
            * concept;
                ** box
                ** pattern: T N V

            * declare and define;
                ** late binding
                ** early binding

            * keywords;
                ** default
                ** var
                ** new
                ** dynamic
                ** record
                ** ref
                ** out
                ** in

            * constraints;
                ** const
                ** static
            ----


            [data types]
            ----
            * C S I L, F D, B B D;
                ** see Types.drawio, linnk to "C#\Types.drawio"
            
            * type traits;
                ** System.Reflection

            * type conversion;
                ** implicit, explicit
                ** downcasting, upcasting
                ** cast operators: dynamic_cast<T>() static_cast<T>() const_cast<T>() reinterpreter_cast<T>()
                ** type conversion operator overloading

            * user-defined types;
                ** enum
                ** struct

                ** class
                ** delegate
                ** dynamic
                ** record

            * "boxed" and "unbox" concept;
                ** "boxed": stack -> heap
                ** "unboxed": heap -> stack, type checking is a MUST --> this is why "unbox" is slow

            ----
            */

            checked // or unchecked overflow / underflow;
            {
                char c = 'c';
                short s = 12;
                int i = 42;
                long l = 1234567890L;

                float f = 2.718f;
                double d = 3.1415926000231;

                byte b = 255;
                bool bo = true;
                decimal de = 6.718m;

                Console.WriteLine(c.ToString());
                Console.WriteLine(s.ToString("C2"));
                Console.WriteLine(i.ToString("C2"));
                Console.WriteLine(l.ToString("E"));

                Console.WriteLine(f.ToString("F2"));
                Console.WriteLine(d.ToString("G"));

                Console.WriteLine(b.ToString("N"));
                Console.WriteLine(bo.ToString());
                Console.WriteLine(de.ToString("C3"));
            }

            // discrete math
            double f1 = 0.2;
            double f2 = 0.1;
            Console.WriteLine(f1 + f2);

            decimal d1 = new decimal(0.2);
            decimal d2 = new decimal(0.1);
            Console.WriteLine(d1 + d2);

            var v1 = 6.718m;
            Console.WriteLine(v1);

            // default
            float f3 = default;
            float f4 = default;
            Console.WriteLine(f3);
            Console.WriteLine(f4);

            // dynamic
            dynamic x = 3.14f;
            x = 6.718;
            x = "hello world!";
            Console.WriteLine(x);

            // record: concept is similar to "namedtuple" in Python;
            public record Stuff(string Name, string Sex, int Age)
            {
                System.Console.WriteLine("\nName: {0}\nSex: {1}\nAge: {2}", Name, Sex, Age);
            }

            Stuff[] people = new Stuff[]{
                new Stuff("ZL", "male", 35),
                new Stuff("ZZ", "female", 32),
                new Stuff("LL", "female", 30),
                new Stuff("MM", "female", 31),
            };

            foreach(var stuff in people)
                System.Console.WriteLine(p);

            // in, out, ref
            int a;
            InitializeNumberA(a);
            System.Console.WriteLine(a); // 42
            DisplayNumberA(a); // 42
            ChangeNumberA(ref a);
            System.Console.WriteLine(a); // 100

            // enum
            System.Console.WriteLine(Colors.red);

            // struct
            Point p1 = Point(3, 4), p2 = Point(4, 5);
            System.Console.WriteLine(p1.ToString());
            System.Console.WriteLine(p2.ToString());
            
            // class
            Person pe1 = new Person("ZL", "male", 35);
            System.Console.WriteLine(pe1.ToString());
            
            // delegate
            CarV1 myCar = new CarV1("ZL", 200, 20, "red");
            EventHandler<CarEngineEventArgs> d = new EventHandler<CarEngineEventArgs>(SendMessage);
            myCar.CarEngineHandler += d;

            for(int i=0; i<10; ++i)
                myCar.Accelerate(20);
           

            /*
            
            [string]
            ----
            * basic;
                ** length
                ** substring, replace, split, copy
                ** capitalize, uppercase, lowercase
                ** standard numeric formatting: C D E F G N P X
                ** interpolation
            
            * System.Text.StringBuild;
                ** append

            * regex;

            ----
            */ 

            string myStr1 = "Fugiat laboris laborum nostrud aute ex ea aute ut cillum esse est.";
            System.Console.WriteLine(myStr1.length);
            System.Console.WriteLine(myStr1[1]);
            System.Console.WriteLine(myStr1.SubString(1, 2));

            // StringBuilder
            StringBuilder sb = new StringBuilder();
            sb.Append("Hello");
            sb.Append("World");
            sb.Append("ZL");
            sb.Append("Dominate!");
            System.Console.WriteLine(sb.ToString());

        }
        
        static void FunctionDemo()
        {
            /*
            
            [function]
            ----

            * concept;
                ** a block of reusable code
                ** "black box"

            * pattern: T N P;
                ** return_type, function_name, parameters
                ** yeah, function is other "type"

            * keywords;
                ** in, out, ref;
                ** params;
                ** return, yield;
                ** await, async;
                ** abstract, virtual, sealed, override, new;

            * overloading;
                ** public
                ** class methods
                    *** using indexer to overload subscript operators []

            * category;
                ** anonymouse function;
                ** lambda expression;
                ** function pointer;
            
            * generic function;
                ** Action<>;
                ** Func<>;
                ** Predict<>;

            *             
            ----
            
            */ 
            InitializeNumberA(int x);
            System.Console.WriteLine(x);
            ChangeNumberA(ref x);
            System.Console.WriteLine(x);
            DisplayNumberA(x);
            
        }

        static void StatementDemo()
        {
            /*
            
            [statement]
            ----

            * concept;
                ** it is similar with "instructions" in real life;
            
            * patter;
                ** var operates object to get results;

            * operators;
                ** Arithmetic: + - * / %; ++(prefix) --(prefix); ++(postfix) --(postfix); += -= *= /* %=
                ** Relational: == !=; < <=; > >=;
                ** Logical: ! && ||
                ** Access: . [];
                ** Bitwise: << >> & | ^ ~;
                ** Assignment: =, ();
                ** Cast: (T)var; is; as;
                ** Operator for storage: new
                ** Operator for other: () {}
            
            ----
            */ 
            
            // arithmetic
            int x = 42, y =12;
            System.Console.WriteLine($"x = {x}, y = {y}, x + y = {x + y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x - y = {x - y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x * y = {x * y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x / y = {x / y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x % y = {x % y}");

            // relational
            System.Console.WriteLine($"x = {x}, y = {y}, x == y : {x == y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x != y : {x != y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x > y : {x > y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x >= y : {x >= y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x < y : {x < y}");
            System.Console.WriteLine($"x = {x}, y = {y}, x <= y : {x <= y}");

            // logical
            System.Console.WriteLine($"x = {x}, !x : {!x}");
            System.Console.WriteLine($"x = {x}, x = {y}, x && y : {x && y}");
            System.Console.WriteLine($"x = {x}, x = {y}, x || y : {x || y}");

            // access
            System.Console.WriteLine(string.Format($"x = {x}, y = {y}"));
            
            // bitwise; using Convert.ToString(var, bits);
            System.Console.WriteLine($"x = {x}, binary form in 8-bit system: {Convert.ToString(x, 2)}");
            System.Console.WriteLine($"y = {y}, binary form in 8-bit system: {Convert.ToString(y, 2)}");
            x = 42; x << 2;
            System.Console.WriteLine($"x << 2: {x}");
            x = 42; x >> 2;
            System.Console.WriteLine($"x >> 2: {x}");
            System.Console.WriteLine($"~ x: {~x}");
            x = 42;
            System.Console.WriteLine($"x & y: {x & y}");
            System.Console.WriteLine($"x | y: {x | y}");
            System.Console.WriteLine($"x ^ y: {x ^ y}");

            // assign
            // cast, C-style type conversion

            // nullable, as, is, null

            // operator for storage, new
            // operator for other, ternary

        }

        static void ControlflowDemo()
        {
            /*
            
            [controlflow]
            ----
            * if...else if...else...
            * switch...case...default...
                ** pattern matching in C# >= 8.0

            * try...catch...finally...
            ----
            
            */
            IfelseDemo(69);
            SwitchcaseDemo(42);
            TrycatchDemo(10, 0); 
        }

        static void LoopDemo()
        {
            /*
            
            [loop]
            ----
            * for
            * foreach
            * while
            * do...while
            ----

            
            */
            
            List<Person> people = new List<Person>{
                new Person("ZL", "male", 34),
                new Person("ZZ", "female", 35),
                new Person("LL", "female", 30),
                new Person("MM", "male", 28),
                new Person("NN", "male", 24),
            };

            // for loop
            for(int i=0; i<people.count; ++i)
                System.Console.WriteLine(people[i].ToString());

            // foreach
            foreach(Person p in people)
                System.Console.WriteLine(p.ToString());

            // while
            int i = 0;
            while(true)
            {
                if(i<people.count)
                {
                    System.Console.WriteLine(people[i]);
                    i++;
                }
                else
                    break;
            }

            // do...while
            i = people.count;
            do
            {
                --i;
                System.Console.WriteLine(people[i].ToString());
            } while(i > 0); 
        }

        static void ClassDemo()
        {
            /*
            
            [class]
            ----
            * concept: a model that simulates a concept in real life; it is a block of code which groups hard-coupled data members and methods together;
            
            * A E I P
                ** abstraction
                ** encapsulation
                ** inheritance
                ** polymorphism
            
            * S O L I D
                ** single responsibility principle
                ** open-close principle
                ** lovski substitution principle
                ** interface segregation principle
                ** dependency inverse principle

            * keywords
                ** abstract
                ** virtual
                ** override
                ** new
                ** set
                ** get
                ** sealed

                ** readonly

                ** static

                ** private            
                ** public
                ** protect
                ** internal

            ----
            
            */ 

            // see class Car in Car.cs
            SportsCarCollection coll = new SportsCarCollection(10);
            foreach(var c in coll)
            {
                if(c is SportsCar sc)
                {
                    System.Console.WriteLine(c.ToString());
                }
            }
            
        }

        static void ContainerDemo()
        {
            // seq: array, list, vector, forward_list
            // adapter: stack, dequeue, queue
            // associative: map, multimap, set, multiset
            // I C A M L O B P;
            
            // ! warning: do NOT use ArrayList containers in System.Collections;
            // ? due to box and unbox operations btwn stack and heap, they are not efficient;
            
            // Array; fixed capacity
            Person[] people = new Person[] {
                new Person("ZL", "male", 35),
                new Person("ZZ", "female", 34),
                new Person("LL", "male", 33)    
            };

            System.Console.WriteLine(people.length);
            System.Console.WriteLine(people[^1]);

            // List; flexible capacity
            List<SportsCar> spcars = new List<SportsCar> {
                new SportsCar("ZL", 111, "red", 120),
                new SportsCar("ZZ", 311, "green", 180),
                new SportsCar("LL", 211, "blue", 150),
                new SportsCar("MM", 112, "yellow", 220),
            };

            var myCars = 
                from spcar in spcars
                where spcar.MaxSpeed >= 150
                orderby spcar.Number
                select spcar;
            
            foreach(var myCar in myCars)
                System.Console.WriteLine(myCar.ToString());

            // dictionary; k-v
            Dictionary<int, string> dict1 = new Dictionary<int, string>();
            dict1.Add(1, "hello");
            dict1.Add(2, "world");
            dict1.Add(3, "Zhang");
            dict1.Add(4, "Liang");
            
            foreach(KeyValuePair<int, string> kv in dict1)
            {
                System.Console.WriteLine($"key={kv.Key}, val={kv.Val}");
            }

            // HashSet; uniqueness
            HashSet<Point> points = new HashSet<Point>{
                Point(3, 4),
                Point(4, 5),
                Point(5, 6),
                Point(7, 8),
                Point(9, 10),
            };
            
            foreach(Point p in points)
                System.Console.WriteLine(p.ToString());

        }

        static void FileIODemo()
        {
            /*
            
            [SystemIO, FS]
            ----
            * Drive

            * Directory, DirectoryInfo

            * File, FileInfo

            * Path

            ----

            [System.IO, WriterReader]
            ----
            * BinaryReader, BinaryWriter
            
            * StreamReader, StreamWriter
            
            * StringReader, StringWriter
            
            * TextReader, TextWriter

            ----
            
            */

            // using IStreamer, OStreamer
            // see /draw/SystemIO.drawio for details
            string path = @"";
            (using StreamWriter sw = new StreamWriter(path))
            {
                // do some stuff;
            }

            (using StreamReader sr = new StreamReader(path))
            {
                // do errands;
            }

        }

        static void ThreadingDemo()
        {
            /*
            
            [Threading]
            ----
            * concept: concurrency

            * how
                * Thread
                * ThreadPool
                * TPL

            ----

            */ 
            Task.Factory.StartNew((1, 10, 1000)=>{
                VeryImportantWork();
            });

            Task.Factory.StartNew((2, 5, 1500)=>{
                VeryImportantWork();
            });

            Task.Factory.StartNew((3, 8, 3000)=>{
                VeryImportantWork();
            });
            
            System.Console.WriteLine(CurrentThread.Name);
        }

        static void AsyncDemo()
        {
            /*
            
            [Asynchronous]
            ----
            * concept: chess master in 12 hours; 
            * how:
                ** async, await;

            ----
            
            */ 
            static async Task Main(string[] args)
            {
                System.Console.WriteLine("Async demo=>");
                List<int> myList = default;

                // return_value is using Task<T>
                string msg = await DoWorkAsync();
                System.Console.WriteLine(msg);
                // or call async methods in non-async methods
                System.Console.WriteLine(DoWorkAsync().Result);    

                // return_value is void, using Task
                await DoAnotherWorkAsync();

                // multiawaits;
                await MultiAwaits();

                System.Console.WriteLine("Completed");
            }

            static async Task<string> DoWorkAsync()
            {
                return await Task.Run(()=>{
                    Thread.Sleep(5_000);
                    return "Done with work!"
                });
            }

            static async Task DoAnotherWorkAsync()
            {
                await Task.Run(()=>{
                    Thread.Sleep(4_000);
                    System.Console.WriteLine("Void method completed");
                });
            }

            static async Task MultiAwaits()
            {
                await Task.Run(()=>{ Thread.Sleep(2_000); });
                System.Console.WriteLine("Do with first task!");
                
                await Task.Run(()=>{ Thread.Sleep(3_000); });
                System.Console.WriteLine("Do with second task!");
                
                await Task.Run(()=>{ Thread.Sleep(4_000); });
                System.Console.WriteLine("Do with third task!");
            }

        }

        static void VeryImportantWork(int i, int n, int time)
        {
            System.Console.WriteLine($"Worker{i} starts");
            for(int j=0; j < n; ++j)
            {
                Thread.Sleep(time);
                System.Console.WriteLine($"worker{i} is working");
            }
            System.Console.WriteLine($"Worker{i} done");
        }

        static void InitializeNumberA(out int n)
        { n = 42; }

        static void DisplayNumberA(in int n)
        { System.Console.WriteLine(n); } // n can NOT be changed in this context

        static void ChangeNumberA(ref int n)
        { n = 100; }

        static void SendMessage(object sender, CarEngineEventArgs e)
        {
            if(sender is CarV1 c)
            {

                System.Console.WriteLine(c.CurrentSpeed);
                System.Console.WriteLine(e.Info);
            }
            else
                throw new ArgumentException("sender is not a CarV1 type");
        }

        static void IfelseDemo(int x)
        {
            if(x % 2 == 1)
            {
                System.Console.WriteLine($"{x} is odd");
            }
            else if(x % 3 == 1)
            {
                System.Console.WriteLine($"{x} is foo");
            }
            else if(x % 5 == 1)
                System.Console.WriteLine($"{x} is buz");
            else
                System.Console.WriteLine("unknown");
        }

        static void SwitchcaseDemo(int x)
        {
            switch(x)
            {
                case x % 2 == 1:
                    System.Console.WriteLine($"{x} is odd");
                default:
                    System.Console.WriteLine($"{x} may be even");
            }
        }

        static void TrycatchDemo(int x, int y)
        {
            try
            {
                System.Console.WriteLine(x / y);
            }
            catch (System.Exception ex)
            {
                System.Console.WriteLine(ex.Message);
            }
            finally
            {
                throw new Exception("u messed up");
            }
        }




    }
    
}