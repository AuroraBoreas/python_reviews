#ifndef GRAPHIC_H_INCLUDED
#define GRAPHIC_H_INCLUDED

#include "visitor.h"

class Graphic
{
    public:
        virtual void accept(const Visitor*) const = 0;
}; // class Graphic

class Shape: public Graphic
{
    public:
        void accept(const Visitor* v) const;
}; // class Shape


class Dot: public Graphic
{
    public:
        void accept(const Visitor* v) const;
}; // class Dot

#endif