Title: malloc/free implementation. Just4Fun!
Date: 2015-11-26 00:08
Modified: 2016-01-24 22:22
Tags: c, tlpi, glibc, memory
Author: José Guilherme Vanz

Some time ago I bought the The Linux Programming Interface book, one of the best books I have acquired.
One of the first chapters I read were about memory allocation. At the end of the chapter, author offers some exercises
to the reader. Among them there is a challenging one. He suggests to implement the equivalent to the malloc and free
functions. The challenge has been accepted!

First of all, this implementation is just for study purposes. It means you should NOT start to implement your malloc and
free functions for production programs. Do not reinvent the wheel! The glibc are being improved for decades for many
great guys. You probably will take more time to do the equivalent excellent work! ;)

I assume that you know a little bit about how a process and its segments works. It is nice remember this code does not
cover all details. As any software it can be improved (a lot).
