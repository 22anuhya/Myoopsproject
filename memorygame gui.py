from tkinter import *
from tkinter import messagebox
import time
import random
o=Tk()
o.title("Memory Puzzle Game")
o.geometry("600x500")
o['bg']="pink"
l=Label(o,text="MEMORY PUZZLE GAME",font=('bold'),bg='white')
l.place(x=160,y=20)
li=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
random.shuffle(li)
def reset():
    global chances,win,count,al,ad
    chances=0
    win=0
    al=[]
    ad={}
    random.shuffle(li)
    b1=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b1,0))
    b1.place(x=160,y=80)
    t1=time.time()
    b2=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b2,1))
    b2.place(x=200,y=80)
    b3=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b3,2))
    b3.place(x=240,y=80)
    b4=Button(o, text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b4,3))
    b4.place(x=280,y=80)
    b5=Button(o, text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b5,4))
    b5.place(x=160,y=120)
    b6=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b6,5))
    b6.place(x=200,y=120)
    b7=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b7,6))
    b7.place(x=240,y=120)
    b8=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b8,7))
    b8.place(x=280,y=120)
    b9=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b9,8))
    b9.place(x=160,y=160)
    b10=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b10,9))
    b10.place(x=200,y=160)
    b11=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b11,10))
    b11.place(x=240,y=160)
    b12=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b12,11))
    b12.place(x=280,y=160)
    b13=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b13,12))
    b13.place(x=160,y=200)
    b14=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b14,13))
    b14.place(x=200,y=200)
    b15=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b15,14))
    b15.place(x=240,y=200)
    b16=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b16,15))
    b16.place(x=280,y=200)
chances=0
win=0
count=0
al=[]
ad={}
def reset_button():
    for key in ad:
        key['text']=' '
def button_click(B,n):
    global count,al,ad,win,chances
    if B['text']==' ' and count<2:
        chances+=1
        #if clicks are 2 show numbers
        B['text']=li[n]
        #store the position of the card in another list to refer later
        al.append(n)
        #store that number inside the card to that paticular button in a dict
        ad[B]=li[n]
    #determine correct or not
    if len(al)==2:
        #if they both match
        if li[al[0]]==li[al[1]]:
            win+=2
            Label(o,text="MATCHED!",height=1,width=15).place(x=200,y=300)
            #disable the matched button
            for key in ad:#as ad have the buttons as its key's
                key['state']='disabled'
            #reset everything
            al=[]
            ad={}
        else:
            Label(o,text="NOT MATCHED!").place(x=200,y=300)
            #reset everything
            al=[]
            messagebox.showinfo("Oh no!","incorrect")
            #reset buttons
            reset_button()
            ad={}
    if chances==36:
        t2=time.time()
        messagebox.askokcancel("RESULT","""YOU LOST :(
        Time taken {}""".format(t2-t1))
        b=Button(o,text="PLAY AGAIN",bg="pale green",command=lambda: reset())
        b.place(x=360,y=180)        
    elif win==16:
        t2=time.time()
        messagebox.askokcancel("RESULT","""CONGRATULATIONS!!
        YOU WON THE GAME :)
        Time taken:"""+str(t2-t1))
        b=Button(o,text="PLAY AGAIN",bg="pale green",command=lambda: reset())
        b.place(x=360,y=180)
b1=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b1,0))
b1.place(x=160,y=80)
t1=time.time()
b2=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b2,1))
b2.place(x=200,y=80)
b3=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b3,2))
b3.place(x=240,y=80)
b4=Button(o, text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b4,3))
b4.place(x=280,y=80)
b5=Button(o, text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b5,4))
b5.place(x=160,y=120)
b6=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b6,5))
b6.place(x=200,y=120)
b7=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b7,6))
b7.place(x=240,y=120)
b8=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b8,7))
b8.place(x=280,y=120)
b9=Button(o,text=' ',height=2,width=4,bg='sky blue',command=lambda: button_click(b9,8))
b9.place(x=160,y=160)
b10=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b10,9))
b10.place(x=200,y=160)
b11=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b11,10))
b11.place(x=240,y=160)
b12=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b12,11))
b12.place(x=280,y=160)
b13=Button(o,text=' ', height=2,width=4,bg='sky blue',command=lambda: button_click(b13,12))
b13.place(x=160,y=200)
b14=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b14,13))
b14.place(x=200,y=200)
b15=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b15,14))
b15.place(x=240,y=200)
b16=Button(o,text=' ',height=2,width=4, bg='sky blue',command=lambda: button_click(b16,15))
b16.place(x=280,y=200)
