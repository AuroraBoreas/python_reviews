#ifndef META_H_INCLUDED
#define META_H_INCLUDED

#define PI PI = 3.1415926;

#include <string>
#include <ctime>
#include <iomanip>
#include <sstream>
#include <iostream>

// function template;
template<class T>
T square(T x)
{
    return x * x;
}

class Time
{
private:
    short hour;
    short minute;
    short second;
public:
    // ctors; ctor delegation;
    Time(short h, short m, short s);
    // ctor helper
    bool setTime(short, short, short) const;
    void setTime(void);
    // dtors
    virtual ~Time(){};
    // getter
    short Hour(void) const;
    short Minute(void) const;
    short Second(void) const;
    // setter
    void Hour(short);
    void Minute(short);
    void Second(short);
    // repr
    std::string toString(void) const;
};

class Date
{
private:
    unsigned m_year;
    unsigned m_month;
    unsigned m_day;
public:
    // ctor
    Date(unsigned, unsigned, unsigned);
    // helper
    bool setDate(unsigned, unsigned, unsigned);
    void setDate(void);
    // dtor
    virtual ~Date(){};
    // getter
    unsigned Year(void) const;
    unsigned Month(void) const;
    unsigned Day(void) const;
    // setter
    void Year(unsigned);
    void Month(unsigned);
    void Day(unsigned);
    // other
    friend std::ostream& operator <<(std::ostream& os, const Date& d)
    {
        os << d.toString();
        return os;
    }

    std::string toString(void) const;

    bool isLeapYear(unsigned year) const;
};

class DateTime: public Date, public Time
{
private:
    unsigned year, month, day;
    short hour, minute, second;
public:
    // ctor
    DateTime(unsigned year, unsigned month, unsigned day,
             short hour, short minute, short second);
    // dtor
    ~DateTime() {};
    // getter: year, month, day; hour, minute, second;
    // implement or not?
    // can't we just inherit from base classes?

    // setter: year, month, day; hour, minute, second;
    // can't we just inherit from base classes?

    std::string toString(void) const;
};


#endif // META_H_INCLUDED
