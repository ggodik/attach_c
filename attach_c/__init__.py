import psutil
import getpass


def command():
    from attach_c import Attach_C
    Attach_C()

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
    

