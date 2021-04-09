#ifndef CPP_REVIEW_H
#define CPP_REVIEW_H

#include <iostream>
#include <sstring>
#include <string>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <stdexcept>
#include <exception>
#include <list>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <memory>

namespace ZLSpace
{
    void variable_notation(void);
    void function_notation(void);
    void statement_notation(void);
    void controlflow_notation(void);
    void loop_notation(void);
    void class_notation(void);
    void container_notation(void);
    void fileio_notation(void);

    int add(int x, int y)
    { return x + y; }

    int add(const int x, const int y, const int z)
    { return x + y + z; }

    int sub(const int& x, const int& y)
    { return x - y; }

    int fibonacci(int n)
    { return (n < 2)? 1: fibonacci(n-1) + fibonacci(n-2); }

    int factorial(int n)
    { return (n < 2)? 1: n * factorial(n-1); }

    inline void addone(int* p1)
    { *p1 +=1; }

    inline void addone(int& _ref)
    { _ref = _ref + 1; }

    template<class T, class U>
    void display(T arg1, U arg2)
    { std::cout << arg1 << ", " << arg2 << std::endl; }

    typedef void (*func_ptr)(char* s);

    inline void msg(char* s)
    { std::cout << s << std::endl; }

    struct Point
    {
        private:
            int m_x, m_y;
        public:
            // ctors
            Point(int x, int y)
            { m_x = x; m_y = y; }
            // dstor
            ~Point(){}
            // getter
            int X(void) const { return m_x; }
            int Y(void) const { return m_y; }
            // setter
            void X(int val) { m_x = val; }
            void Y(int val) { m_y = val; }
            // repr
            std::string ToString(void) const
            {
                std::stringstream ss;
                ss << "[" << m_x << ", " << m_y << "]";
                return ss.str();
            }
    }

    inline bool IsLeapYear(int year)
    { return (year%4 == 0 && year%100 != 0) || (year%400 == 0); }

    class Date
    {
        private:
            unsigned m_year, m_month, m_day;
        public:
            // ctors
            Date(){ m_year=0; m_month=0; m_day=0; }
            Date(unsigned year, unsigned month, unsigned day)
            {
                // check?
                if(!SetDate(year, month, day))
                {
                    m_year = m_month = m_day = 0;
                }
                this->m_year = year;
                this->m_month = month;
                this->m_day = day;

            }
            // helper
            bool SetDate(unsigned y, unsigned m, unsigned d)
            {
                if(m > 12) return false;
                if(d > 31) return false;
                switch(m)
                {
                    case 2: if(IsLeapYear(y))
                            {
                                if(m > 29) return false;
                            }
                            else
                            {
                                if(m > 28) return false;
                            }
                            break;
                    case 4:
                    case 6:
                    case 9:
                    case 11: if(m>30) return false;
                }
                return true;
            }
            void SetDate(void)
            {
                struct tm *tm;
                time_t sec; std::time(&sec);
                tm = std::localtime(&sec);

                this->m_year = tm->tm_year + 1900;
                this->m_month = tm->tm_mon + 1;
                this->m_day = tm->tm_mday;
            }
            // dtor
            ~Date(){}
            // getter
            unsigned Year(void) const { return m_year; }
            unsigned Month(void) const { return m_month; }
            unsigned Day(void) const { return m_day; }
            // setter
            void Year(unsigned val) { m_year = val; }
            void Month(unsigned val) { m_month = val; }
            void Day(unsigned val) { m_day = val; }
            // ToString
            std::string ToString(void) const
            {
                std::stringstream ss;
                ss << std::setfill('0') << std::setw(4) << m_year << "-"
                << std::setfill('0') << std::setw(2) << m_month << "-"
                << std::setfill('0') << std::setw(2) << m_day;
                return ss.str();
            }

    };

    inline int division(int x, int y)
    {
        if(y == 0)
            throw std::invalid_argument("denominator can NOT be zero!");
        return x / y;
    }

