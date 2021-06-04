import tkinter as tk
from tkinter.constants import BOTH, TRUE

BUTTONHEIGHT = 2
BUTTONWIDTH = 15
TITLEFONT = "Consolas",100
HEADINGFONT = "Consolas",50
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

class Maths(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(lessonInfo)
        self.title("L2 Calculus Program")

    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=TRUE,fill="both")
    
    lessontext = "hello"


class lessonInfo(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="LeibnizNotation.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="This lesson will explain to you the basics behind differentation, how to differentiate a quadratic and what differentiation actually does.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 1/1",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")
    
    def create_function():
        print("hello")

def main():
    app = Maths()
    app.geometry("1280x720")
    app.config(bg=BGCOLOUR)
    app.resizable(False, False)
    app.mainloop()

if __name__ == '__main__':
    main()