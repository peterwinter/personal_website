Troubleshooting the Pyenv/Homebrew Combination
##############################################

:date: 2014-06-06 10:20
:modified: 2014-06-06 10:20
:tags: thats, awesome
:slug: troubleshooting-pyenv
:authors: Peter B Winter
:summary: When first starting to use pyenve with homebrew, there are a couple things you can do to horribly mess things up. Or you could avoid doing them, if you'd prefer to have things functional. I  tried both approaches.


.. role:: underline
    :class: underline

Since I've been hearing such enthusiastic praise for pyenv_, I figured I would implement homebrew and pyenv to set up a pleasing environment for python development on my mac laptop (OS X 10.9.3).

Unfortunately, I immediately started breaking unwritten rules and had to uninstall everything and start over. (While I don't fully know if these rules are truly unwritten, I personally have been able to find them with google.) Here is a brief synopsis of what I have learned.

Overview of the Basics:
-----------------------

(1) Homebrew is for installing and managing general system tools that are useful for many programs outside of python.

(2)  Use pyenv with pip ONLY for installing and managing python.

The secret to using these tools together is to keep their actions separate.
:underline:`None of the python packages you install with brew install will ever be useful while inside your pyenv environments. Switch out of pyenv when you want to install system tools.`
If you really want, you can probably come up with some workarounds to these suggestions, but in general, the point of pyenv environments is to keep them separate

In practice this is implemented because homebrew and pyenv install their goodies into two completely different directory structures.  Brew saves all it's goodies in:

`/usr/local/`


and pyenv, installs each python version (+ packages) in separate directories inside

`~/.pyenv/`

pyenv works by switching the PYTHON_PATH so that it can point at it's own directory. All the python packages installed elsewhere in the filesystem will be ignored.

Setting Things up
-----------------

Ok, Joao already covered the basics on how to "`get pyenv up and running`__", however, there are two important rules to follow when getting started. Initially, out of ignorance I ended up braking both these rules, and hope that writing them down might help my fellow wayfarers.

Rule 1: Only *brew install* while pyenv global is set to *system* and never brew while in a virtual environment.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'm not sure why, but homebrew just won't install things properly if pyenv is engaged. And worse, brew won't tell you if the installation went wrong, the installed program will just fail at inconvenient times.

I'm looking at you, gcc.

Solution
~~~~~~~~

`$ brew uninstall that_thing_you_installed_wrong`

`$ pyenv global system`

`$ brew install that_thing_you_installed_wrong`

Make sure to open an new terminal after you've installed something important.

Use this trick every time you encounter a python package that requires heavy lifting (i.e. installing  non-python drivers).

(1) Set pyenv to system,
(2) install the drivers separately,
(3) open a fresh terminal to get your configuration up to date, and
(4) then  get back into your pyenv of choice for 'pip install'.

Rule 2: The pyenv directory must be before "/usr/local/bin" in your PATH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If this happens, you are probably using the wrong pip to install things. This is because your system looks through your PATH in order and uses the first pip it finds. Make sure that you are really using your .pyenv pip. If you are using the wrong pip, then you will most likely also have these two symptoms:
(A) pip install without sudo has permissions problems and
(B) the pip python package you just installed is not found by python.

To check if this is indeed your problem, check your path from the command line using:

`$ echo $PATH`

Solution:
~~~~~~~~~

Make sure these lines are in you .profile, .bash_profile, .bashrc or whatever your computer calls it.
Make sure they are in this order, and that you don't have any other lines that insert /usr/local/bin first.

`export PATH=/usr/local/bin:$PATH`

`export PYENV_ROOT="$HOME/.pyenv"`

`export PATH="$PYENV_ROOT/bin:$PATH"`


Closing Remarks
---------------

Following these two rules fixed everything that I needed to get up and running with numpy, scipy, matplotlib, pandas, and ipython notebook. Really, everything I need for 99% of my work.  I still haven't figured out how to get opencv functional inside my pyenvs, but hey,  that's for another day.

special thanks to Joao_ and Adam_ for their help in getting my python functional.

.. _pyenv : https://amaral.northwestern.edu/blog/pyenv-tutorial
.. _Joao : https://amaral.northwestern.edu/people/jmoreira/
.. _Adam : https://amaral.northwestern.edu/people/pah/
.. __ : https://amaral.northwestern.edu/blog/pyenv-tutorial
