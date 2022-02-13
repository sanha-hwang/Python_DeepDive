from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다.
checkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable = chkvar)
checkbox.select() # 자동 선택 처리
checkbox.deselect() # 선택 해제 처리
checkbox.pack()

chkvar2 = IntVar()
checkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable = chkvar2)
checkbox2.pack()

def btncmd():
   print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
   print(chkvar2.get()) # 0 : 체크 해제, 1 : 체크

bnt = Button(root, text="클릭", command=btncmd)
bnt.pack()

root.mainloop()