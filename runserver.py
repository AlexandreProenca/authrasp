#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from bottle import debug, run
from project.sinc.sinc import Sinc
import logging

# Path to log file
dir_script = os.path.dirname(os.path.abspath(__file__))
auth = dir_script+'/auth-rasp.log'

# Log, formater and file
logging.basicConfig(format='[%(asctime)s] - %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename=auth)

#debug(True)
if __name__ == '__main__':
    Sinc.start()
    port = int(os.environ.get("PORT", 8080))
    logging.info("SERVER STARTED ON PORT [%d]" % port)
    run(app, reloader=False, host='0.0.0.0', port=port)


