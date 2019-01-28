#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
# from tkinter.messagebox import *
import tkinter.messagebox

import requests

url = 'https://api.cloudcone.com/api/v1/compute/id/'
headers = {'App-Secret': 'yoursec', 'Hash': 'yourhash'}
root = tk.Tk()
root.title("Cloudcone 一键开关机")
# 设置窗口的大小宽x高+偏移量
root.geometry('300x150+500+200')


def boot():
    b = requests.get(url+'boot', headers=headers)
    tkinter.messagebox.showinfo('Info', b.json()['message'])


def shutdown():
    s = requests.get(url+'shutdown', headers=headers)
    tkinter.messagebox.showinfo('Info', s.json()['message'])


def check():
    status = requests.get(url+'status', headers=headers).json()['__data']['status']
    if status == 'offline':
        fg = 'red'
    else:
        fg = 'green'
    w.config(text=status, fg='dark '+fg, bg='light yellow')


w = tk.Label(root)
check()
w.pack()

btn1 = tk.Button(root, text='Boot', width=25, fg='green', command=boot)
btn1.pack()

btn2 = tk.Button(root, text='Shutdown', width=25, fg='red', command=shutdown)
btn2.pack()

btn3 = tk.Button(root, text='Check Status', width=25, command=check)
btn3.pack()

root.mainloop()
