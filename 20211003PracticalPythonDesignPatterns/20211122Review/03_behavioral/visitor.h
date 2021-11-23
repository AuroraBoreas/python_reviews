#ifndef VISITOR_H_INCLUDED
#define VISITOR_H_INCLUDED

#include <iostream>

class Shape;
class Dot;

class Visitor
{
    public:
        void visit(const Shape& s) const;
        void visit(const Dot& d) const;
}; // class Visitor

#endif