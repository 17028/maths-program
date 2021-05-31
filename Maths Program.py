import tkinter as tk

BUTTONHEIGHT = 2
BUTTONWIDTH = 15
TITLEFONT = "Consolas",100
BUTTONFONT = "Arial",20
BGCOLOUR = "light grey"

#Selection Screen Constants
BUTTONGAPX = 50
BUTTONGAPY = 20
BACKBUTTONGAPY = 40
SSBUTTONWIDTH = 20
SSBUTTONHEIGHT = 4
DIFFBG = "spring green3"
INTBG = "royal blue2"
SMALLBUTTONFONT = "Arial"

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
        tk.Label(f2,text="Lessons",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,row=0)
        tk.Button(f2,text='Differentiation;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=1,padx=BUTTONGAPX,pady=BUTTONGAPY)
        tk.Button(f2,text='Differentiation;Gradients',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=1,padx=BUTTONGAPX)
        tk.Button(f2,text='Differentiation;Tangents',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=2,row=1,padx=BUTTONGAPX)
        tk.Button(f2,text='Differentiation;Δ Graident',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=2,pady=BUTTONGAPY)
        tk.Button(f2,text='Differentiation;Max/Min',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=2)
        tk.Button(f2,text='Integration;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=INTBG,font = SMALLBUTTONFONT) .grid(column=2,row=2)
        tk.Button(f2,text='Integration;Functions',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=INTBG,font = SMALLBUTTONFONT) .grid(column=0,row=3)
        tk.Button(f2,text='Integration;Kinematics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg= INTBG,font = SMALLBUTTONFONT) .grid(column=1,row=3,pady=BUTTONGAPY)
        tk.Button(f2,text='Final Quiz',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg= "chocolate2",font = SMALLBUTTONFONT) .grid(column=2,row=3)
        tk.Button(f2,text='Back',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg="orange red2",font = SMALLBUTTONFONT) .grid(column=1,row=4,pady=BACKBUTTONGAPY)

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