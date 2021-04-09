#include <iostream>
#include <cctype>
#include <cstdlib>

#include "meta.h"

using std::cout;

// function pointer;
void message(const char*), message_error(const char*),
    message_upper(const char*), message_lower(const char*),
    (*func_ptr[])(const char*) = { message, message_error, message_upper, message_lower };


int main()
{
    cout << "Hello world!" << std::endl;
    cout << "\n";

    // function template
    {
        cout << square<char>(42) << std::endl;
        cout << square<int>(3) << std::endl;
        cout << square<short>(69) << std::endl;
        cout << square<long>(128) << std::endl;
        cout << square<float>(3.14) << std::endl;
        cout << square<double>(2.718281828) << std::endl;
        cout << "\n";
    }

    // class Time
    {
        Time t1 = Time(8, 30, 15);
        cout << t1.toString() << std::endl;
    }

    // class Date
    {
        Date d1 = Date(2021, 4, 5);
        cout << d1 << std::endl;

        Date d2 = Date(0, 1, 1);
        cout << d1 << std::endl;
        d2.setDate();
        cout << d1 << std::endl;

        // function pointer
        char hello[] = "\nchoose "
                       "an integer between(0-3)";
        char msg[] = "Hello World! Welcome Zhang Liang";
        char err[] = "index out of range!";

        int index;
        cout << hello << std::endl;

        while(std::cin>>index)
        {
            if(index<=3 && index >= 0)
            {
                (*func_ptr[index])(msg);
            }
            else
            {
                (*func_ptr[1])(err);
                break;
            }
            cout << hello << std::endl;
        }
    }
    // variable
    {
        /*

        [ variable ]
        ---
        * concept: box
        * feature:
            ** pattern: T N V
            ** primitive types: C S I L, F D, L D; B B D;
            ** type conversion:
                *** upcasting/downcasting;
                *** implicit/explicit;
                *** operator overloading;

            ** type traits: reflection
            ** variable template
         ---

        */

        char a = 'a';
        short b = 128;
        int x = 69;
        long y = 42;

        float c = 3.1415926f;
        double d = 3e8;

        long double e = 2.718281828219123012391;

        bool x1 = bool(0);

        std::cout << a << std::endl;
    }

    // function
    {
        /*

        [ function ]
        ---
        * concept: black box
        * patter: T N P

        * feature:
            ** function inside function
            ** function template
            ** return_type is value, pointer, reference;
            ** function name -> overloading
            ** parameters are passing ByVal, ByRef, Pointer; ParamArray;

        * category:
            ** regular
            ** anonymous
            ** lambda
            ** immediate
            ** generator?
            ** iterator?
        ---

        */
    }

    // statement
    {
        /*

        [ statement ]
        ---
        * concept: link
        * pattern: symbols
        * feature:
            ** expression vs statement
            ** explicit and implicit

        * category:
            ** Arithmetic
            ** Rational
            ** Logical
            ** Access
            ** Bitwise
            ** Assign
            ** Cast
            ** Operator for storage
            ** Operator for other
        ---

        */

    }

    // controlflow
    {
        /*

        [ controlflow ]
        ---
        * concept: flow
        * pattern: branch or option
        * feature:
            ** if...else if...else
            ** switch...case...default
            ** try...catch...finally

        * category:
            ** shorthand?
            **
        ---

        */
    }

    // loop
    {

        /*

        [ loop ]
        ---
        * concept: circle
        * pattern: circle
        * feature:
            ** for(;;;)
            ** foreach(:)
            ** while
            ** do...while

        ---

        */
    }

    // class
    {
        /*

        [ class ]
        ---
        * concept: simulator
        * pattern: simulator
        * feature:
            ** Abstract
            ** Encapsulation
            ** Inheritance
            ** Polymorphism

            ** Single responsibility principle
            ** Open and close principle
            ** Lovski substitution principle
            ** Interface isolation principle
            ** Dependency inversion principle

        * keyword:
            ** class vs struct(litter difference in C++, big difference in C#)
            ** =0 -> abstract;
            ** virtual -> vtable -> polymorphism;
            ** override -> explicitly override virtual methods;
            ** explicit -> explicitly overload operator;
            ** default -> ctor
            ** delete -> ctor

        ---

        */
    }

    // container
    {
        /*

        [ data structure ]
        ---
        * concept: container
        * pattern: container
        * feature:
            ** separate container with its algorithm;
            ** iterator
            ** const_iterator
            ** capacity
            ** access
            ** modifier
            ** list observation
            ** bucket
            ** hash policy

        * category:
            ** seq
                *** array   -> bidirectional iterator
                *** list    -> bidirectional iterator
                *** forward_list -> forwarding only iterator
                *** dequeue -> bidirectional iterator

            ** adapter
                *** queue
                *** stack
                *** heap

            ** associative
                *** map
                *** multimap
                *** set
                *** multiset
        ---


        */
    }

    // io
    {
        /*

        [ io ]
        ---
        * concept: input and output
        * pattern: in and out
        * feature:
            ** file io
            ** stream io
            ** buffer io

        ---

        */
    }

    return 0;
}

// functions
void message(const char* s)
{ std::cout << s << std::endl; }

void message_error(const char* s)
{ std::cerr << s << std::endl; }

void message_upper(const char* s)
{
    char tmp;
    for(; *s != '\0'; s++)
    { tmp = std::toupper(*s); std::cout.put(tmp); }

    std::cout << std::endl;
}

void message_lower(const char* s)
{
    char tmp;
    for(; *s != '\0'; ++s)
    { tmp = std::tolower(*s); std::cout.put(tmp); }

    std::cout << std::endl;
}

