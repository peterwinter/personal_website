Coding in Emacs and PyCharm
###########################

:date: 2015-10-03 10:20
:modified: 2015-10-03 10:20
:tags: tools, emacs
:slug: emacs-and-pycharm
:authors: Peter B Winter
:summary: While I'm paid to do research, much of my daily activities involve programming. As such, I like to experiment with ways to make writing code simpler and faster by playing around with my development environment.

While I'm paid to do research, much of my daily activities involve programming. As such, I like to experiment with ways to make writing code simpler and faster by playing around with my development environment. The term 'development environment' is a precise way of saying 'what you see and what you can do' while writing code. Every development environment contains hundreds of little features designed to make your life easier, such as highlighting syntax errors, auto-completing common words, or coloring different code elements differently. Because every development environment has made different decisions about which features to implement, the subjective experience of writing python can feel completely different depending on what program you are using to write it.

My most recent experimentation with development environments has involved switching back and forth between Emacs, my default editor, and PyCharm, a newer integrated development environment (IDE). While sticking to one development environment can help you become more fluent in that environment (ie. learn the minimum amount of keystrokes needed to do useful commands), I found that switching back and forth helped me discover helpful features that I may never have stumbled on if I had stuck to using only one.

Before I go into what I like about Emacs and PyCharm, it may be helpful to explain what each of them are. By programming standards, Emacs is ancient. It has been around since the mid 1970s and has survived for so long because it is free, open-source and can be easily extended if you can code its particular dialect of lisp (elisp). An active community has written plug-ins that can make it do nearly anything you could want and for coding. The only problem is that barely any of the best features are built straight into Emacs.  For Emacs to become remotely efficient, there is a long list of hurdles to jump through. For example, If I wanted a specific feature (such as a python-specific auto-complete library) I would first need to find the right key-word that described the feature, find a suitable package, install it's dependencies, declare the paths, and resolve conflicts. Furthermore, since I never learned elisp, my .emacs file was (until recently) a horrible mash-up of code from colleages and various websites. It was a hacked together Frankenstein's monster. My recent discovery of the Emacs package manager called ‘el-get’, has simplified this process immensely, but for newbies, it will still be a complicated experience.

PyCharm, on the other hand, is polished and immediately useful. It has been written almost exclusively for python users and many helpful features immediately jump out when starting. It, however, is a large program. It loads slowly and there are so many features that after a couple months of using it, I've barely used any of the extensive lists of commands.

Now, it isn't easy to say if one development environment is better than the other. Each side has its' own advantages. If I had to pick my favorite features from each, I like Emacs' windowing system (to look at multiple files at once), and its' snippet features (for quickly pasting in generic, reusable pieces of code). On PyCharm, I like its' debugger, it's refactoring tools (renaming or moving modules/functions/variables and updating all occurrences), and its' hovering reminders and style advice.

I'll likely continue to switch back and forth between PyCharm and Emacs for a while. At this point, I can write new code faster in Emacs, but my refactoring is faster in PyCharm. If I had to recommend one for new programmers or people who haven't yet experienced a decked-out python development environment, I'd defiantly recommend PyCharm.
