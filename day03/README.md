# Day 3

```python
if understanding("conditionals").when < datetime.Today():
  day03.tedious = True
elif not understanding("conditionals"):
  rewatch(day03)
else:
  understanding("conditionals").when = datetime.Today()  # clamped to day start
```

I did not type out all of the exercises, only the final one.  I hope that's ok,
the concept of conditionals is so fundamental that I've proably typed 1000 of
them already, and that's just in Python.  There were 11 of them just in the
extra work I did in the tip calculator yesterday!  So, yeah, I'm good on ifs.

I'm actually a little surprised that there were already 7 or 8 example programs
with some utility without even using a single conditional!  Kudos.

Ok, I was tempted to do leap year computation, there is a way to do it without
conditionals and just div, add, mod and picking the bits out from that using
logical operators.  But that wouldn't really be fair, the course material is
supposed to focus on conditionals here, and it would arguably go against the
primary motive of readability and explainability.

But for the leap-year problem, in the real world you would likely call out to
the existing calendar module and its `isleap` function.

```python
import calendar
year = input("Which year? ")
eh = "a " if calendar.isleap(int(year)) else "not a "
print(f"It's {eh} leap year.")
```

I'm not sure about dedicating an entire day to conditionals, but it is at the
core of every program, and it's important to know really well.  And the logical
operators were covered, too.  I guess it's not too surprising, you could spend
two to three classes on it if it was presented in a Discrete Mathematics course.

I love that the day's final exercise is a Choose Your Adventure story.  This is
the kind of program that I wrote as a kid when first learning BASIC, though I
tried to include some world design as well, it still consisted of a lot of
if-then conditionals too.

I still have the notes I took down on paper for some of
those games I wrote, back then the Atari 800XL we had didn't have any storage
(there were cassette drives so you could store data on tapes, but we didn't have
one and I didn't even know they existed).  I took enough notes to be ready to
type it all in.  Hours of data entry for a few minutes of entertainment.  Some
programs broken up into multiple sessions because it used the one TV in the
house, but at least there was a toggle for switching between the antanna and the Atari.
Then, after I'd played it and anyone else that wanted to, I turned off the power
and the program was gone forever.  It was probably good, though, since I
didn't develop any strong attachments to these first programs, I didn't develop
strong attachments to the programs I wrote early in my career either.  And hey,
I still have the notes if I really want a memento.

Anyway, yeah, computing is different now.  There is some throwaway code out there that I
wouldn't even show anyone, it got the job done and I needed only give
barely enough attention to it, it was just meant as a quick fix at first..
and some of that code will probably outlive me.

I made the adventure game a little more interesting by building a map.  I didn't
follow the flowchart exactly but close enough.  I tried reconstructing the E.T.
Atari game's map and theme.  There is no treasure, only death or a cold bleak
reality.  But it's fun!  Or, it was fun to write.

Something that Python is missing, although the other facilities of Python make
it possible to code up in about 120-150 lines, is a case-matching selection of
some kind.  C and C++ have a rudimentary form of it, ML and Haskell have more
sophisticated forms of it.  Javascript eventually got some flavor of it, but
indirectly through the spread operator (added in EcmaSript 6).
You can hack it into Python manually with
a lot of if/elif/else, and if the flow chart is small enough or the types
consistent enough, it is fine to do it that way, possibly more efficient.  But
if you want any amount of extensibility to types that aren't defined within the
scope of the matching logic, well, that takes some special-handling code where in
other languages it comes built in.  But Python wins out in other ways,
especially low visual clutter and a wide variety of libraries available.
