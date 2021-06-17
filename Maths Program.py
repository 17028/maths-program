import tkinter as tk
from tkinter.constants import BOTH, TRUE
import os

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

# Function to find the images in a filepath of my choosing
def get_image(image):
    # Gets the path of the program itself
    dir = os.path.dirname(__file__) 
    # Finding a filepath in the program's directory
    filename = os.path.join(dir, 'Images',str(image)) 
    return filename

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
        # Method for detecting what type of organization method the frame uses
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

#The template for lesson information screens, all lesson information screens will be LessonTemplate type objects
class LessonTemplate(tk.Frame):
    def __init__(self,master):
        self.frametype = "place"
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.title = tk.Label(self,text="",font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        self.imagefile = tk.PhotoImage(file="") 
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile      
        self.explanation = tk.Label(self,text="",font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.pagenumber = tk.Label(self,text="Page 1/1",bg=BGCOLOUR,font=BUTTONFONT)
        self.pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        self.nextbutton = tk.Button(self,text="Next",bg="spring green3",font=BUTTONFONT)
        self.nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        self.backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT,command=lambda:master.switch_frame(LessonSelect))
        self.backbutton.place(relx = 0.2,rely=0.9,anchor="center")

class LessonInfo1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("1.png"))
        self.pagenumber.config(text="1/6")
        self.explanation.config(text="This lesson will explain to you the basics behind differentation, how to differentiate a quadratic and what differentiation actually does.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("2.png"))
        self.explanation.config(text="This lesson will explain to you what a gradient is, how differentiation relates to gradients and how to use differentiation to find a graident.")

class LessonInfo3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("3.png"))
        self.explanation.config(text="This lesson will explain to you what a tangent is, what a normal is, and how to use the gradient to find the equation of a tangent.")

class LessonInfo4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Δ Graident")
        self.imagefile.config(file=get_image("4.png"))
        self.explanation.config(text="This lesson will show you how to find increasing and decreasing functions using the changes (Δ) in gradient.")

class LessonInfo5(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("5.png"))
        self.explanation.config(text="This lesson will explain to you what a minimum is, what a maximum is and how to use differentiation to find them.")

class LessonInfo6(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("6.png"))
        self.explanation.config(text="This lesson will show you the basics behind integration, what integration actually does and how to integrate a quadratic.")

class LessonInfo7(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file=get_image("7.png"))
        self.explanation.config(text="This lesson will walk you through finding the original equation by using integration methods.")

class LessonInfo8(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file=get_image("8.png"))
        self.explanation.config(text="This lesson will explain to you what kinematics are and how apply integration/differentiation techniques to them.")

class LessonInfo9(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Final Quiz")
        self.imagefile.config(file=get_image("shrek.gif"),format="gif -index 1600")
        self.explanation.config(text="This is the final quiz! You should be comfortable with all of the topics and concepts covered in this program before you attempt this.")
        self.nextbutton.config(text="Start the quiz!")

class Lesson1P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson.png"))
        self.pagenumber.config(text="2/6")
        self.explanation.config(text="When differentiating a quadratic, you look at each piece of the quadratic and 'take it down a level', so to speak. Refer to the above image, where x\u00B2 becomes 2x, 4x becomes 4 and 9 becomes 0.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo1))

class Lesson1P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson2.png"))
        self.pagenumber.config(text="3/6")
        self.explanation.config(text="If x is to a power, the power 'drops down' (x is multiplied by the power) and one is subtracted from the power. If it is just x, then you remove the x and just leave its coefficient. If it is just a constant, then it becomes 0.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P1))

class Lesson1P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson3.png"))
        self.pagenumber.config(text="4/6")
        self.explanation.config(text="By following these rules, you can see how we derive x\u00B2 + 4x + 9 to become 2x+4.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P2))

class Lesson1P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson4.png"))
        self.pagenumber.config(text="5/6")
        self.explanation.config(text="Differentiating an equation finds its gradient, or its Rate of Change. Gradients will be explained later, but you need to know that to find the rate of change of an equation you have to differentiate it.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P5))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P3))

class Lesson1P5(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("parrot.png"))
        self.pagenumber.config(text="6/6")
        self.explanation.config(text="Congratulations, you finished this lesson! You should now know how to differentiate a quadratic equation. Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command="")
        self.backbutton.config(text="Back to Start",command=lambda:master.switch_frame(LessonInfo1))

#Defining the main subroutine
def main():
    app = Maths()
    app.geometry("1280x720")
    app.config(bg=BGCOLOUR)
    app.resizable(False, False)
    app.mainloop()

#Proper, conventional way to run main, prevents main accidentally if the program is ever called
if __name__ == '__main__':
    main()