from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="3주차/gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # 함수가 끝나도 안사라지게 전역변수로 선언
    photo2 = PhotoImage(file="3주차/gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()
root.mainloop()