import tkinter as tk

BUTTONHEIGHT = 2
BUTTONWIDTH = 15
TITLEFONT = "Consolas",100
BUTTONFONT = "Consolas",20
BGCOLOUR = "light grey"

def raiseframe(frame):
    frame.tkraise()

class Title_screen():
    def __init__(self):
        tk.Label(f1,text="Calculus",font=TITLEFONT,bg=BGCOLOUR) .grid(pady=100)
        tk.Button(f1,text="Start",font=BUTTONFONT,bg="spring green3",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=lambda:raiseframe(f2)) .grid()
        tk.Label(f1,text="",bg=BGCOLOUR) .grid()
        tk.Button(f1,text="Quit",font=BUTTONFONT,bg="orange red2",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=quit) .grid(pady=30)

class Selection_screen():
    def __init__(self):
        tk.Label(f2,text="this is page 2",font=TITLEFONT) .grid(column=0,row=0)


def main():
    global f1,f2,root
    root = tk.Tk()
    root.title("L2 Calculus Program")
    root.geometry("1280x720")
    root.resizable(False, False)
    root.configure(bg=BGCOLOUR)
    stacking_frame = tk.Frame()
    stacking_frame.pack()
    f1 = tk.Frame(master=stacking_frame,bg=BGCOLOUR)
    f2 = tk.Frame(master=stacking_frame,bg=BGCOLOUR)
    for frame in (f1,f2):
        frame.grid(column=0,row=0,sticky='news')
    f1.grid(column=0,row=0,sticky='news')
    f1.columnconfigure(0,weight=1)
    f1.rowconfigure(0,weight=1)
    f2.grid(column=0,row=0,sticky='news')
    f2.columnconfigure(0,weight=1)
    f2.rowconfigure(0,weight=1)
    Title_screen()
    Selection_screen()
    f1.tkraise()
    root.mainloop()

if __name__ == '__main__':
    main()