#!/usr/bin/env python

#SETTINGS
file_path = '/tmp/http_watchdog_touchplace'
elapsed_time = 60

#LOGGING
import logging
from logging.handlers import SysLogHandler
logHandler = SysLogHandler(address="/dev/log")
logging.getLogger().addHandler(logHandler)

import os.path, time
from subprocess import call

if __name__ == '__main__':

    if not os.path.exists(file_path) or time.time() - os.path.getmtime(file_path) > elapsed_time :
        logging.error('Watchdog: WEB app check dely is over %d seconds, restarting browser' % elapsed_time)
        if call(['killall', 'chrome']) != 0:
            logging.error('Watchdog: Error during browser restart process!')