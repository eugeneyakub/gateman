#!/usr/bin/env python

import logging
LOG_FILENAME = '/home/eugene/vzabote-xinetd.log'
logging.basicConfig(filename=LOG_FILENAME,
     level=logging.ERROR,
     )


def kill_chrome(file_path, elapsed_time, command_to_execute, command_arg):
    import os.path, time
    t1 = os.path.getmtime(file_path)
    t2 = time.time()
    
    if t2 - t1 > elapsed_time:
        from subprocess import call
        _t = time.strftime("%a, %d %b %Y %H:%M:%S +06", time.gmtime())
        logging.error('%s long delay. restart browser' % _t)
        call([command_to_execute, command_arg])

        
if __name__ == '__main__':
    file_path = '/home/eugene/t'
    elapsed_time = 2
    command_to_execute = 'touch'
    command_arg = '/home/eugene/t2'
    kill_chrome(file_path, elapsed_time, command_to_execute, command_arg)
    
    
