from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.minsize(600,600)
root.maxsize(600,600)

open_img = ImageTk.PhotoImage(Image.open("opened-folder.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("delete-sign.png"))

lf = Label(root,text="File name")
lf.place(relx=0.28,rely=0.03,anchor=CENTER)

ifn=Entry(root, text="File name")
ifn.place(relx=0.46, rely=0.03,anchor=CENTER)

my_text = Text(root,height=90, width=110)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

ob=Button(root,image=open_img, text="OpenFile", command=openFile)
ob.place(relx=0.05,rely=0.03,anchor=CENTER)
root.mainloop()

