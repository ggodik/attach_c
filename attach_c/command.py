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
