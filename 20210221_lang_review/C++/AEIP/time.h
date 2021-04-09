#ifndef TIME_H_INCLUDED
#define TIME_H_INCLUDED

#include <iostream>
#include <string>

class Time
{
private:
    unsigned short m_hour, m_minute, m_second;

public:
    // ctors
    Time();
    Time(unsigned short hour, unsigned short minute, unsigned short second);
    // dtor
    ~Time();

    // getter
    unsigned short Hour(void) const;
    unsigned short Minute(void) const;
    unsigned short Second(void) const;

    // setter
    void Hour(unsigned short val);
    void Minute(unsigned short val);
    void Second(unsigned short val);

    // method
    void SetTime(void);
    bool SetTime(unsigned short hour, unsigned short minute, unsigned short second) const;

    // repr
    std::string ToString(void) const;
    friend std::ostream& operator<<(std::ostream& os, const Time& t)
    {
        os << t.ToString();
        return os;
    }
};

#endif // TIME_H_INCLUDED
