import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

values= [str(i)+"일" for i in range(1,32)] # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height = 5, values= values)
combobox.pack()
combobox.set("카드 결제일") # 최초목록 제목 설정

readonly_combobox = ttk.Combobox(root, height = 5, values= values, state="readonly")
readonly_combobox.current(0) # 0번쨰 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
   print(combobox.get())
   print(readonly_combobox.get())

bnt = Button(root, text="클릭", command=btncmd)
bnt.pack()

root.mainloop()