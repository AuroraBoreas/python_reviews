#include "meta.h"

// ctors
Time::Time(short h, short m, short s)
{
    if(!setTime(h, m, s))
        hour = minute = second = 0;

    this->hour   = h;
    this->minute = m;
    this->second = s;
}

bool Time::setTime(short hour, short minute, short second) const
{
    if(   (hour<0   || hour>24)
       && (minute<0 || minute>60)
       && (second<0 || second>60))
    {
        return false;
    }
    return true;
}

void Time::setTime(void)
{
    struct tm *timeinfo;
    time_t rawtime; std::time(&rawtime);
    timeinfo = std::localtime(&rawtime);

    this->hour   = (short)timeinfo->tm_hour;
    this->minute = (short)timeinfo->tm_min;
    this->second = (short)timeinfo->tm_sec;
}

// getter
short Time::Hour(void) const
{ return this->hour; }

short Time::Minute(void) const
{ return this->minute; }

short Time::Second(void) const
{ return this->second; }

// setter
void Time::Hour(short val)
{ this->hour = val; }

void Time::Minute(short val)
{ this->minute = val; }

void Time::Second(short val)
{ this->second = val; }

// other
std::string Time::toString(void) const
{
    std::stringstream ss;
    ss << std::setw(2) << std::setfill('0') << this->hour   << ':'
       << std::setw(2) << std::setfill('0') << this->minute << ':'
       << std::setw(2) << std::setfill('0') << this->second;
    return ss.str();
}
