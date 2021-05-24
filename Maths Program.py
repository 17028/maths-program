from tkinter import *

def raiseframe(frame):
    frame.tkraise()

TITLEFONT = "Consolas",100
BUTTONFONT = "Consolas",20
BGCOLOUR = "light grey"

class Title_screen():
    def __init__(self):
        Label(f1,text="Calculus",font=TITLEFONT,bg=BGCOLOUR) .pack()
        Button(f1,text="Start",font=BUTTONFONT,bg="spring green3",command=lambda:raiseframe(f2)) .pack()
        Label(f1,text="",bg=BGCOLOUR) .pack()
        Button(f1,text="Quit",font=BUTTONFONT,bg="orange red2",command=quit) .pack()

class Selection_screen():
    def __init__(self):
        Label(f2,text="whee",font=TITLEFONT) .grid(column=0,row=0)


def main():
    global f1,f2,root
    root = Tk()
    root.title("L2 Calculus Program")
    root.geometry("1280x720")
    root.resizable(False, False)
    stacking_frame = Frame()
    stacking_frame.pack()
    f1 = Frame(master=stacking_frame,bg=BGCOLOUR)
    f2 = Frame(master=stacking_frame,bg=BGCOLOUR)
    root.configure(bg=BGCOLOUR)
    f1.grid(column=0,row=0,sticky='news')
    f1.columnconfigure(0,weight=1)
    #f1.pack(expand=TRUE)
    f1.rowconfigure(0,weight=1)
    f2.grid(column=0,row=0,sticky='news')
    f2.columnconfigure(0,weight=1)
    f2.rowconfigure(0,weight=1)
    Title_screen()
    Selection_screen()
    f1.tkraise()
    root.mainloop()


main()

