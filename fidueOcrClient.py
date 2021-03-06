#!/usr/bin/env python
import datetime
import os
import time
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *
from os import *

from src.ImgOcr import parse


def findSubStr(substr, str, i):
    count = 0
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]
            i -= 1
            count = count + index + 1
    return count - 1

def getPath1():
    path_=path.normpath(askdirectory())
    path1.set(str(path_)+'\\')

def getPath2():
    path_=path.normpath(askdirectory())
    path2.set(str(path_)+'\\')

def getPath3():
    path_=path.normpath(askdirectory())
    path3.set(str(path_)+'\\')

def setHitInfo():
    nohitfiletxt = os.path.join(os.path.expanduser('~'),"Desktop/fidueOcr/nohitfiled.txt")
    if os.path.isfile(nohitfiletxt):
        hitinfo.set(str(nohitfiletxt))

def clientcheck(pdfpath,reportpath,ocrtxtpath):
    if pdfpath=='.\\' or pdfpath=='':
        showerror('Error message','The pdfpath  is incorrect. Please reselect')
        return
    if reportpath=='.\\' or reportpath=='':
        showerror('Error message','output report path is incorrect. Please reselect')
        return
    if ocrtxtpath=='.\\' or ocrtxtpath=='':
        showerror('Error message','ocrtxt is incorrect. Please reselect')
        return
    try:
        start_tm=datetime.datetime.now()
        parse(pdfpath, reportpath,ocrtxtpath)
        end_tm = datetime.datetime.now()
        # time.sleep(1)
        showinfo('results', 'OCR identification generation report completed!\n Time consuming:'+str((end_tm-start_tm).seconds))
        setHitInfo()
        os.system('pause')
    except Exception as e:
        showinfo('results','OCR identification generation report fail! errmsg:'+str(e))
root = Tk()
path1 =  StringVar()
path2 =  StringVar()
path3 =  StringVar()
hitinfo =  StringVar()
Label(root,text = 'PDF path:').grid(row = 0,column=0,padx=10,pady=10)
Entry(root,textvariable = path1).grid(row =0,column=1)
Button(root,text='browse',command = getPath1).grid(row=0,column=2)
Label(root,text = 'output report path:').grid(row = 1,column=0,padx=10,pady=10)
Entry(root,textvariable = path2).grid(row =1,column=1)
Button(root,text='browse',command = getPath2).grid(row=1,column=2)
Label(root,text = 'ocrtxt path:').grid(row = 2,column=0,padx=10,pady=10)
Entry(root,textvariable = path3).grid(row =2,column=1)
Button(root,text='browse',command = getPath3).grid(row=2,column=2)
Button(root,text='ocr-recognition',command = lambda: clientcheck(path1.get(),path2.get(),path3.get())).grid(row=3,column=1,padx=10,pady=10)
Label(root,text = 'no-hitfiledinfo:').grid(row = 4,column=0,padx=10,pady=10)
Entry(root,textvariable = hitinfo).grid(row =4,column=1)

# ???????????????????????????
root.title('pdf-ocr')
# ????????????????????????????????????
# ??????????????????????????????
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
dialog_width = 380
dialog_height = 260
# ????????????????????????????????????????????????????????????????????????
root.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height, (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))
root.grid
root.mainloop()
