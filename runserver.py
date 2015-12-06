#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app
from bottle import debug, run
from project.sinc.sinc import Sinc
debug(True)
if __name__ == '__main__':
    Sinc.start()
    port = int(os.environ.get("PORT", 8080))
    run(app, reloader=True, host='0.0.0.0', port=port)
