#include "time.h"

#include <ctime>
#include <iomanip>
#include <sstream>

Time::Time()
{
    m_hour = m_minute = m_second = 0;
}

bool Time::SetTime(unsigned short hour,
              unsigned short minute,
              unsigned short second) const
{
    if(hour > 24) return false;
    if(minute > 60) return false;
    if(second > 60) return false;
    return true;
}

Time::Time(unsigned short hour,
           unsigned short minute,
           unsigned short second)
{
    if(!SetTime(hour, minute, second))
    {
        m_hour = m_minute = m_second = 0;
    }
    else
    {
        m_hour = hour;
        m_minute = minute;
        m_second = second;
    }
}

Time::~Time() {}

void Time::SetTime(void)
{
    struct tm *tm;
    time_t sec; std::time(&sec);
    tm = std::localtime(&sec);

    m_hour = (unsigned short)tm->tm_hour;
    m_minute = (unsigned short)tm->tm_min;
    m_second = (unsigned short)tm->tm_sec;
}

unsigned short Time::Hour(void) const
{ return m_hour; }
unsigned short Time::Minute(void) const
{ return m_minute; }
unsigned short Time::Second(void) const
{ return m_second; }

void Time::Hour(unsigned short val)
{ m_hour = val; }
void Time::Minute(unsigned short val)
{ m_minute = val; }
void Time::Second(unsigned short val)
{ m_second = val; }

std::string Time::ToString(void) const
{
    std::stringstream ss;
    ss << std::setfill('0') << std::setw(2) << m_hour << ":"
       << std::setfill('0') << std::setw(2) << m_minute << ":"
       << std::setfill('0') << std::setw(2) << m_second;
    return ss.str();
}
