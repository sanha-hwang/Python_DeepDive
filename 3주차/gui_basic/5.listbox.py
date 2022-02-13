from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"글자를 입력하세요.")

e = Entry(root, width=30) # 한줄만 입력, enter가 안됨
e.pack()
e.insert(0,"한 줄만입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
bnt = Button(root, text="클릭", command=btncmd)
bnt.pack()

root.mainloop()