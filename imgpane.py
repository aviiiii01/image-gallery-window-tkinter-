from tkinter import *
from PIL import ImageTk,Image
root = Tk()

#or title on the window!!
root.title('This is me and tkinter')


#for favicon
root.iconbitmap('D:/docs/class python/DevFolio/static/assets/img/favicon.ico')


img1=Image.open("book1.jpg")
img1 = img1.resize((600, 400), Image.Resampling.LANCZOS)
img1=ImageTk.PhotoImage(img1)

img2=Image.open("book2.jpg")
img2 = img2.resize((600, 400), Image.Resampling.LANCZOS)
img2=ImageTk.PhotoImage(img2)

img3=Image.open("book3.jpg")
img3 = img3.resize((600, 400), Image.Resampling.LANCZOS)
img3=ImageTk.PhotoImage(img3)

img4=Image.open("book4.jpg")
img4 = img4.resize((600, 400), Image.Resampling.LANCZOS)
img4=ImageTk.PhotoImage(img4)

img5=Image.open("book5.jpg")
img5 = img5.resize((600, 400), Image.Resampling.LANCZOS)
img5=ImageTk.PhotoImage(img5)



label=Label(image=img1)
label.grid(row=0,column=0,columnspan=5)

im=[img1,img2,img3,img4,img5]

label3=Label(root,text='Image Sliding View',fg='white',bg='black',font=('Arial',20),width=35)
label3.grid(row=0,column=2,pady=10)

x=0
def next():
    global label
    global x
    global button_next
    if x<len(im)-1:
        x=x+1
        label.grid_forget()
        label=Label(image=im[x])
        label.grid(row=1,column=0,columnspan=5)
    else:
        label1=Label(root,text='error 404:- no more forwordsss',padx=30,pady=40)
        label1.grid(row=1,column=2)
        button_next=Button(root,state=DISABLED)

def back():
    global label
    global x
    global button_back
    if x>0:
        x=x-1
        label.grid_forget()
        label=Label(image=im[x])
        label.grid(row=1,column=0,columnspan=5)
    else:

        label1=Label(root,text='error 404:- no more backssss',padx=30,pady=40)
        label1.grid(row=1,column=2)
        button_back=Button(root,state=DISABLED)


button_next=Button(root,text='>>',pady=10,width=10,borderwidth=5,command=next)
button_exit=Button(root,text='Exit',width=20,pady=10,command=root.quit)
button_back=Button(root,text='<<',pady=10,width=10,borderwidth=5,command=back)









button_exit.grid(row=4,column=2,padx=10,pady=20)
button_back.grid(row=4,column=0,padx=20)
button_next.grid(row=4,column=3,padx=20)    



root.mainloop()