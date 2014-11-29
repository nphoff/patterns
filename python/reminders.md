Reminders
---

- Things that should be remembered but aren't necessarily in code.

xrange
---
range will generate an array, xrange is a generator, which means something like range(100000000) will use all available memory, and xrange(100000000) will not.  Useful when you have to iterate over a huge amount of stuff.

help
---
you can do help(some_object) to get the help for that object (sort of like ipython's some_object?)
