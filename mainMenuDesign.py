from tkinter import *

def raiseframe(frame):
    frame.tkraise()

TITLEFONT = "Consolas",100
BUTTONFONT = "Consolas",20
BGCOLOUR = "light grey"

class Title_screen:
    def __init__(self):
        Label(f1,text="Calculus",font=TITLEFONT,bg=BGCOLOUR) .pack()
        Button(f1,text="Start",font=BUTTONFONT,bg="spring green3",command=raiseframe(f2)) .pack()
        Label(f1,text="",bg=BGCOLOUR).pack()
        Button(f1,text="Quit",font=BUTTONFONT,bg="orange red2",command=quit) .pack()

def main():
    global f1,f2,root
    root = Tk()
    root.title("L2 Calculus Program")
    root.geometry("1280x720")
    root.resizable(False, False)
    f1 = Frame(root,bg=BGCOLOUR)
    f2 = Frame(root,bg=BGCOLOUR)
    root.configure(bg=BGCOLOUR)
    f1.pack(side='top',expand='true',fill="y")
    raiseframe(f1)
main()
Title_screen()
mainloop()