#include <iostream>
#include <string>
#include <memory>
#include <string_view>

template<typename T>
T PI(3.14159261182182313123L);

[[deprecated("this function is deprcated!")]]
inline auto add(int x, int y) -> int
{
    return x + y;
}

template<typename T>
auto add(T x, T y) -> T
{
    return x + y;
}

template<typename T, typename ...>
auto addCpp(T& arg1, ...& args) -> T
{
    return addCpp(T, ...args);
}

int main()
{
    // #1 digit separator literal
    long a = 1'000'000'000;

    // #2 binary literal
    int x1 = 0xFF;
    int x2 = 0B1111111;

    // #3 variable template
    std::cout << PI<int> << std::endl;
    std::cout << PI<long> << std::endl;
    std::cout << PI<float> << std::endl;
    std::cout << PI<double> << std::endl;

    // #4 return_value deduction 
    std::cout << add(3, 4) << std::endl;   

    // #5 lambda template/polymorphic
    auto c = [val = [](){ return 3; }](auto x, auto y){ return x + y; };
    std::cout << c(1, 2) << std::endl;
    
    // #6 std::string_view
    std::string_view name = "hello ZL";

    // #7 std::make_unique
    auto ptr(std::make_unique<int>());
    std::cout << *ptr << std::endl;

    // #8 spaceship <=>, is similar with @functools.total_ordering in Python

    // #9 [[deprecated]]
    std::cout << add(4, 5) << std::endl;
    std::cout << add<int>(3, 4) << std::endl;

    // #11 CRPT

    // #12 constexpr, declare and free, dont use freed memory(UB)
    constexpr auto x = []() ->int {
        int i = 69;
        int *ptr = &i;
        int val = *ptr;
        delete ptr;
        return val;
    };

    // #13 variadic template
    
    // #14 unpack
    auto p = std::make_pair<int, std::string>(69, "hello world");
    auto [x3, y1] = p; 

    return 0;
}