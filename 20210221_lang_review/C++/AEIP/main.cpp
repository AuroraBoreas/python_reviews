#include <iostream>
#include "time.h"
#include "date.h"
#include "datetime.h"

int main()
{
    {
        Time t1 = Time();
        std::cout << t1 << std::endl;
        t1.SetTime();
        std::cout << t1 << std::endl;
    }

    {
        Date d1 = Date();
        std::cout << d1 << std::endl;
        d1.SetDate();
        std::cout << d1 << std::endl;
    }

    {
        DateTime dt1 = DateTime();
        std::cout << dt1 << std::endl;
        dt1.SetDateTime();
        std::cout << dt1 << std::endl;
    }

    return 0;
}
