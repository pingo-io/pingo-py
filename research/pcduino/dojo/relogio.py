#!/usr/bin/env python
# coding: utf-8

import Tkinter
import time

relogio = Tkinter.Label()
relogio.pack()
relogio['text'] = time.strftime('%H:%M:%S')
relogio['font'] = 'Helvetica 96 bold'
relogio['fg'] = 'red'

def tic():
    agora = time.strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(100, tic)

tic()
relogio.mainloop()