    inline void trycatch_demo()
    {
        int x = 42, y = 0;
        try
        {
            division(x, y);
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
        }
    }

    class Parcel
    {
        private:
            unsigned prio;
            std::string info;
        public:
            Parcel(const std::string& s, unsigned p)
            { info = s; prio = p; }
            unsigned Priority(void) const
            { return prio; }
            bool operator<(const Parcel& p)
            { return (this->prio < p.Priority()); }
            std::string ToString(void) const
            { 
                std::stringstream ss;
                ss << "priority: " << prio << ", info: " << info;
                return ss.str();
            }
    }


    void variable_notatino(void)
    {
        /*
        [variable]
        ----
        syntax: T N V
        ----
        
        [data types]
        ----
        * Char
        * Short
        * Int
        * Long

        * Float
        * Double
        ----

        [type traits]
        ----
        isxxx?
        ----

        [type conversion]
        ----
        * downcasting
        * upcasting
        ----

        [constraints]
        ----
        * const
        ----

        [storage modifier]
        ----
        * static
        * extern
        * register
        * auto
        ----

        */ 

    char c = 'a';
    short s = 12;
    int i = 32;
    long l = 3213L;
    float f = 3.14F;
    double d = 2.718281828;
    long double ld = 1.99999999999999999999999999901;
    
    std::cout << c << std::endl;

    auto x = 42;
    std::cout << x << std::endl;

        // type conversion
        std::cout << std::stoi("42") << std::endl;

        // address
        int y = 12;
        std::cout << "memory address of y : " << &y << std::endl;
        // alias
        int& ya = y;
        // pointer
        int* ptry = &y;
        std::cout << "memory address of y: " << ptry << std::endl;
        // rvalue vs lvalure;
        // rvalue reference vs lvalye reference;
        // std::move(); unconditional;
        // std::forward();  conditionaly, perfect forwarding;

    }

    void function_notation(void)
    {
        /*
        
        [function]
        ----
        * overloading, function signatures(types of args, quantities of args);
        * passing args by val or ref or pointer
        * function pointer
        * function template
        * prototype declaration, definition
        * inline definition vs macro
        * lambda expr
        * keywords: static, const, friend, inline,
        ----
        

        */ 
        
        // overloading
        std::cout << add(1, 2) << std::endl;    // 3
        std::cout << add(1, 2, 3) << std::endl; // 6
        // recursion, tail recursion
        std::cout << fibonacci(3) << std::endl; // 3
        std::cout << factorial(5) << std::endl; // 120
        // passing args by val or ref or pointer
        int x = 42,
            *ptr = &x;

        addone(&x);
        std::cout << x << std::endl; // 43
        addone(x);
        std::cout << x << std::endl; // 44
        // passing an array as arg, the array will be degraded into pointer;   
        // function template
        display<int, double>(x, 3.14); 
        display<std::string, floa>("hello world", 2.718f);
        // function pointer
        char s[] = "hello world";
        func_ptr fp = msg;
        msg(s);
        
        // lambda expr;
        func_ptr another_fp = [](char* s)->void {
            std::cout << s << std::endl;
        }
        another_fp(s);

    }

