# Day 1

I like the instructor's occasional use of visualization for new concepts and the
focus on showing the code while it's written.  The explanation of `print()` and
the concept of strings are well done.  String nesting and string manipulation
is a better first concept than simple arithmetic, even though it's a little bit
more complicated to explain than computers basically computing.

The instructor even shared the origin of the word bug, that's a fun story.
Classic.

One of the nicer things about Python is that `print` is a global function and
doesn't need any imports, so starting up a Hello World program is literally one
line and getting from there to string manipulation also only needs to use
built-in functionality of the language and no libraries or cryptic code.  Most
other languages require you to import from a standard library at least, and may
also have a lot of boilerplate code for such a simple example (I'm looking at
you, Java).

This is a tradeoff in language design and there isn't really a better way.  For
the languages that have boilerplate code and explicit library references, you at
least know that these things are being included (or not included) from scanning
over the code.  You also know for sure where the `main` entry loop is, whereas
with Python you can evaluate any Python file as though it were `main`.  It also
reduces the surprising evaluation of global statements (and why we typically use
a guard condition around `main` so that global statements aren't evaluated when
the python file is imported from another python file, but that hasn't been
introduced yet).  Personally, the parts that make Python good are why I often
use it for prototyping ideas but also why I typically don't use it for larger
projects.