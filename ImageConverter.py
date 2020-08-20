from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os

from pilkit.processors import Thumbnail

root = Tk()
root.title("Image Converter for DATA DUCK")
root.geometry("400x400+50+50")
root.resizable(False,False)
openFile=""
saveDir=""


def Load():
    global openFile
    global label1
    openFile = filedialog.askopenfilename(initialdir='/', title="select file", )
    openPath = '파일:'+openFile
    label1.configure(text=openPath)

def Save():
    global saveDir
    global label2
    saveDir = filedialog.askdirectory( title="save file",)
    savePath = '저장경로:' + saveDir
    label2.configure(text=savePath)

def Convert():
    try:
        filename=os.path.basename(openFile)
        saveFile=saveDir+'/DD_'+filename+'.jpg'
        img = Image.open(os.path.abspath(openFile))
        garoPixel = int(garoEntry.get())
        seroPixel = int(seroEntry.get())
        processor= Thumbnail(garoPixel,seroPixel)
        img=processor.process(img)
        img=img.convert("RGB")
        print(saveFile)
        img.save(saveFile, quality=85)
        messagebox.showinfo(title="사장님 나빠요", message="변환완료!")
    except:
        messagebox.showinfo(title="다시 ㄱㄱ", message="오류!")




label1=Label(root,text="파일:",relief='solid', width=50, height=2) #tk변수에 문자열을 연결하여 label객체생성
label2=Label(root,text="저장경로:",relief='solid', width=50,height=2) #객체생성시 문자열을 지정
label1.pack()
label2.pack()
garo=Label(root, text="가로:")
garoEntry=Entry(root, bd=1, width=5)
sero=Label(root,text="세로:")
seroEntry=Entry(root, bd=1, width=5)
garo.pack()
garoEntry.pack()
sero.pack()
seroEntry.pack()
openbutton = Button(root,text='파일열기', overrelief="solid", width=15, height=2, command=Load, repeatdelay=1000, repeatinterval=100)
savebutton = Button(root, text='저장위치선택',overrelief="solid", width=15, height=2, command=Save, repeatdelay=1000, repeatinterval=100)
convertionbutton= Button(root, text='변환',overrelief="solid", width=15, height=2, command=Convert, repeatdelay=1000, repeatinterval=100)
openbutton.place(x=130,y=150)
savebutton.place(x=130,y=200)
convertionbutton.place(x=130,y=250)



root.mainloop()

