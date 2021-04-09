
class Point
{
    _x;
    _y;

    constructor(x, y)
    {
        this._x = x;
        this._y = y;
    }
    
    // getter
    get X(){ return this._x; }
    get Y(){ return this._y; }
    // setter
    set X(val){ this._x = val; }
    set Y(val){ this._y = val; }

    ToString(){
        return `[${this._x}, ${this._y}]`;
    }

    Add(other){
        return new Point(this.X + other.X, this.Y + other.Y);
    }

    Sub(other){
        return new Point(this.X - other.X, this.Y - other.Y);
    }

    Mul(val){
        return new Point(this.X * val, this.Y * val);
    }

    K(other){
        return (this.Y - other.Y) / (this.X - other.X);
    }
}

class IShape
{
    Circumentference(){}
    Area(){}
}

class Rectangle extends IShape
{
    _length;
    _width;
    constructor(length, width){
        this._length = length;
        this._width = width;
    }

    Circumentference(){
        return (this._length + this._width) * 2;
    }

    Area(){
        return this._length * this._width;
    }
}

class Circle extends IShape
{
    _radius;
    constructor(radius){
        this._radius = radius;
    }

    Circumentference(){
        return 2 * Math.PI * this._radius; 
    }

    Area(){
        return Math.PI * this._radius * this._radius;
    }
}

exports.Point = Point;
exports.IShape = IShape;
exports.Rectangle = Rectangle;
exports.Circle = Circle;