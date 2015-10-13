# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.nameInput = Entry(self)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput.pack()
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('消息', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('福利采集工具')
# 主消息循环:
app.mainloop()
