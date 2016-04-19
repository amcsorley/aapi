import os, errno

class mkDir:
    def __init__(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise


class forkIt:
    def __init__(self, it, pidfile):
        import sys, os 

        try: 
            pid = os.fork() 
            if pid > 0:
                sys.exit(0) 
        except OSError, e: 
            print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
            sys.exit(1)

        os.chdir("/") 
        os.setsid() 
        os.umask(0) 

        try: 
            pid = os.fork() 
            if pid > 0:
                #print "Daemon PID %d" % pid 
                if pidfile:
                    pf = open(pidfile, 'w')
                    pf.write(str(pid) + '\n')
                sys.exit(0) 
        except OSError, e: 
            print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
            sys.exit(1) 

        self.outfile = it()

    def get_outfile(self):
        return self.outfile

