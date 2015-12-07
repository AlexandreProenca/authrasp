#!/usr/bin/python
# -*- coding: utf8 -*-
__author__ = 'cleytonpedroza'

from threading import Thread
import time
import os
import subprocess

class ThConection(Thread):
    def __init__(self, _callback):
        Thread.__init__(self)
        self.callback = _callback
        self.loop = True

    def run(self):
        while self.loop:
            time.sleep(0.05)
            self.callback()


class Sinc():

    thread_loop = None
    start_time = None
    seconds = 0

    tasks =[]

    @staticmethod
    def start():
        Sinc.start_time = time.time()
        Sinc.thread_lopp = ThConection(Sinc.clock_pulse)
        Sinc.thread_lopp.start()

    @staticmethod
    def clock_pulse():
        new_value = int(time.time() - Sinc.start_time)
        if Sinc.seconds != new_value:
            Sinc.seconds = new_value
        Sinc.process()

    @staticmethod
    def insert(info):
        info['start'] = Sinc.seconds
        Sinc.tasks.append(info)

    @staticmethod
    def process():
        for el in Sinc.tasks:
            if Sinc.seconds >= (int(el['start']) + int(el['delta'])):
                # print 'el:', el, Sinc.seconds
                Sinc.tasks.remove(el)
                return_code = subprocess.call(el['path'], shell=True)
                #print return_code


if __name__ == "__main__":

    Sinc.start()

    while 1:
        a = raw_input('>')
        if a.lower() in ['bye', 'sair', 'quit', 'exit', 'cu']:
            os._exit(0)
        if a.lower() in ['tasks']:
            print 'tasks:', Sinc.tasks
        if a.lower() in ['g30']:
             Sinc.insert({'delta': 30, 'info': 'sh de 30 segundos', 'path': './list.sh' })
        if a.lower() in ['g0']:
             Sinc.insert({'delta': 0, 'info': 'sh de 1 segundo', 'path': './run.sh'})

