#!/usr/bin/env python



def kill_chrome(file_path, elapsed_time, command_to_execute, command_arg):
    import os.path, time
    t1 = os.path.getmtime(file_path)
    t2 = time.time()
    
    if t2 - t1 > elapsed_time:
        from subprocess import call
        call([command_to_execute, command_arg])
        
if __name__ == '__main__':
    file_path = '/home/eugene/t'
    elapsed_time = 25
    command_to_execute = 'touch'
    command_arg = '/home/eugene/t2'
    kill_chrome(file_path, elapsed_time, command_to_execute, command_arg)
    
    
