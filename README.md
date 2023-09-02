# 100 Days of Code: The Complete Python Pro Bootcamp for 2023

I found this [course on Udemy](https://www.udemy.com/course/100-days-of-code/)
while searching for good resources for my brother to learn coding -- he had
mentioned having some interest in learning but not knowing where to start, or
whether any of the boot camps were any good for getting a job, or even whether
he would enjoy it. I wanted to find something that covered a lot of ground and
would be suitable for a beginner but actually have projects that would be neat
to show off and satisfying to accomplish.

I had already learned programming before bootcamps became a thing, but I have
seen a lot of university courseware and online tutorials, and having developed
my own course materials when I taught `CSC 316: Data Structres and Algorithms`,
I've acquired some ability to judge the quality of courseware and this course
does look really good in a lot of ways.

But, I want to be sure, and I want to be able to fill in any gaps or answer any
uncertainties for my brother during his journey learning Python. I'm going to
watch the classes and attempt all of the exercises and use this repository to
save and share my work.  Maybe I'll also take away some project pieces for my
portfolio, but I hope also to be able to help my brother and anyone else taking
this course with learning how to code in Python.  I won't be providing all of
the course material, only my solutions to the exercises (as another data point
to compare to the instructor's solution).  The quizzes so far have been good for
making you think about the material, I highly recommend doing those and watching
the videos if you're interested in the example solutions I'm providing here.

_Please_, **PLEASE!** if you are taking this course do not simply copy my code,
but work through the exercises on your own. Refer to this code when you get
stuck, maybe some of what I wrote will help you, but don't expect the code to
be a substitute for the course material, either.  If you feel the need to copy
some part of it, follow the usual guidance to only copy/paste code that you
understand.  Type it by hand so you're forced to read through all of it.  If
you're not sure, change it! see what breaks or changes and if it matches your
expectations.

Also, if you see bugs or other issues in my code, or just think there might be
a more elegant/Pythonic way to do something, you can use this repo and Issues
or Pull Requests to notify me.  I may include your code and give attribution or
I may try to impart my reasoning for the way it is written.  I will not be
playing code golf or using fancy techniques for their own sake -- my primary
motivation will consistently be explainability.  I want the code to make sense
on first reading and not be too opaque or confusing.  So, any contributions
should also have that goal in mind.

I will also try to include a README.md in each day's folder.  This will have any
comments on the coding exercise and instruction material and will also explain
any organizational or algorithmic choices that I consider to be non-obvious.  I
hope that it will help, not just as a review of the material but also as another
perspective on the exercise and my chosen solution.  I chose the naming README
instead of NOTES or GUIDE because GitHub will automatically surface the markdown
of a README.md found in a folder when browsing the folder on GitHub.

## Folders per day, not branches

I chose to put each day's code in its own folder.  I had considered using the
branches of the repository and making everything organized by project.. but this
would be more challenging to navigate and would make sharing code across days
more complicated (I would probably just duplicate the code instead of trying to
consistently get the branch-parenting right).  Since my motivation here is in
helping others, I want it to be easy to go straight to the day in question and
if it depends on a good chunk of code from a previous day it will be obvious
from the `import .dayXX.library` statements.

## Dependencies (Python 3.10+)

See `requirements.txt` for any third-party dependencies (typically these are
per-day requirements so they are stored in the day's folder, rather than having
to install unrelated dependencies if only one of the projects is of interest).
I recommend using `pip` to install them:

```
> pip install -r dayXX/requirements.txt
```

Let me know if I accidentally miss a dependency in one of my `requirements.txt`
files.  If there is no file that probably means there are no external deps.

## All VSCode, no Replit or Coding Rooms

This was a personal decision.  I would rather have all my code here in one place
than have it scattered about, and I'm already familiar enough with running and
testing code in VSCode.  But don't let that deter you from using these tools!
Especially if you haven't used an IDE previously.  There's a reason the course
starts you off with these tools, so you're not climbing several learning curves
at the same time right at the start.

