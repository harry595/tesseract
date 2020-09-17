from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import string
import os
import cv2

window=Tk()

window.title("IMG 텍스트 찾기")
window.geometry("283x105+820+460")
window.resizable(False, False)

memory=[]

path="./change"
file_list=os.listdir(path)

label=Label(window, text="찾을 단어", relief="solid",bg='mint cream')
label.grid(row=1,column=1,pady=5)

str=StringVar()
entry=Entry(window,width=30,bg='white',textvariable=str)
entry.grid(row=3,column=1,padx=5)

def clickMe():
    memory.append(str.get())
    print(memory)
    entry.delete(0,END)
    
def clickMe2():
    count=0
    for j in memory:
        for i in file_list:
            f = open("./change/"+i, 'r')
            print(i,j)
            if (re.findall(j,f.read()))!=[]:
                a = cv2.imread("./original/"+i[:len(i)-4])
                a = cv2.resize(a,(1200,1000))
                cv2.namedWindow(i[:len(i)-4], cv2.WINDOW_AUTOSIZE)
                cv2.imshow(i[:len(i)-4], a)
                cv2.waitKey()
                count=1
                f.close()
                break
            f.close()
        if(count==1):
            break
        
    if(count==0):
        messagebox.showinfo("해당 단어 검색 실패", memory)
    del memory[:]
    
btn2=Button(window,text="+",width=2,height=1,bg='white',command=clickMe)
btn2.grid(row=3,column=2,padx=0)

btn=Button(window,text="찾기",bg='mint cream',command=clickMe2)
btn.grid(row=5,column=1)

window.mainloop()


# messagebox.showinfo("Button Clicked", str.get())
