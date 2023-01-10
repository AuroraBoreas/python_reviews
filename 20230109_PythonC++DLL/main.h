#ifndef __MAIN_H__
#define __MAIN_H__

#include <windows.h>
#include <cmath>
#include <iostream>

const double e = 2.7182818284590452353602874713527;

class Foo
{
    private:
        int val;
    public:
        Foo(int);
        ~Foo(void);
        void bar();
        int add(int);
};

#ifdef BUILD_DLL
    #define DLL_EXPORT __declspec(dllexport)
#else
    #define DLL_EXPORT __declspec(dllimport)
#endif


#ifdef __cplusplus
extern "C"
{
#endif
    int DLL_EXPORT Add(int a, int b);
    double DLL_EXPORT sinh_impl(double x);
    double DLL_EXPORT cosh_impl(double x);
    double DLL_EXPORT tanh_impl(double x);
    long DLL_EXPORT Sum(long*, long);
    Foo* DLL_EXPORT Foo_new(int n);
    void DLL_EXPORT Foo_bar(Foo* f);
    int DLL_EXPORT Foo_add(Foo* f, int val);
    void DLL_EXPORT Foo_del(Foo* f);

#ifdef __cplusplus
}
#endif

#endif // __MAIN_H__
