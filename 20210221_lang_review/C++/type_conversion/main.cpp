#include <iostream>

using namespace std;

typedef void (*func_ptr)(char*);

inline void hello(char* s)
{
    std::cout << s << std::endl;
}

int main()
{
    cout << "Hello world!" << endl;

    {
        /*
        [variable]
        ----
        * declaration and definition
            ** early binding
            ** late binding
            ** pattern: T N V
            ** l-value, r-value;
            ** l-reference, r-reference
                *** std::move
                *** std::forwarding
            ** struct
                *** return_type
                *** func_name
                *** parameters


        ----
        */

        int x;
        x = 3.14;
        std::cout << x << std::endl;
        x = int(3.14);
        std::cout << x << std::endl;
        // x = int{3.14}; // error out
        x = int{3};
        std::cout << x << std::endl;
    }

    {
        // func pointer
        func_ptr fp = hello;
        char s[] = "hello ZL";
        fp(s);
    }

    return 0;
}
