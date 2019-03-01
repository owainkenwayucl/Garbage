Julia microbenchmarks fiddling
==============================

![Fast mac](../../images/icons/fastmac.png)

The Julia project publish some microbenchmarks which include a benchmark called "pisum".  Since calculating Pi is one of muy hobbies, I was interested to see how it works.  It doesn't.  What it does is calculate 1.6448... 500 times.

The `microbench.py` and `microbench.jl` files are exactly this routine, MIT licensed from the Julia project.  The `microbench.cl` file is my implementation in Common LISP.

The `matrix.py` file is an implementation of the two Numpy based benchmarks.
