#ifndef DATETIME_H_INCLUDED
#define DATETIME_H_INCLUDED

#include "date.h"
#include "time.h"

class DateTime: public Date, public Time
{

public:
    DateTime(int year = 1, int month = 1, int day = 1,
             unsigned short m_hour = 0,
             unsigned short m_minute = 0,
             unsigned short m_second = 0);

    ~DateTime(){}

    void SetDateTime(void);

    std::string ToString(void) const;

    friend std::ostream& operator<<(std::ostream& os, const DateTime& dt)
    {
        os << dt.ToString();
        return os;
    }

};


#endif // DATETIME_H_INCLUDED
