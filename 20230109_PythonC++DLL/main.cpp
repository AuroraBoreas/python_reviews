#include "main.h"

int DLL_EXPORT Add(int a, int b)
{ return a + b; }

double sinh_impl(double x)
{ return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x)); }

double cosh_impl(double x)
{ return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x)); }

double tanh_impl(double x)
{ return sinh_impl(x) / cosh_impl(x); }

long Sum(long* numbers, long n)
{
    long total = 0;
    for(int i = 0; i < n; i++) {
        total += numbers[i];
    }
    return total;
}

Foo::Foo(int n)
{ this->val = n; }

void Foo::bar()
{ std::cout << "Value is " << this->val << std::endl; }

int Foo::add(int n)
{ return this->val + n; }

Foo::~Foo(void)
{
    std::cout << "DLL Foo object is deleted from memory" << std::endl;
}

Foo* DLL_EXPORT Foo_new(int n)
{ return new Foo(n); }

void DLL_EXPORT Foo_bar(Foo* f)
{ return f->bar(); }

int DLL_EXPORT Foo_add(Foo* f, int n)
{ return f->add(n); }

void DLL_EXPORT Foo_del(Foo* f)
{ delete f; }
