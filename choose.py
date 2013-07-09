#class AttachChoose(gdb.Command):
#        def __init__(self):
#                super (AttachChoose, self).__init__ ("AttachChoose", gdb.COMMAND_NONE) 
#        def invoke(self,arg,from_tty):
#                import os,getpass       
              
#                keyword = raw_input('search for process keyword:')

#                cmd = 'ps aux | grep -v "grep" | grep %s | grep fdsa_fire_cl_worker | perl -ane "print @F[1]"' % getpass.getuser()
#                for x,line in enumerate( os.popen(cmd).readlines() ) :
#                        print x,line


import psutil, getpass
try:
    import gdb
except:
    import choose as gdb
    class MockCommand:
        def execute(self,arg):
            print arg
    gdb.Command = MockCommand
    gdb.COMMAND_NONE = 17

import psutil, getpass

class Attach_C(gdb.Command):
    def __init__ (self):
        # should theoretically be COMMAND_USER
        # but that doesn't exist with out gdb/python lib
        super (Attach_C, self).__init__ ("attach_c", gdb.COMMAND_NONE) 
        self.user = getpass.getuser()

    def invoke(self,arg,from_tty):
        ndx = 0
        procs = []
        for proc in psutil.process_iter():
            try:
                if self.user == proc.username and proc.exe.find(arg) > -1:
                    print '[%s]' % ndx, proc.pid, proc.username, proc.exe
                    ndx += 1
                    procs.append(proc)
            except psutil.AccessDenied, e:
                pass

        pid = None
        if 0 == len(procs):
            print 'could not find that process for you'
            return
        elif 1 == len(procs):
            pid = procs[0].pid
        else:
            pos = raw_input('which item do you want? (-1 to cancel):')
            if "-1" == pos:
              return
            pid = procs[int(pos)].pid

        print 'attaching: ',pid
        gdb.execute('attach ' + pid,True)
