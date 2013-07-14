attach_c
========

attach_c command for gdb


How To Install
---------

0. pip install git+git://github.com/ggodik/attach_c
1. or pip install setup.py if you have the files locally. also try running the tests
2. create a .gdbinit file in your root directory (~/) if you don't have one
3. paste this into your .gdbinit file

> python
> from attach_c import Attach_C
> Attach_C()
> end

4. Done

How to Use
----------
Start gdb from commandline or emacs or your favorite IDE and issue <b>attach_c</b> "process executable name". attach_c will attach to the process that matches that name OR give you a list of matching processes that belong to you and let you pick one