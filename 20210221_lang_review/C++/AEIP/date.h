#ifndef DATE_H_INCLUDED
#define DATE_H_INCLUDED

#include <iostream>
#include <string>

//inline bool IsLeapYear(int year)
//{
//    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
//}

struct Date
{
private:
    int m_year, m_month, m_day;

public:
    // ctor
    Date(int year=1, int month=1, int day=1);
    // dtor
    ~Date(){}
    // getter
    int Year(void) const;
    int Month(void) const;
    int Day(void) const;
    // setter
    void Year(int val);
    void Month(int val);
    void Day(int val);

    // methods
    bool SetDate(int year, int month, int day) const;
    void SetDate(void);

    // ToString()
    std::string ToString(void) const;
    friend std::ostream& operator<<(std::ostream& os, const Date& d)
    {
        os << d.ToString();
        return os;
    }

    static bool IsLeapYear(int year);
};




#endif // DATE_H_INCLUDED
