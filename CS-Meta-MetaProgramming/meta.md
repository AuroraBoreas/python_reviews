# What does Meta- mean?

`Meta` is a word which, like so many other things, we have the ancient Greeks to thank for. When they used it, `meta` meant "beyond", "after", or "behind". The "beyond" sense of `meta` still lingers in words like `metaphysics` or `meta-economy`. But that's still NOT the `meta` most of us come acrosss today.

One of the more popular uses of `meta` today is for the meaning best described by the formula:

```
meta-X == X about X(s)
```

So, if we take the word "data" for our X, and add the prefix `meta`- to it, we get `metadata`, or "data about data". A `meta-txt` os a text about texts, `metacognition` is thinking about thinking, and a `meta-joke` is a joke about jokes. The self-reflection sense of `meta` has also given rise to the use of the word as a standalone adjective, where `meta` is used to describe something that's self-reflective or self-referencing.

The self-referencing sense of `meta` seems especially popular in art. In its simplest form, a book in which a character is writing a book or a movie in which a character is making a movie can be described as `meta`. Some works are more `meta` than others--the movie `Birdman`, for example, is a movie about an actor who played a superhero in a movie and who now tries to rekindle his career in theater, and that actor is played by an actor who really did play a superhero in a movie and is now trying to rekindle his career in a movie that looks more like a play than a movie.

When characters in a work of fiction act as if they are aware that they are in a work of fiction, this technique is called `meta-referencing`. It is often employed in `metafiction`, a work of fiction in which the author breaks with convention in order to show that the work is, in fact, fiction.

In the world of gaming, `meta` is used in two ways. `Meta` can be used as an acronym for `most effective tactics available`, and calling something `meta` means that it's an effective way to achieve the goal of the game, whether it's to beat other players or beat the game itself. `Meta` can also be short for `metagame`, which is using information about the game, derived from the world beyong the game or its rules, to influence the outcome of the game or gain a competitive edge.

# What is meta-programming?

`meta-programming` refers to variety of ways a program has knowledge of itself or can manipulate itself.

In languages like C#, Java, reflection is a form of `meta-programming` since the program can examine information about itself.

`meta-programming` relates actually to many things.

- <b>Macro</b> The ability to extend the syntax and semantics of a programming language was explored first under the terminology macro.

- <b>DSL</b> The ability to extend one language syntax and semantics is now rebranded under the term "DSL". The easiest way to create a DSL is with the `interpreter pattern`.

- <b>Reflection</b> `meta-programming` is also inseparable from reflection. The ability to reflect on the program structure at run-time is immensely powerful.
  
- <b>Annotations</b> Annotations could be seen as a subset of the reflective capabilities of a language, but I think it deserves its own category. Annotations are meta-data that can be processed at compile-time or at run-time.

- <b>Byte-code or AST transformation</b>. This can be done at compile-time or at run-time. This is somehow are low-level approach but can also be considered a form of `meta-programming` (in a sense, it's the same as macro for non-homoiconic language)

## Conclusion
`meta-programming` is the ability for a program to reason about itself or to modify itself. Just like `meta stackoverflow` is the place to ask question about stack overflow itself. `Meta-programming` is not one specific technique, but rather an ensemble of concepts and techniques.

## Demonstration by example

<b>it is the C++ compiler that generates the Fibonacci series at compile-time, NOT your program while it runs.</b>

```C++
unsigned int fib(usgined int n)
{
    return n >= 2 ? fib(n-2) + fib(n-1): n;
}
```

## Farther Reading
(What Does Meta- Mean?)[https://www.grammarly.com/blog/meta-meaning/]

(What exactly is meta-programming?)[https://stackoverflow.com/questions/514644/what-exactly-is-meta-programming]

(java meta-programming - self explanatory code - tutorials, articles, books [closed])[https://stackoverflow.com/questions/2565572/meta-programming-self-explanatory-code-tutorials-articles-books]


## About

Copyright &copy; 2020 ZL

All rights reserved.

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
