# This file is placed in the Public Domain.


import time


from los.utility import STARTTIME, elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))