    void statement_notation(void)
    {
        /*
        
        [operators]
        ----
        * Arithmetic
        * Relational
        * Logic
        * Access
        * Bitwise
        * Assign
        * Cast
        * Operator for storage
        * Operator for other
        ----
        */ 

        // arithmetic
        int x = 24, y = 12;
        std::cout << "x = " << x << ", y = " << y << " x + y = " << x + y << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x - y = " << x - y << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x * y = " << x * y << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x / y = " << x / y << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x % y = " << x % y << std::endl;
        
        // relational
        std::cout << "x = " << x << ", y = " << y << " x == y : " << (x == y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x != y : " << (x != y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x < y : " << (x < y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x <= y : " << (x <= y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x > y : " << (x > y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x >= y : " << (x >= y) << std::endl;

        // logic
        std::cout << "x = " << x << ", y = " << y << " x >= y : " << (!x) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x >= y : " << (x && y) << std::endl;
        std::cout << "x = " << x << ", y = " << y << " x >= y : " << (x || y) << std::endl;

        // access
        Point* p1 = new Point(3, 4);
        std::cout << (*p1).ToString() << std::endl;
        std::cout << p1->ToString() << std::endl;
        delete p1;

        // bitwise
        std::cout << "x = " << x << ", in binary: " << std::bitset<8>(x) << std::endl;
        std::cout << "y = " << y << ", in binary: " << std::bitset<8>(y) << std::endl;
        std::cout << " x & y: " << std::bitset<8>(x) & std::bitset<8>(y) << std::endl;
        std::cout << " x & y: " << std::bitset<8>(x) | std::bitset<8>(y) << std::endl;
        std::cout << " x & y: " << std::bitset<8>(x) ^ std::bitset<8>(y) << std::endl;
        std::cout << " x & y: " << ~ std::bitset<8>(x) << std::endl;

        // assign { =, regular ctor, uniform initializer, initializer_list(), }
        Point *p2 = new Point(3, 4);
        Point *p3 = new Point{3, 4};
        delete p2; delete p3;

        // cast { static_cast, const_cast, dynamic_cast, reinterpret_cast }
        // relate with OO Polymorphism;

        // Op for storage
        // see code above

        // Op for other
        // ternary, "." etc., 

    }

    void controlflow_notation(void)
    {
        /*
        
        [control flow]
        ----

        * if...else if...else; ternary operator(?:)
        * switch...case...default
        * try...catch...finally

        ----    
        */

    // decision tree
    // see class Date
    
        Date *d1 = new Date(2021, 2, 22);
        std::cout << d1->ToString() << std::endl;

        delete d1;

        // try...catch...
        trycatch_demo();
    }

    void loop_notation(void)
    {
        /*
        [loop]
        ----
        * for loop
        * while loop
        * do...while;
        * foreach
        ----
        
        */ 
        
        int numbers[] = { 1, 2, 3 };

        // for
        for(int i=0; i<3; ++i)
            std::cout << numbers[i] << " ";
        std::cout << std::endl;

        // foreach
        for(auto i : numbers)
            std::cout << i << " " << std::endl;
        std::cout << std::endl;

        // for { address, index, pointer }
        // { address }
        std::cout << std::endl;
        for(int i=0; i<3; ++i)
        std::cout << (numbers + i) << ", " << *(numbers + i) << std::endl;

        // { index }
        std::cout << std::endl;
        for(int i=0; i<3; ++i)
            std::cout << &numbers[i] << ", " << numbers[i] << std::endl;

        // { pointer }
        std::cout << std::endl;
        int *ptr = numbers;
        for(int i=0; i<3; ++i)
        {
            if(ptr==nullptr)
                break;
            std::cout << ptr << ", " << *ptr << std::endl;
            ptr++;
        }
    }

    void class_notation(void)
    {
        /*
        
        + pillars: A E I P
            - abstraction: coupled viriables and methods are bounded together, work together
            - encapsulation: private, public, protect
            - inheritance: MRO; Left-Right; TopDown;
            - Polymorphism: same behaviors of subclasses have different results or forms
        
        + principles: S O L I D
            - Single Responsibility principle: coupling or decoupling vars and methods;
            - Open close principle: always be aware that open and close props, methods, and classes;
            - Lovski substitute principle: base class can subtitutes subclass;
            - Interface segregation principle: coupling aor decoupling interfaces
            - Dependency inversion principle: high-level dependency relies on high-level dependency; low-level dependency relies on low-level dependency;
        
        + structures:
            - auto-generated methods:
                < C++11
                - default ctor
                - default dtor
                - default copy ctor
                - default copy assignment operator
                
                >= C++11
                - default move copy ctor
                - default move copy assignment operator
            
            - constraints
                >= C++11
                - "default" kw
                - "delete" kw
                - "override" kw
                - "final" kw
                - "virtual" kw
                - "=0"

        */ 

       // see class Date
       Date *d1 = new Date(2021, 2, 23);
       std::cout << d1->ToString() << std::endl;
       delete d1;
    }

    void container_notation(void)
    {
        /*
        
        + containers:
            ++ sequence
            - array, fixed capacity, contains elements with a homegeneous type;
            - list, non-fixed capacity, contains elements with a homegenous type;
            - queue,
            - vector,
            - forward list,

            ++ adapater
            - dequeu    e
            - stack
            - PriorityQue

            ++ 
            - map
            - multimap
            - set
            - multiset
        
        + algorithms
            - Iterator, const_iterator
            - Capacity
            - Access
            - Modifier
            - List operation
            - Observer
            - Bucket
            - Policy
        
        */ 
        typedef std::list<int> INTList;
        typedef std::vector<double> DblVec;

        // vector, list
        {
            INTList intlist = { 1, 2, 3, 4, 5 };
            INTList::iterator it;
            for(it = intlist.begin(); it!=intlist.end(); ++it)
                std::cout << *it << std::endl;

            DblVec dv = { 1.1, 2.718, 3.14, 12.0 };
            DblVec::const_iterator cit;
            for(cit = dv.begin(); cit!=dv.end(); ++cit)
                std::cout << *cit << std::endl;

        }
        // queue
        {
            std::queue<Parcel> q1;
            q1.push(Parcel{"ZL", 3});
            q1.push(Parcel{"CY", 6});
            q1.push(Parcel("LL", 8));
            q1.push(Parcel("ZZ", 2));

            while(!q1.empty())
            {
                std::cout << q1.front().ToString() << std::endl;
                q1.pop();
            }
        }
    }

    class PersonV0
    {
        private:
            std::string FirstName;
            std::string LastName;
        public:
            // ctor
            PersonV0(const std::string& fName, const std::string& lName)
            : FirstName(fName), LastName(lName)
            {}
            // dtor
            ~Personv0(){}
            // getter
            std::string FirstName(void) const { return FirstName; }
            std::string LastName(void) const { return LastName; }
            // setter
            void FirstName(const std::string& value) { FirstName = value; }
            void LastName(const std::string& value) { LastName = value; }
            // repr
            std::string ToString(void) const
            {
                std::stringstream ss;
                ss << FirstName << LastName;
                return ss.str();
            }
    }

    class PersonV1
    {
        private:
            struct Pimpl;
            std::unique_ptr<Pimpl> pimpl;
        public:
            // ctor
            PersonV1(const std::string& fName, const std::string& lName);
            PersonV1(const PersonV1& rhs);
            PersonV1& operator=(PersonV1 rhs);
            // dtor
            ~PersonV1(){}
            // getter
            std::string FirstName(void) const;
            std::string LastName(void) const;
            // setter
            void FirstName(const std::string& val);
            void LastName(const std::string& val);
            // repr
            std::string ToString(void) const;
    };

    struct PersonV1::Pimpl
    {
        std::string FirstName, LastName;
        public:
            Pimpl(const std::string& fName, const std::string& lName)
            : FirstName(fName), LastName(lName){}
    };

    PersonV1::PersonV1(const std::string& fName, const std::string& lName)
    : pimpl(new Pimpl(fName, lName)){}

    PersonV1::PersonV1(const PersonV1& rhs)
    : pimpl(new Pimpl(*rhs.pimpl)){}

    PersonV1& PersonV1::operator=(PersonV1 rhs)
    {
        std::swap(pimpl, rhs.pimpl);
        return *this;
    }

    std::string PersonV1::FirstName(void) const
    { return pimpl->FirstName; }
    std::string PersonV1::LastName(void) const
    { return pimpl->LastName; }

    void PersonV1::FirstName(const std::string& val)
    { pimpl->FirstName = val; }
    void PersonV1::LastName(const std::string& val)
    { pimpl->LastName = val; }

    std::string PersonV1::ToString(void) const
    { return pimpl->FirstName + " " + pimpl->LastName; }
} // namespace ZLSpace



#endif