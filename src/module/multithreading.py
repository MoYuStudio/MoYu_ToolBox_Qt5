
# -*- coding: UTF-8 -*-

import multiprocessing

class Multithreading:
    def __init__(self):
        pass
    def new_threading(self,func,args):
        p = multiprocessing.Process(target=func, args=())
        p.start()
        p.join()

if __name__ == "__main__":
    pass
