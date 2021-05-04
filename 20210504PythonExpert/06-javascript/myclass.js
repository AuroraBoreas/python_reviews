
class Point {
    _x;
    _y;

    constructor(x, y) {
        this._x = x;
        this._y = y;
    }

    ToString() {
        return `[${this.X}, ${this.Y}]`;
    }

    get X() { return this._x; }
    get Y() { return this._y; }

    set X(val) { this._x = val; }
    set Y(val) { this._y = val; }

    Add(other) {
        return new Point(this.X + other.X, this.Y + other.Y);
    }

    Sub(other) {
        return new Point(this.X - other.X, this.Y - other.Y);
    }
}

class Random {
    constructor(min, max) {
        this.min = Math.ceil(min);
        this.max = Math.floor(max);
    }
    RandInt() {
        return Math.floor(Math.random() * (this.max - this.min + 1)) + this.min;
    }
}

class IShape {
    circumference(){}
    area(){}
    ToString(){}
}

class Rectangle extends IShape {
    constructor(length, width) {
        this.length = length;
        this.width = width;
    }

    circumference() {
        return (this.length + this.width) * 2;
    }

    area() {
        return this.length * this.width;
    }

    ToString() {
        return `Rectangle(length=${this.length}, width=${this.width}`;
    }
}

class Circle extends IShape {
    constructor(radius) {
        this.radius = radius;
    }

    circumference() {
        return Math.PI * this.radius * 2;
    }

    area() {
        return Math.PI * this.radius * this.radius;
    }

    ToString() {
        return `Circle(radius=${this.radius})`;
    }
}

exports.Point = Point;
exports.Random = Random;
exports.Rectangle = Rectangle;
exports.Circle = Circle;
