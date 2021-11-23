#include "graphic.h"

void Shape::accept(const Visitor* v) const
{
    v->visit(*this);
}

void Dot::accept(const Visitor* v) const
{
    v->visit(*this);
}