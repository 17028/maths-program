import tkinter as tk
from tkinter.constants import BOTH, TRUE

#Main menu constants
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
testvar = "lessonInfo1"

#The main class, defining the root window
class Maths(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TitleScreen)
        self.title("L2 Calculus Program")

    #The frame switch method
    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        if self._frame.frametype == ("place"):
            self._frame.pack(expand=TRUE,fill="both")
        elif self._frame.frametype == ("grid"):
            self._frame.pack()
        else:
            print("error! no frametype specified")

#Title screen widgets
class TitleScreen(tk.Frame):
    def __init__(self,master):
        self.frametype = "grid"
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="Calculus",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,pady=100)
        tk.Button(self,text="Start",font=BUTTONFONT,bg="spring green3",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=lambda:master.switch_frame(LessonSelect)) .grid(column=1)
        tk.Label(self,text="",bg=BGCOLOUR) .grid(column=1)
        tk.Button(self,text="Quit",font=BUTTONFONT,bg="orange red2",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=quit) .grid(column=1,pady=30)

#Lesson select screen widgets
class LessonSelect(tk.Frame):
    def __init__(self,master):
        self.frametype = "grid"
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="Lessons",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,row=0)
        tk.Button(self,text='Differentiation;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo1),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=1,padx=BUTTONGAPX,pady=BUTTONGAPY)
        tk.Button(self,text='Differentiation;Gradients',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo2),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Differentiation;Tangents',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo3),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=2,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Differentiation;Δ Graident',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo4),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=2,pady=BUTTONGAPY)
        tk.Button(self,text='Differentiation;Min/Max',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo5),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=2)
        tk.Button(self,text='Integration;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo6),bg=INTBG,font = SMALLBUTTONFONT) .grid(column=2,row=2)
        tk.Button(self,text='Integration;Functions',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo7),bg=INTBG,font = SMALLBUTTONFONT) .grid(column=0,row=3)
        tk.Button(self,text='Integration;Kinematics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo8),bg= INTBG,font = SMALLBUTTONFONT) .grid(column=1,row=3,pady=BUTTONGAPY)
        tk.Button(self,text='Final Quiz',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo9),bg= "chocolate2",font = SMALLBUTTONFONT) .grid(column=2,row=3)
        tk.Button(self,text='Back',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(TitleScreen),bg="orange red2",font = SMALLBUTTONFONT) .grid(column=1,row=4,pady=BACKBUTTONGAPY)

#The template for lesson information screens
class LessonInfoTemplate(tk.Frame):
    def __init__(self,master):
        self.frametype = "place"
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        self.imagefile = tk.PhotoImage(file="1.png") 
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile      
        self.explanation = tk.Label(self,text="This lesson will explain to you the basics behind differentation, how to differentiate a quadratic and what differentiation actually does.",
        font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.pagenumber = tk.Label(self,text="Page 1/1",bg=BGCOLOUR,font=BUTTONFONT)
        self.pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        self.nextbutton = tk.Button(self,text="Next",bg="spring green3",font=BUTTONFONT)
        self.nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        self.backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT,command=lambda:master.switch_frame(LessonSelect))
        self.backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class LessonInfo1(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)

class LessonInfo2(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file="2.png")
        self.explanation.config(text="This lesson will explain to you what a gradient is, how differentiation relates to gradients and how to use differentiation to find a graident.")

class LessonInfo3(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file="3.png")
        self.explanation.config(text="This lesson will explain to you what a tangent is, what a normal is, and how to use the gradient to find the equation of a tangent.")

class LessonInfo4(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Δ Graident")
        self.imagefile.config(file="4.png")
        self.explanation.config(text="This lesson will show you how to find increasing and decreasing functions using the changes (Δ) in gradient.")

class LessonInfo5(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file="5.png")
        self.explanation.config(text="This lesson will explain to you what a minimum is, what a maximum is and how to use differentiation to find them.")

class LessonInfo6(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file="6.png")
        self.explanation.config(text="This lesson will show you the basics behind integration, what integration actually does and how to integrate a quadratic.")

class LessonInfo7(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file="7.png")
        self.explanation.config(text="This lesson will walk you through finding the original equation by using integration methods.")

class LessonInfo8(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file="8.png")
        self.explanation.config(text="This lesson will explain to you what kinematics are and how apply integration/differentiation techniques to them.")

class LessonInfo9(LessonInfoTemplate):
    def __init__(self,master):
        LessonInfoTemplate.__init__(self,master)
        self.title.config(text="Final Quiz")
        self.imagefile.config(file="shrek.gif",format="gif -index 1600")
        self.explanation.config(text="This is the final quiz! You should be comfortable with all of the topics and concepts covered in this program before you attempt this.")
        self.nextbutton.config(text="Start the quiz!")

#Defining the main subroutine
def main():
    app = Maths()
    app.geometry("1280x720")
    app.config(bg=BGCOLOUR)
    app.resizable(False, False)
    app.mainloop()

#Proper, conventional way to run main
if __name__ == '__main__':
    main()