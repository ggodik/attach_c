import psutil, getpass

try:
    import gdb
except:
    import tests.mock_gdb as gdb

import psutil
import getpass


def get_processes(user,keyword):
    ndx = 0
    procs = []
    for proc in psutil.process_iter():
        try:
            if user == proc.username and proc.exe.find(keyword) > -1:
                print '[%s]' % ndx, proc.pid, proc.username, proc.exe
                ndx += 1
                procs.append(proc)
        except psutil.AccessDenied, e:
            pass
    return procs

def choose_pid(procs,input_func=raw_input):
    if 0 == len(procs):
        print 'could not find that process for you'
        return None
    elif 1 == len(procs):
        return procs[0].pid
    else:
        pos = input_func('which item do you want? (-1 to cancel):')
        if "-1" == pos:
            return None
        return procs[int(pos)].pid
    

class Attach_C(gdb.Command):
    def __init__ (self):
        # should theoretically be COMMAND_USER
        # but that doesn't exist with out gdb/python lib
        super (Attach_C, self).__init__ ("attach_c", gdb.COMMAND_NONE) 
        self.user = getpass.getuser()

    def invoke(self,arg,from_tty):
        procs = get_processes(self.user,args)
        pid = choose_pid(procs)
        if pid:
            print 'attaching: ',pid
            gdb.execute('attach ' + pid,True)
