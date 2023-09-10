# Day 6

I really like the use of this sandbox Karel for the lesson covering functions
and more advanced looping.  There was a tricky question in the quiz where a
recursive call would technically output what was expected (but it will output
it indefinitely, until the process overflows its stack or the OS crashes).

The gradual introduction of complexity was done well during this lesson, and
coding up a navigation routine for the robot with increasingly complicated (and
randomized!) terrain, is really good.  For the solution of the varying-height
hurdles, I would have solved it with a recursion, but this is a little advanced.
I'll share it here in case you'd like to see an elegant and brief solution:

```python
def jump():
  turn_left()
  jump_higher()
  
def jump_higher():
  move()
  if wall_on_right():
    jump_higher()
  else:
    turn_right()
    move()
    turn_right()
  move()

while not at_goal():
  jump() if wall_in_front() else move()
```

Just 14 lines! and still fairly readable, IMHO.  Each time we call jump to go
another step up, we know we'll need to take a step back down later.  So rather
than having to keep checking the left wall, it just moves again after the call
to jump_higher().  A function calling itself like this can take advantage of the
self-similarity to consistenly perform both before- and after- actions.  In the
case of more complex structures like trees and graphs, it can be very useful to
have the per-node or per-edge computation separated out into its own function
this way, too.  But, the kind of thinking needed to approach a recursive form
of a solution is significantly more challenging than approaching it as a fully
procedural solution.  There are techniques to help but I will save that for
later, after more programming knowledge has been acquired.

The instructor covered indentation and spaces vs tabs, and vim vs emacs!  I am
definitely a spaces and vim person, but I don't judge others for whatever choice
they make, that's their personal choice.  In Google all the languages style
guides restrict indentation to two spaces, four for continued lines.  Even the
guidelines for languages like C and Python where the language standard is 4
spaces.  Even though the author of Python (Guido van Rossum) was working at
Google at the time!  I've gotten so used to two spaces I always update my editor
to that as part of setting things up.  I also turn on vim mode in any editor
that supports it (VS Code, Eclipse, emacs) and if the platform doesn't have a
good graphical IDE I'll install vim before anything (and in any good OS it's
already there).

The maze-solving exercise is left out here because it wouldn't be much different
than what the instructor provided.  I'm tempted to implement A* (an improvement
over following the right-hand wall) but maybe I'll come back and do that later.