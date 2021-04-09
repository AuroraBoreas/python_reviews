#include "date.h"

#include <ctime>
#include <sstream>
#include <iomanip>

bool Date::IsLeapYear(int year)
{
    return (year%4 == 0 && year%100 != 0) || (year%400 == 0);
}

bool Date::SetDate(int year, int month, int day) const
{
    if(year < 0 ) return false;
    if(month < 0 || month > 12) return false;
    if(day <0 || day > 31) return false;

    switch(month)
    {
        case 2: if(IsLeapYear(year))
                {
                    if(day > 29) return false;
                }
                else
                {
                    if(day > 28) return false;
                }
                break;
        case 4:
        case 6:
        case 9:
        case 11: if(day > 30)
                 {
                     return false;
                 }
    }

    return true;
}

Date::Date(int year, int month, int day)
{
    if(!SetDate(year, month, day))
        m_year = m_month = m_day = 1;

    m_year = year;
    m_month = month;
    m_day = day;
}

int Date::Year(void) const
{ return m_year; }
int Date::Month(void) const
{ return m_month; }
int Date::Day(void) const
{ return m_day; }

void Date::Year(int val)
{ m_year = val; }
void Date::Month(int val)
{ m_month = val; }
void Date::Day(int val)
{ m_day = val; }

void Date::SetDate(void)
{
    struct tm *tm;
    time_t sec; std::time(&sec);
    tm = std::localtime(&sec);

    m_year = tm->tm_year + 1900;
    m_month = tm->tm_mon + 1;
    m_day = tm->tm_mday;
}

std::string Date::ToString(void) const
{
    std::stringstream ss;
    ss << std::setw(4) << std::setfill('0') << m_year << "-"
       << std::setw(2) << std::setfill('0') << m_month << "-"
       << std::setw(2) << std::setfill('0') << m_day;
    return ss.str();
}
