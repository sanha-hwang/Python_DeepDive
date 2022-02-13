from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창크기 변경 불가), default는 가능함

listbox = Listbox(root, selectmode="extended", height = 0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제
#   listbox.delete(0) # 0 : 맨 앞 항목을 삭제,  END : 맨 뒤에 항목을 삭제

    # 갯수 확인
    # print("리스트에는",listbox.size(),"개가 있어요")

    # 항목 확인
    print("1번째 부터 3번째 까지의 항목: ", listbox.get(0, 2))

    # 선택된 항목 확인 ( 위치로 반환 ex.(1,2,3))
    print("선택된 항목 : ", listbox.curselection())

    
bnt = Button(root, text="클릭", command=btncmd)
bnt.pack()

root.mainloop()