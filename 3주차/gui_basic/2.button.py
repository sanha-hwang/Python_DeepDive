from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

btn1 = Button(root, text='버튼1')
btn1.pack() # GUI창에 포함시키기

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 버튼 상대크기 조절 padx, pady
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3,  text="버튼4") # 고정 크기, 버튼 내용이 짤릴 수 있음
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text="버튼5")
btn5.pack()

photo = PhotoImage(file="3주차/gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()