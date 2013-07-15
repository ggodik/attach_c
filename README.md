attach_c
========

`attach_c` command for gdb. Use it to to attach to processes by name instead of pid

How To Install
---------
 - pip install git+git://github.com/ggodik/attach_c
 - or pip install setup.py if you have the files locally. also try running the tests
 - create a .gdbinit file in your root directory (~/) if you don't have one
 - if you cannot install into root, install locally and manually add that path to your sys.path for gdb
```
python
import sys
sys.path.append('path-to-where-you-installed-your-local-packages')
end
```
 - paste this into your .gdbinit file as well
``` 
python
from attach_c.command import Attach_C
Attach_C()
end
```

How to Use
----------
1. start gdb
2. issue `attach_c` optionally followed by process name
3. if process name is unique, gdb will attach. Show you a list otherwise. See examples below


Examples
--------

With no input - list your processes
```(gdb) attach_c
[0] 15428 george /home/user/george/bin/gdb
[1] 31292 george /bin/bash
[2] 32445 george /usr/bin/emacs-23.1
```

With a single matching process
```(gdb) attach_c emacs
[0] 32445 george /usr/bin/emacs-23.1
attaching:  32445
Attaching to process 32445
Reading symbols from /usr/bin/emacs-23.1...(no debugging symbols found)...done.
......
```

We must go deeper
```(gdb) attach_c gdb
[0] 26062 george /home/user/george/bin/gdb
attaching:  26062
Python Exception <class 'gdb.error'> I refuse to debug myself!:
Error occurred in Python command: I refuse to debug myself!
```