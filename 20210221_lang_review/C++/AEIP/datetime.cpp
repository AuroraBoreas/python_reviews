#include "datetime.h"

DateTime::DateTime(int year, int month, int day,
                   unsigned short hour,
                   unsigned short minute,
                   unsigned short second)
: Date(year, month, day), Time(hour, minute, second)
{}

void DateTime::SetDateTime(void)
{
    Date::SetDate();
    Time::SetTime();
}

std::string DateTime::ToString(void) const
{
    return Date::ToString()  + " " + Time::ToString();
}
