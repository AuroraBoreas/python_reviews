#include "meta.h"

bool Date::isLeapYear(unsigned year) const
{
    return (year%4 == 0 && year%100 != 0) || (year%400 == 0);
}

Date::Date(unsigned year, unsigned month, unsigned day)
{
    if(!setDate(year, month, day))
        m_year = m_month = m_day = 1;

    this->m_year  = year;
    this->m_month = month;
    this->m_day   = day;
}

bool Date::setDate(unsigned y, unsigned m, unsigned d)
{
    if(m>12) { return false; }
    if(d>30) { return false; }
    switch(m)
    {
        case 2: if(isLeapYear(y))
                {
                    if(d>29) { return false; }
                }
                else
                {
                    if(d>28) { return false; }
                }
                break;
        case 4:
        case 6:
        case 9:
        case 11: if(d>30) { return false; }
    }

    return true;
}

void Date::setDate(void)
{
    struct tm *timeinfo;
    time_t sec; std::time(&sec);
    timeinfo = std::localtime(&sec);

    this->m_year  = (unsigned)timeinfo->tm_year + 1900;
    this->m_month = (unsigned)timeinfo->tm_mon + 1;
    this->m_day   = (unsigned)timeinfo->tm_mday;
}

unsigned Date::Year(void) const
{ return this->m_year; }

unsigned Date::Month(void) const
{ return this->m_month; }

unsigned Date::Day(void) const
{ return this->m_day; }

void Date::Year(unsigned val)
{ this->m_year = val; }

void Date::Month(unsigned val)
{ this->m_month = val; }

void Date::Day(unsigned val)
{ this->m_day = val; }

std::string Date::toString(void) const
{
    std::stringstream ss;
    ss << std::setw(4) << std::setfill('0') << this->Year()  << '-'
       << std::setw(2) << std::setfill('0') << this->Month() << '-'
       << std::setw(2) << std::setfill('0') << this->Day();
    return ss.str();
}

