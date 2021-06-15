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

# This is not very beautiful code, and most of it is repeated, but I couldn't be bothered to properly implement classes for the designing stage. 
class lessonInfo(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="lesson-1.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="This lesson will explain to you the basics behind differentation, how to differentiate a quadratic and what differentiation actually does.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 1/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",command=lambda:master.switch_frame(lesson1),font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class lesson1(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="lesson.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="When differentiating a quadratic, you look at each piece of the quadratic and 'take it down a level', so to speak. Refer to the above image, where x\u00B2 becomes 2x, 4x becomes 4 and 9 becomes 0.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 2/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",command=lambda:master.switch_frame(lesson2),font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",command=lambda:master.switch_frame(lessonInfo),font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class lesson2(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="lesson2.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="If x is to a power, the power 'drops down' (x is multiplied by the power) and one is subtracted from the power. If it is just x, then you remove the x and just leave its coefficient. If it is just a constant, then it becomes 0.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 3/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",command=lambda:master.switch_frame(lesson3),font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",command=lambda:master.switch_frame(lesson1),font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")
    
class lesson3(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="lesson3.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="By following these rules, you can see how we derive x\u00B2 + 4x + 9 to become 2x+4.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 4/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",command=lambda:master.switch_frame(lesson4),font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",command=lambda:master.switch_frame(lesson2),font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class lesson4(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="lesson4.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="Differentiating an equation finds its gradient, or its rate of change. Gradients will be explained later, but you need to know that to find the rate of change of an equation you have to differentiate it.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 5/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="Next",bg="spring green3",command=lambda:master.switch_frame(lesson5),font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back",bg="orange red2",command=lambda:master.switch_frame(lesson3),font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class lesson5(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file="parrot.png")      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile      
        explanation = tk.Label(self,text="Congratulations, you finished this lesson! You should now know how to differentiate a quadratic equation. Go back through the lesson if you're unsure on anything, otherwise take the quiz!",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        pagenumber = tk.Label(self,text="Page 6/6",bg=BGCOLOUR,font=BUTTONFONT)
        pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        nextbutton = tk.Button(self,text="To the quiz!",bg="spring green3",font=BUTTONFONT)
        nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back to start",bg="orange red2",command=lambda:master.switch_frame(lessonInfo),font=BUTTONFONT)
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