Ah, (pseudo-)random numbers.  Introducing this at the same time as lists is a
good idea, as often the thing you want to do with a list is either a) select a
random element from it, or b) go through all of its elements.  Sometimes, one
specific element is wanted, but in practice a more structured data type than
lists is used in those cases.  What you want to do with the element determines
the structure you choose, and it depends also on whether the data is permanent
or temporary.

The 0-offset thing can trip a lot of people up at first, especially when the
actual layout of data in memory is not made explicit by the language.  Here is
how it makes sense to me, because C and C-like languages were where I learned
heavy use of lists:
the reference to a list is where it starts, and its index gives you its address
by 

   $address = address_{start} + (index * size)$

That is, the index at zero is the element stored at the start of the list, the
next element is at the `start + size`, the next at `start + 2 * size`, and so
on.  Here's some ASCII art:

```
 base address (where the variable of the list points)
 |                            tail (base + len * size)
 v                            v
 [----,----,----,--     -,----]
 [    |    |    |   ...  |    ]
 [----'----'----'--     -'----]
      ^    ^             ^
      |    |             last element (base + (len-1)*size)
      |    |
      |    base + 2 * size
      |
      base + size
```

Where `size` is the addressable size.  This is often single bytes (as before
when we were looking at characters in a string) but it can be any size, and is
very useful in some contexts -- a pair of ints can address more disk space than
what an int32 could, even before we had 64-bit processors, or when drawing
graphics on a screen it's useful to chunk things into lines and pixels (which
depend on the color depth for size) and you'll find that again in GPU shaders
or in tensors for deep neural networks.

From this perspective, it makes sense that 0 would indicate the very start of
the list.  You can always make a 1-indexed list from a 0-indexed one, too (if
you ignore the first element or use it to define a length or metadata, there
are clever uses but most of them are too clever for their own good).  But you
can't get a 0-indexed list from a 1-indexed one without going around the syntax
and conventions of the language.  And that usually just confuses your peers in
the long run, something you usually want to avoid if you want your code to have
continuing use.

There are a few languages that chose to define the start of a list at index 1
instead of at 0 (COBOL, Fortran, Lua, R, MATLAB, Smalltalk, Awk, some others...)
but the convention in the 1000s of other languages is to use 0 as the first
element.  There are some libraries that try to give definition to the difference
where lists are indexed by 1 (think checklists or sequences, first is 1) and an
array or other arbitrary BLOB would be indexed by 0.  I think it only increases
confusion to give both as an option, though.  And some libraries will actually
enforce a 1-based indexing even when the language uses 0-based!  Only when
emulating a 1-based indexing system would that really be rational, though.

In my final exercise I implemented Rock, Paper, Scissors a little differently
than instructed.  I handle DRAW outcomes by re-running the match (which uses
a loop, something I think hasn't been introduced yet) and I implement the
win v. lose v. draw calculation a little more elegantly (see comments).  I also
give the user the choice of skin tone and use emoji to show the plays instead of
ASCII art, which I think will be reusable in a future lesson if this game is
ported to a web app interface.