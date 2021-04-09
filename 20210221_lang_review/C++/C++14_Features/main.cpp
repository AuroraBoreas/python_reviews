#include <iostream>
#include <memory>
#include <string>

inline auto add(int& x, int& y) -> int
{
    return x + y;
}

int main()
{
    // #1 digit separator literal
    long x = 1'000'000'000;
    std::cout << x << std::endl;

    // #2 binary literal
    int a = 0xFF;
    int b = 0B11111111;
    std::cout << a << ", " << b << std::endl;

    // #3 lambda template/polymorphic
    auto c = [](const auto a, const auto b) { return a + b; };
    std::cout << c(1, 3) << std::endl;

    // #4 auto deduction
    int x1 = 3, x2 = 4;
    std::cout << add(x1, x2) << std::endl;

    {

    }

    return 0;
}
