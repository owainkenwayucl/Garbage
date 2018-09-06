Julia microbenchmarks fiddling
==============================

The Julia project publish some microbenchmarks which include a benchmark called "pisum".  Since calculating Pi is one of muy hobbies, I was interested to see how it works.  It doesn't.  What it does is calculate 1.6448... 500 times.

The `.py` and `.jl` files are exactly this routine, MIT licensed from the Julia project.  The `.cl` file is my implementation in Common LISP.