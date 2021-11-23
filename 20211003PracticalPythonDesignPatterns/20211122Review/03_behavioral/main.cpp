#include "graphic.h"
#include "visitor.h"
#include <vector>
#include <algorithm>

int main()
{
    Shape s = Shape();
    Dot d = Dot();
    Visitor v = Visitor();
    std::vector<Graphic*> g { &s, &d };

    std::for_each(g.begin(), g.end(),
                  [&](const Graphic* e){ e->accept(&v); });
    
    std::cin.get();

    return 0;
};