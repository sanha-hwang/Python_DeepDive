import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

# progressbar = ttk.Progressbar(root, maximum = 100, mode="determinate")
# progressbar.start(5) # 10 ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1~100
            time.sleep(0.01) # 0.01초 대기
            p_var2.set(i) # progress bar의 값 설정
            progressbar2.update() # ui 업데이트
            print(p_var2.get())
   #  progressbar2.start() # 작동중지


bnt = Button(root, text="시작", command=btncmd2)
bnt.pack()

root.mainloop()