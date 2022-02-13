from os import lseek
import re
import sre_compile
import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill ="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = scrollbar.set())
for i in range(1,32): # 1~31일
    listbox.insert(END, str(i) +"일") # 1일,2일 ...
listbox.pack()

scrollbar.config(command=listbox.yview)
root.mainloop()