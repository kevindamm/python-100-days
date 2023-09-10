# Day 5

Another super important topic that appears in practically every useful program:
loops!  Any programming language that doesn't have a looping construct (there
are only very few) usually still provide a way around it via function calls or
GOTOs, or looping is inherent to the system running the code (as in game loops
or SQL query execution).

*LOOPS*.  They're like Groundhog Day for CPUs.

I don't have much more to say, if you don't get loops the first time, go back
and cover it again until you do.  Yes, that's `while`, you got it.  Other
programming languages will use `while`, some add a `do { ... } while (cond)` so
that there's an easy way to do something *at least* once.  Go reuses `for {...}`
to cover all of for (range), while and do-while.  Otherwise, if it's a C-family
language the keyword is almost certainly `while`.

The important thing with loops is to be aware when you've nested them two or
three times, because that can start to get expensive.  It's not always obvious
because a loop may contain a function call, and the nested loop is within that
function definition.  For small lists the difference between 5, 25, and 125 may
not seem that much, 125 things can be processed in less than a millisecond.  But
if you have thousands of items then it blows up into millions and billions for
additional nesting.  Still manageable in less than a wait time, if not less than
a blink (approx 200 ms), but add something time-consuming like a network request
or re-layout, and now we're looking at days of delay.  But if you've designed
your program from a high level, you can usually spot where the looping will
happen and avoid nesting things too much.  I wonder if this course goes into
profiling at all.  After debugging, it is a very useful skill (but do things in
the right order: make it, make it work, make it work fast).

For the final exercise I included a few advanced techniques -- constructing
the domain of characters procedurally instead of hard-coding each one (lower
risk of introducing a clerical error).  The `"".join(list)` pattern is a very
useful one and something you'll encounter in Python a lot, and it is typically
faster than the "a" + "b" + "c" + ... form of concatenation.  I've also used a
list comprehension instead of the explicit list construction.  Then, for the
final result I include the character shuffling that was suggested as an extra.
Oh, I also included more symbols than were in the example (basically every
printable character now).

Near the end of the main function you'll notice we had to call random.shuffle()
on its own line.  This is because shuffle() rearranges the original list instead
of returning a new list with the items shuffled.  This is known as a side-effect
and generally should be avoided in APIs, especially in a widely-used library.
It's not merely a point of preference, or a desire to chain function calls (in
this case, it would be nice to call print(random.shuffle(pwd)) but we can't).
It introduces thread-unsafe code.  If two threads were trying to use this list
at the same time, one might be editing it while the other is still looping over
it!  You can imagine the kinds of issues that might introduce.  The only way
around it is to draw a fence around the parts of code that access this list and
make sure that only one is using it at a time.  This introduces contention!  I
can understand that the authors wanted to limit having to ask for more memory
when reordering a large list -- you may already be using more than half of the
available memory! -- but then offer that as an optimized routine, not the one
which people reach for by default.  Anyway, it's not the most troublesome part
of Python when it comes to multithreading.  But maybe the GIL is actually being
removed this year?  Then problems like this will become more of an issue.

Tiny rant done.  You won't have to worry about concurrent programming for a
while, probably, but it is one of the more challenging problems when you get to
advanced programming projects, and often (as seen here) it's because of
limitations introduced in library code that you don't control.  When designing
something purpose-built like this password generator, you can just say that the
list is short-lived and only ever accessed by one thread, something that makes
a LOT of sense for a password-generating program, it should be stored encrypted
if it is kept around any longer, anyway!  But something to think about whenever
you are in a position of designing an API.  Aim for thread-safe, or at the least
thread-compatible, even if it means slightly more complex code or more resource
use.  API decisions are very difficult to undo or change.

Another improvement that could be made to this program is using flags instead of
prompts, but from a security perspective, it's a bad idea to consistently use
the same number of letters, numbers and symbols each time.  Maybe the real
improvement is to only prompt for the length, require it be at least 12 or 16 or
something, and randomly choose the amount of numbers and sybmols.

See also
[Are your passwords in the green?](https://www.hivesystems.io/blog/are-your-passwords-in-the-green?utm_source=tabletext)
for justification of picking at least 12 characters and the benefit of adding
just a few more, or the detriment of including only numbers or only letters.
This table could even be the basis for accepting/rejecting the user's choice
of number of letters vs other character types.