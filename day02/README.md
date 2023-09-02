# Day 2

Data types!  I wonder if it is a little early to be introducing this but it is
a super important concept in basically every programming language.  And, the
instructor keeps it simple at first, just introducing (string, int, float, bool)

I feel like there were maybe too many metaphors used here, but that's probably
just a bias because I know enough details of how CPython implements these types
that I spot the tiny flaws in the metaphors, but they are good enough to shed
light on the topic.

Don't name your num_char variable new_num_char after converting.  After the
previous day's emphasis on variable naming, I'm a little surprised she used
this name.  Six months from now will `new_num_char` tell you anything useful?
No.  Name it `num_char_str`, if you even need to name it at all.  Most of the
time it is ok to just do the str(num_char) conversion inline, or use f-strings
to handle the string interpolation for you (like `f"blahblahblah {num_char}"`).

I think the course material and coding exercises so far are good for beginners,
and I especially like the encouragement to try finding the answers on your own.

It's a little annoying to have to keep re-setting the video speed every 10
minutes because the next video doesn't keep the settings of the previous video..
I'll get over it, though.  I understand why the videos are in these bite-sized
pieces, it helps that it allows for taking a break in the middle of session and
gives a sense of progress at the end of each video.  It was probably also easier
to record and edit that way.  [Correction: this is only on the mobile interface.
The web interface for Udemy does what I would expect.]

An aside, I would have manipulated the equation as
   > 3 * 3 / 3 + 3 - 3

but there are many solutions, and a few that involve only inserting parentheses.

The BMI exercise is useful for thinking about when some data types are more
useful than others, and the many assumptions that can creep into code (meters?
kilograms? yeah not everyone even knows what their weight and height are in
those units.. and conversion would introduce the issue of how to prompt for a
value and its unit without bothering half your users in doing so).

The tip calculator is a good exercise at this early stage.  Some input handling,
some type conversion and calculation, and formatting a result, plus it's even
useful, if you happen to have a python interpreter handy 😂.  Well, it could be
ported to a web service in a month or two, as most of these text-heavy examples
can.  I suppose if I had used the Replit or Code Rooms version of this exercise,
I would be able to run it on a web page already.

I added some better error handling and factored the input handling into separate
functions ... ok I know we wouldn't have learned of functions yet but I'm
using it anyway because it's good form.  The input readers handle empty inputs
and malformed inputs with some grace and allow for retrying on bad input if no
default value has been specified.

Doing so makes the implementation on the order of 140 lines (including comments)
instead of the 14 line implementation shown in the instructor's solution.  Yes,
that's right, basic error handling can add 10x lines of code over basic logic.
And we haven't even really exhausted the kinds of inputs we might expect -- what
if we wanted to handle drinks separately from the rest of the meal, or what if
we wanted to accept a Venmo/PayPal/etc. address for coordinating payments?  It
also assumes everyone is going to tip the same amount, but the final calculation
is more or less the same, with maybe a rounding error if the bill is split
before doing the tip-adjustment, as would be the case if only calculating your
own tip amount.

Overall, I would say this is a good pace for two days of instruction, especially
for someone who hasn't been introduced to programming before.  Udemy wanted me
to rate it already, when I'd only seen a few videos, not even before the end of
day 1.  That's far too early for me to make a fair evaluation.  But so far this
course looks good for introductory material, and I'm interested in seeing how
some of the later topics are covered.