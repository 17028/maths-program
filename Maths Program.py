import tkinter as tk
from tkinter.constants import BOTH, TRUE
import os

# Main menu constants
BUTTONHEIGHT = 2
BUTTONWIDTH = 15
TITLEFONT = "Consolas",100
HEADINGFONT = "Consolas",50
BUTTONFONT = "Arial",20
BGCOLOUR = "light grey"

# Selection Screen Constants
BUTTONGAPX = 50
BUTTONGAPY = 20
BACKBUTTONGAPY = 40
SSBUTTONWIDTH = 20
SSBUTTONHEIGHT = 4
DIFFBG = "spring green3"
INTBG = "royal blue2"
SMALLBUTTONFONT = "Arial"

# High score file
HIGHSCOREFILE = "values.txt"

# Images directory - name of the folder in the root path of the program
IMAGEDIRECTORY = "Images"

# Function to find the images in a filepath of my choosing
# This allows assets to be stored in a folder instead of the program's root directory
# This allows me to simply specify the program
def get_image(image):
    # Gets the path of the program itself
    dir = os.path.dirname(__file__) 
    # Finding a filepath in the program's directory
    filename = os.path.join(dir, IMAGEDIRECTORY,str(image)) 
    return filename    

#T he main class, defining the root window
class Maths(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(TitleScreen)
        self.title("NCEA L2 Calculus")

    # The frame switch method
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
            # This is more for debugging than anything else
            print("error! no frametype specified")

# Title screen widgets - this class is the whole of the page
# No template was used because there is only one of this type of page
class TitleScreen(tk.Frame):
    def __init__(self,master):
        self.frametype = "grid"
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="NCEA L2 Calculus",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,pady=100)
        tk.Button(self,text="Start",font=BUTTONFONT,bg="spring green3",width = BUTTONWIDTH,
            height = BUTTONHEIGHT,command=lambda:master.switch_frame(LessonSelect)) .grid(column=1)
        tk.Label(self,text="",bg=BGCOLOUR) .grid(column=1)
        tk.Button(self,text="Quit",font=BUTTONFONT,bg="orange red2",width = BUTTONWIDTH,
            height = BUTTONHEIGHT,command=quit) .grid(column=1,pady=30)

# Lesson select screen widgets - again, no template because there is only one of this type of page
class LessonSelect(tk.Frame):
    def __init__(self,master):
        self.frametype = "grid"
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="Lessons",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,row=0)
        tk.Button(self,text='Lesson 1\n\nDifferentiation;Basics',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo1),
            bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=1,padx=BUTTONGAPX,pady=BUTTONGAPY)
        tk.Button(self,text='Lesson 2\n\nDifferentiation;Gradients',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo2),
            bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Lesson 3\n\nDifferentiation;Tangents',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo3),
            bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=2,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Lesson 4\n\nDifferentiation;Inc/Dec',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo4),
            bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=2,pady=BUTTONGAPY)
        tk.Button(self,text='Lesson 5\n\nDifferentiation;Min/Max',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo5),
            bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=2)
        tk.Button(self,text='Lesson 6\n\nIntegration;Basics',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo6),
            bg=INTBG,font = SMALLBUTTONFONT) .grid(column=2,row=2)
        tk.Button(self,text='Lesson 7\n\nIntegration;Functions',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo7),
            bg=INTBG,font = SMALLBUTTONFONT) .grid(column=0,row=3)
        tk.Button(self,text='Lesson 8\n\nIntegration;Kinematics',width=SSBUTTONWIDTH,
            height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(LessonInfo8),
            bg= INTBG,font = SMALLBUTTONFONT) .grid(column=1,row=3,pady=BUTTONGAPY)
        tk.Button(self,text='Final Quiz',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,
            command=lambda:master.switch_frame(LessonInfo9),
            bg= "chocolate2",font = SMALLBUTTONFONT) .grid(column=2,row=3)
        tk.Button(self,text='Back',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,
            command=lambda:master.switch_frame(TitleScreen),
            bg="orange red2",font = SMALLBUTTONFONT) .grid(column=1,row=4,pady=BACKBUTTONGAPY)

# The template for lesson information screens
# All lesson information screens will be LessonTemplate type objects
class LessonTemplate(tk.Frame):
    # Defining everything to run when this class is initalized
    def __init__(self,master):
        # Defining frametype for the frame switch method
        self.frametype = "place"
        tk.Frame.__init__(self,master)
        # Setting the background colour to be a constant varialbe  
        self.config(bg=BGCOLOUR)
        # Constant variables for title font and background colour
        # This is to ensure consistency and easy editing in the future
        # Note that the title is blank, as this is a template
        # The title will vary across lessons, so there is no point in setting a "default" title
        self.title = tk.Label(self,text="",font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        # Again, blank image as image will vary across every single lesson
        self.imagefile = tk.PhotoImage(file="") 
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile
        # Blank explanation because of variation, no point in a default      
        self.explanation = tk.Label(self,text="",font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.pagenumber = tk.Label(self,text="Page 1/1",bg=BGCOLOUR,font=BUTTONFONT)
        self.pagenumber.place(relx = 0.5,rely=0.9,anchor="center")
        self.nextbutton = tk.Button(self,text="Next",bg="spring green3",font=BUTTONFONT)
        self.nextbutton.place(relx = 0.8,rely=0.9,anchor="center")
        self.backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT)
        self.backbutton.place(relx = 0.2,rely=0.9,anchor="center")

#############################################################

#Lesson information classes, where each class is an instance of the template class defined above
class LessonInfo1(LessonTemplate):
    # Everything is run upon initialization of the class
    def __init__(self,master):
        # Initalization of the template is run first
        # This is so that each lesson has all of the widgets/objects present in the parent class
        LessonTemplate.__init__(self,master)
        # Setting the title
        self.title.config(text="Differentiation;Basics")
        # Setting the image file - you can see the get_image function at work here
        self.imagefile.config(file=get_image("1.png"))
        # Setting the page number
        self.pagenumber.config(text="1/6")
        # Setting the explanation
        self.explanation.config(text=
            "This lesson will explain to you the basics behind differentation," + 
            " how to differentiate a quadratic and what differentiation actually does.")
        # Configuring the back and next buttons to go to the correct pages
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("2.png"))
        self.pagenumber.config(text="1/5")
        self.explanation.config(text=
            "This lesson will explain to you what a gradient is, " +
            "how differentiation relates to gradients " + 
            "and how to use differentiation to find a gradient.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson2P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("3.png"))
        self.pagenumber.config(text="1/8")
        self.explanation.config(text=
            "This lesson will explain to you what a tangent is, " + 
            "what a normal is, and how to use the gradient to find the equation of a tangent.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Increase/Decrease")
        self.imagefile.config(file=get_image("4.png"))
        self.pagenumber.config(text="1/5")
        self.explanation.config(text=
            "This lesson will show you how determine whether a function " + 
            "is increasing or decreasing via differentiation methods.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson4P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo5(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("5.png"))
        self.pagenumber.config(text="1/5")
        self.explanation.config(text=
            "This lesson will explain to you what a minimum is, " + 
            "what a maximum is and how to use differentiation to find them.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson5P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo6(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("6.png"))
        self.pagenumber.config(text="1/5")
        self.explanation.config(text=
            "This lesson will show you the basics behind integration, " + 
            "what integration actually does and how to integrate a quadratic.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson6P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo7(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file=get_image("7.png"))
        self.pagenumber.config(text="1/4")
        self.explanation.config(text=
            "This lesson will walk you through finding " + 
            "the original equation by using integration methods.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson7P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo8(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file=get_image("8.png"))
        self.pagenumber.config(text="1/5")
        self.explanation.config(text=
            "This lesson will explain to you what kinematics are " + 
            "and how apply integration/differentiation techniques to them.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson8P1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))

class LessonInfo9(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Final Quiz")
        self.imagefile.config(file=get_image("finalquiz.png"))
        # This extra bit of code detects displays the user's high score and displays it
        with open(get_image(HIGHSCOREFILE),"r+") as TXT_FILE:
            self.highscore = TXT_FILE.readline()
        self.explanation.config(text=
            "This is the final quiz! You should be comfortable with " + 
            "all of the topics and concepts covered in this program before you attempt this. " + 
            "\nYour current high score is: " + str(self.highscore) + ".")
        # This if/else statement checks if the user's high score is above 0
        # If it is, then it offers the user the choice of resetting their high score back to 0
        if int(self.highscore) == 0:
            self.pagenumber.config(text="1/1")
        elif int(self.highscore) > 0:
            self.pagenumber.config(text="")
            self.resetbutton = tk.Button(self,text="Reset high score",bg="spring green3",
                font=BUTTONFONT,command=lambda:self.ResetScore())
            self.resetbutton.place(relx = 0.5,rely=0.9,anchor="center")
        self.nextbutton.config(text="Start the quiz!",
            command=lambda:master.switch_frame(FinalQuizP1))
        self.backbutton.config(command=lambda:master.switch_frame(LessonSelect))
    
    # This method is used for the LessonInfo9 page to reset the highscore before taking the quiz
    # This was initially a subroutine under the LessonTemplate class, but it was only used here
    # Because of this I moved it here, where it was actually used 
    def ResetScore(self):
        # Sets the high score as "0" in the highscore file
        with open(get_image(HIGHSCOREFILE),"r+") as TXT_FILE:
            TXT_FILE.write("0")
        # Changes the name of the button to say "reset to 0"
        self.resetbutton.config(text="Reset to 0!",command="")
        # Refreshing the explanation text to display the updated high score (0)
        with open(get_image(HIGHSCOREFILE),"r+") as TXT_FILE:
            self.highscore = TXT_FILE.readline()
        self.explanation.config(text=
            "This is the final quiz! You should be comfortable with " + 
            "all of the topics and concepts covered in this program before you attempt this. " + 
            "\nYour current high score is: " + str(self.highscore) + ".")
        # After 2 seconds, the button is destroyed and replaced with the normal pagenumber display
        self.after(2000,lambda:self.resetbutton.destroy())
        self.after(2000,lambda:self.pagenumber.config(text="1/1"))


#############################################################
# Lesson classes, again where each class is an instance of the template class
# These don't differ greatly from the lesson template pages

class Lesson1P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson1 1.png"))
        self.pagenumber.config(text="2/6")
        self.explanation.config(text=
            "When differentiating a quadratic, you look at each piece of the quadratic " + 
            "and 'take it down a level', so to speak. Refer to the above image, " + 
            "where x\u00B2 becomes 2x, 4x becomes 4 and 9 becomes 0.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo1))

class Lesson1P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson1 2.png"))
        self.pagenumber.config(text="3/6")
        self.explanation.config(text=
            "If x is to a power, the power 'drops down' (x is multiplied by the power) " + 
            "and one is subtracted from the power. If it is just x, " + 
            "then you remove the x and just leave its coefficient. " + 
            "If it is just a constant, then it becomes 0.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P1))

class Lesson1P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson1 3.png"))
        self.pagenumber.config(text="4/6")
        self.explanation.config(text=
            "By following these rules, you can see how we derive x\u00B2 + 4x + 9 to become 2x+4.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P2))

class Lesson1P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("lesson1 4.png"))
        self.pagenumber.config(text="5/6")
        self.explanation.config(text=
            "Differentiating an equation finds its gradient, or its Rate of Change. " + 
            "Gradients will be explained later, but you need to know that to find " + 
            "the rate of change of an equation you have to differentiate it. " + 
            "Also, take note of the notation f'(x), which means the derivative of x.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson1P5))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson1P3))

class Lesson1P5(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Basics")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="6/6")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! " +
            "You should now know how to differentiate a quadratic equation. " + 
            "Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz1P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson2P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("lesson2 1.png"))
        self.pagenumber.config(text="2/5")
        self.explanation.config(text=
            "The graident of an equation is the rate of change for that equation. " + 
            "Some equations have a constant rate of change (in the form y = mx + c), " + 
            "however quadratics have a constantly changing graident.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson2P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo2))

class Lesson2P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("lesson2 2.png"))
        self.pagenumber.config(text="3/5")
        self.explanation.config(text=
            "To find the gradient of an equation, you differentiate that equation " + 
            "(like you learnt to do in the previous lesson).")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson2P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson2P1))

class Lesson2P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("lesson2 3.png"))
        self.pagenumber.config(text="4/5")
        self.explanation.config(text=
            "To find the gradient at a certain x value, " + 
            "substitute in that x value into the gradient/differentiated equation.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson2P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson2P2))

class Lesson2P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Gradients")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="5/5")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now " + 
            "know how to find the gradient of a quadratic equation at a certain point. " + 
            "Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz2P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson3P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 1.png"))
        self.pagenumber.config(text="2/8")
        self.explanation.config(text=
            "A tangent line to a given quadratic equation is a line " + 
            "that has the same gradient as the point of the curve it touches.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo3))

class Lesson3P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 2.png"))
        self.pagenumber.config(text="3/8")
        self.explanation.config(text=
            "A normal line is a line that is perpendicular " + 
            "to the tangent line (i.e it is rotated 90 degrees).")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson3P1))

class Lesson3P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 3.png"))
        self.pagenumber.config(text="4/8")
        self.explanation.config(text=
            "To find the equation of a tangent to a curve at a specific x value, " + 
            "you first find the gradient of the curve at that x value. " + 
            "We call the gradient value m and the x value a.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson3P2))

class Lesson3P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 4.png"))
        self.pagenumber.config(text="5/8")
        self.explanation.config(text=
            "Then, substitute the x value back into the original equation " + 
            "to find its corresponding y value. We call this value b.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P5))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson3P3))

class Lesson3P5(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 5.png"))
        self.pagenumber.config(text="6/8")
        self.explanation.config(text=
            "Finally, substitute a, b and m into the equation y - b = m(x - a), " + 
            "and rearrange to find the equation of the tangent.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P6))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson3P4))

class Lesson3P6(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("lesson3 6.png"))
        self.pagenumber.config(text="7/8")
        self.explanation.config(text=
            "To find the normal line of a tangent, go through the same procedure " + 
            "as finding a tangent, except use the equation y - b = -1/m(x - a).")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson3P7))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson3P5))

class Lesson3P7(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Tangents")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="8/8")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! " + 
            "You should now know how to find the tangent and normal lines of an equation. " + 
            "Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz3P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson4P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Increase/Decrease")
        self.imagefile.config(file=get_image("lesson4 1.png"))
        self.pagenumber.config(text="2/5")
        self.explanation.config(text=
            "When a function is increasing, its gradient is positive " + 
            "(going up as it moves right), and when it is decreasing, " + 
            "its gradient is negative (going down as it moves right). " + 
            "When it is still (straight), it is stationary.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson4P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo4))

class Lesson4P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Increase/Decrease")
        self.imagefile.config(file=get_image("lesson4 2.png"))
        self.pagenumber.config(text="3/5")
        self.explanation.config(text=
            "To determine whether a function is increasing or decreasing at a certain point, " + 
            "derive it and substitute in the x value of that point. " + 
            "Note that f'(x) means the derivative of x. If the result is positive, " + 
            "it is increasing. If it is negative, it is decreasing. If it is 0, it is stationary.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson4P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson4P1))

class Lesson4P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Increase/Decrease")
        self.imagefile.config(file=get_image("lesson4 3.png"))
        self.pagenumber.config(text="4/5")
        self.explanation.config(text="Take a look at the worked example.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson4P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson4P2))

class Lesson4P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Increase/Decrease")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="5/5")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now know " + 
            "how to determine whether an equation is increasing, decreasing or stationary. " + 
            "Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz4P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson5P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("lesson5 1.png"))
        self.pagenumber.config(text="2/5")
        self.explanation.config(text=
            "A turning point is a point where f'(x) = 0. " + 
            "A maximum is a 'peak' and a minimum is a 'valley'.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson5P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo5))

class Lesson5P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("lesson5 2.png"))
        self.pagenumber.config(text="3/5")
        self.explanation.config(text=
            "To determine whether a quadratic's turning point is a " + 
            "minimum or a maximum, derive its equation twice.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson5P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson5P1))

class Lesson5P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("lesson5 3.png"))
        self.pagenumber.config(text="4/5")
        self.explanation.config(text="Take a look at the worked example.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson5P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson5P2))

class Lesson5P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Differentiation;Min/Max")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="5/5")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now know how to determine " + 
            "whether an equation's turning point is a minimum or a maximum. " + 
            "Go back through the lesson if you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz5P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson6P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("lesson6 1.png"))
        self.pagenumber.config(text="2/5")
        self.explanation.config(text=
            "You can think of integration as the opposite of differenatiation. If you have " + 
            "the graident of an equation, you can integrate it to find the original equation. " + 
            "Integration is sometimes called anti differentiation.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson6P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo6))

class Lesson6P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("lesson6 2.png"))
        self.pagenumber.config(text="3/5")
        self.explanation.config(text=
            "To integrate an equation, take everything 'up a level'. " +
            "For anything multiplied by x, put x to the power of its coefficient and " +
            "subtract one from its coefficient. For a constant, multiply it by x. " +
            "Always add a '+c' to represent constants that were removed in the original equation.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson6P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson6P1))

class Lesson6P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("lesson6 3.png"))
        self.pagenumber.config(text="4/5")
        self.explanation.config(text=
            "You might notice that we are left with a '+c' instead of the constant " +
            "in the original equation. We will cover how to find this constant and " +
            "therefore fully find the original equation in the next lesson.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson6P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson6P2))

class Lesson6P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Basics")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="5/5")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now know how to " + 
            "integrate an equation. Go back through the lesson if you're unsure on anything, " + 
            "otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz6P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson7P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file=get_image("lesson7 1.png"))
        self.pagenumber.config(text="2/4")
        self.explanation.config(text=
            "To find the original equation of a gradient, a point will be provided to you. " + 
            "Integrate the equation to get to the state where you have the unknown of '+c' " + 
            "(previous lesson). Then substitute in your point and solve for x.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson7P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo7))

class Lesson7P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file=get_image("lesson7 2.png"))
        self.pagenumber.config(text="3/4")
        self.explanation.config(text="Take a look at the worked example.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson7P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson7P1))

class Lesson7P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Functions")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="4/4")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now know how to " +
            "integrate to find the original equation. Go back through the lesson if " + 
            "you're unsure on anything, otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz7P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

class Lesson8P1(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file=get_image("lesson8 1.png"))
        self.pagenumber.config(text="2/5")
        self.explanation.config(text=
            "Kinematics describes the relationships between " + 
            "displacement, velocity and acceleration. " +
            "Because velocity is the rate of change of displacement, " + 
            "and acceleration is the rate of change of velocity, " + 
            "you can differentiate displacement to find velocity, " + 
            "and differentiate velocity to acceleration. " + 
            "You can also go backwards by integrating; take a look at the image above.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson8P2))
        self.backbutton.config(command=lambda:master.switch_frame(LessonInfo8))

class Lesson8P2(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file=get_image("lesson8 2.png"))
        self.pagenumber.config(text="3/5")
        self.explanation.config(text=
            "Take a look at the worked example above where " + 
            "you are calculating acceleration from displacement.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson8P3))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson8P1))

class Lesson8P3(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")    
        self.imagefile.config(file=get_image("lesson8 3.png"))
        self.pagenumber.config(text="4/5")
        self.explanation.config(text=
            "Take a look at the worked example above where you are calculating " +
            "displacement from acceleration. Note that points will be provided " + 
            "to you so that you can calculate the constant c.")
        self.nextbutton.config(command=lambda:master.switch_frame(Lesson8P4))
        self.backbutton.config(command=lambda:master.switch_frame(Lesson8P2))

class Lesson8P4(LessonTemplate):
    def __init__(self,master):
        LessonTemplate.__init__(self,master)
        self.title.config(text="Integration;Kinematics")
        self.imagefile.config(file=get_image("congratulations.png"))
        self.pagenumber.config(text="5/5")
        self.explanation.config(text=
            "Congratulations, you finished this lesson! You should now know " +
            "the basics of kinematics. Go back through the lesson if you're unsure on anything, " +
            "otherwise take the quiz!")
        self.nextbutton.config(text="Take the Quiz!",command=lambda:master.switch_frame(Quiz8P1))
        self.backbutton.config(text="Back to Menu",command=lambda:master.switch_frame(LessonSelect))

#Template class for quiz - each quiz page/class will be an instance of this class
class Quiz(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        #Score counter for the final quiz, will be accessed later outside of this class 
        FinalQuizScoreCount = 3
        # Answerlist varies per question, and will be defined differently every question
        # Therefore. no point in a default 
        self.answerlist = [""]
        # Same as above, no point in default
        self.correctanswer = ""
        # Setting frametype for the swich frame function
        self.frametype = "place"
        # Background colour is set to a constant variable for consistenty
        self.config(bg=BGCOLOUR)
        # This is for the final quizzes - boolean is used to check if it is the user's first attempt or not
        self.firstattempt = True
        # Unlike the lessons, the title WILL be consistent across some of the quizzes (the final quiz)
        # Therefore a default makes sense in this case, and will reduce lines of code written
        self.title = tk.Label(self,text='Final Quiz',font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        # No point in a default for the images
        # However, setting this to be blank throws up an error so a random image is used
        self.imagefile = tk.PhotoImage(file=get_image("congratulations.png"))      
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile
        # User answer is set as a string, saves me from having to do str() constantly
        self.useranswer = tk.StringVar()
        # Sets the answering optionmenu to display everything within the answerlist
        # Also sets the selected answer to the useranswer varible
        self.explanation = tk.OptionMenu(self,self.useranswer,*self.answerlist)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.explanation.config(font=BUTTONFONT)
        # The optionmenu object is given a name via the nametowidget method
        # This allows me to set a custom font for the selected/highlighted answer
        self.options = self.nametowidget(self.explanation.menuname)
        self.options.config(font=BUTTONFONT)
        # Question number will vary, no point in default
        self.questionnumber = tk.Label(self,text="",bg=BGCOLOUR,font=BUTTONFONT)
        self.questionnumber.place(relx = 0.5,rely=0.9,anchor="center")
        # Submitting will run the check_answer function
        # Giving up kicks the user back out to the main menu
        self.submitbutton = tk.Button(self,text="Submit",bg="spring green3",
            command=lambda:self.check_answer(),font=BUTTONFONT)
        self.submitbutton.place(relx = 0.8,rely=0.9,anchor="center")
        self.backbutton = tk.Button(self,text="Give Up",bg="orange red2",
            command=lambda:master.switch_frame(LessonSelect),font=BUTTONFONT)
        self.backbutton.place(relx = 0.2,rely=0.9,anchor="center")
        
    
    # The subroutine for checking the answer + whether it counts as a point
    def check_answer(self):
        # If it is a question in the final quiz:
        if self.finalquiz == True:
            # If the user's answer is the same as the correct answer:
            if self.useranswer.get() == self.correctanswer:
                # Button changes to say correct and disply a different shade of green
                self.submitbutton.config(text="Correct!", bg="lawn green",command = "")
                # IF it is the user's first attempt, then score count is upped
                if self.firstattempt == True: self.master.FinalQuizScoreCount +=1
                # In 2 seconds, the next frame is called
                self.after(2000,lambda:self.master.switch_frame(self.nextframe))
            # If the user's answer is blank (i.e nothing was selected)
            elif self.useranswer.get() == "":
                # The button text changes to "select an answer"
                # After 2 seconds the button reverts to normal
                # Note that this doesn't change the status of firstattempt
                # This is so a blank submission doesn't count as an attempt
                self.submitbutton.config(text="Please select an answer!", 
                    bg = "orange red2",command = "")
                self.after(2000,lambda:self.submitbutton.config(text="Submit",
                    bg="spring green3",command=lambda:self.check_answer()))
            # Else if the user's answer is incorrect:
            else:
                # Firstattempt is set to false 
                # Any subsequent answers therefore won't count towards the final score
                self.firstattempt = False
                # They are told incorrect, and for 3 seconds the submit button ceases to function
                self.submitbutton.config(text="Incorrect (3)",bg = "orange red2", command = "")
                self.after(1000,lambda:self.submitbutton.config(
                    text="Incorrect (2)",bg = "orange red2", command = ""))
                self.after(2000,lambda:self.submitbutton.config(
                    text="Incorrect (1)",bg = "orange red2", command = ""))
                self.after(3000,lambda:self.submitbutton.config(
                    text="Submit",bg = "spring green3", command=lambda:self.check_answer()))
        # If it is just a normal quiz (i.e part of the lessons)
        else:
            # If the answer is correct, the user is told they are correct and the next frame is switched to
            if self.useranswer.get() == self.correctanswer:
                self.submitbutton.config(text="Correct!", bg="lawn green",command = "")
                self.after(2000,lambda:self.master.switch_frame(self.nextframe))
            # If blank, they are told "please selct an answer"
            elif self.useranswer.get() == "":
                self.submitbutton.config(text="Please select an answer!",
                    bg = "orange red2",command = "")
                self.after(2000,lambda:self.submitbutton.config(
                    text="Submit",bg="spring green3",command=lambda:self.check_answer()))
            # If wrong, then they can't submit another answer for 3 seconds
            else:
                self.submitbutton.config(text="Incorrect (3)",
                    bg = "orange red2", command = "")
                self.after(1000,lambda:self.submitbutton.config(
                    text="Incorrect (2)",bg = "orange red2", command = ""))
                self.after(2000,lambda:self.submitbutton.config(
                    text="Incorrect (1)",bg = "orange red2", command = ""))
                self.after(3000,lambda:self.submitbutton.config(
                    text="Submit",bg = "spring green3", command=lambda:self.check_answer()))

    # This function is used to refresh the dropdown menu in each individual quiz
    # This is doneafter the answer list is redefined in each subclass
    def refresh_menu(self):
        # The explanation widget is destroyed
        self.explanation.destroy
        # Explanation is defined again using the updated answerlist and placed in the same spot
        self.explanation = tk.OptionMenu(self,self.useranswer,*self.answerlist)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.explanation.config(font=BUTTONFONT)
        self.options = self.nametowidget(self.explanation.menuname)
        self.options.config(font=BUTTONFONT)

#############################################################
# Quiz classes - instances of the Quiz class/template/master

class Quiz1P1(Quiz):
    def __init__(self,master):
        # Initalizing the quiz class, so all of the widgets/variables are present
        Quiz.__init__(self,master)
        # Final quiz is set to false, as this is just a lesson quiz
        self.finalquiz = False
        # The next frame is defined so the check_answer function can switch to this
        self.nextframe = Quiz1P2
        # Title is set
        self.title.config(text="Differentiation;Basics")
        # Possible answers/choices are set
        self.answerlist = ["f'(x) = x² + 103",
            "f'(x) = 0.5x + 4","f'(x) = x + 4", "f'(x) = 99x + 2"]
        # The question image is set
        self.imagefile.config(file = get_image("quiz1 1.png"))
        # Menu is refreshed to show the answerlist defined above
        Quiz.refresh_menu(self)
        # Correct answer is set, so check_answer has something to compare the user's answer with
        self.correctanswer = "f'(x) = x + 4"
        # Question number is configured
        self.questionnumber.config(text="Question 1/2")

class Quiz1P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Differentiation;Basics")
        self.answerlist = ["f'(x) = 4x","f'(x) = 4x + 99",
            "f'(x) = 4x² + 99", "f'(x ) = 2x² + 99x + 99"]
        self.imagefile.config(file = get_image("quiz1 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f'(x) = 4x"
        self.questionnumber.config(text="Question 2/2")

class Quiz2P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz2P2
        self.title.config(text="Differentiation;Gradients")
        self.answerlist = ["f'(x) = 6x + 3","f'(x) = 2",
            "f'(x) = 4x²", "f'(x) = 2x + 4"]
        self.imagefile.config(file = get_image("quiz2 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f'(x) = 2x + 4"
        self.questionnumber.config(text="Question 1/2")

class Quiz2P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Differentiation;Gradients")
        self.answerlist = ["f'(2) = 10",
            "f'(3) = 14","f'(3) = 12", "f'(3) = 4x + 2"]
        self.imagefile.config(file = get_image("quiz2 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f'(3) = 14"
        self.questionnumber.config(text="Question 2/2")

class Quiz3P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz3P2
        self.title.config(text="Differentiation;Tangents")
        self.answerlist = ["y = 9x - 5","y = x + 2","y = 10x - 6", "y = x"]
        self.imagefile.config(file = get_image("quiz3 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "y = 10x - 6"
        self.questionnumber.config(text="Question 1/2")

class Quiz3P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Differentiation;Tangents")
        self.answerlist = ["y = -x/10 + 27.3",
            "y = 10x + 3","y = x + 2", "y = -x/10 + 30"]
        self.imagefile.config(file = get_image("quiz3 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "y = -x/10 + 27.3"
        self.questionnumber.config(text="Question 2/2")

class Quiz4P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz4P2
        self.title.config(text="Differentiation;Increase/Decrease")
        self.answerlist = ["Increasing","Decreasing","Stationary"]
        self.imagefile.config(file = get_image("quiz4 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Decreasing"
        self.questionnumber.config(text="Question 1/2")

class Quiz4P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Differentiation;Increase/Decrease")
        self.answerlist = ["Increasing","Decreasing","Stationary"]
        self.imagefile.config(file = get_image("quiz4 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Stationary"
        self.questionnumber.config(text="Question 2/2")

class Quiz5P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz5P2
        self.title.config(text="Differentiation;Min/Max")
        self.answerlist = ["Maximum","Minimum"]
        self.imagefile.config(file = get_image("quiz5 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Minimum"
        self.questionnumber.config(text="Question 1/2")

class Quiz5P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Differentiation;Min/Max")
        self.answerlist = ["Maximum","Minimum"]
        self.imagefile.config(file = get_image("quiz5 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Maximum"
        self.questionnumber.config(text="Question 2/2")

class Quiz6P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz6P2
        self.title.config(text="Integration;Basics")
        self.answerlist = ["f(x) = x² + 9x + c","f(x) = 2x² + 9x",
            "(fx) = x² + 9x + 1","f(x) = 2x² + 9 + c"]
        self.imagefile.config(file = get_image("quiz6 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f(x) = x² + 9x + c"
        self.questionnumber.config(text="Question 1/2")

class Quiz6P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Integration;Basics")
        self.answerlist = ["f(x) = x²/2 + cx + d","f(x) = x² + c", 
            "f(x) = x² + 2x + d","f(x) = x²/2 + c"]
        self.imagefile.config(file = get_image("quiz6 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f(x) = x²/2 + c"
        self.questionnumber.config(text="Question 2/2")

class Quiz7P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz7P2
        self.title.config(text="Integration;Functions")
        self.answerlist = ["f(x) = x² + 3x + c","f(x) = x² + 3x",
             "f(x) = x² + 3x + 3","f(x) = x² + 2x + 3"]
        self.imagefile.config(file = get_image("quiz7 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f(x) = x² + 3x"
        self.questionnumber.config(text="Question 1/2")


class Quiz7P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Integration;Functions")
        self.answerlist = ["f(x) = x²/2 + 4x - 8","f(x) = x² - 4x + 8",
            "f(x) = x²/2 - 4x + 8","f(x) = x²/2 + c"]
        self.imagefile.config(file = get_image("quiz7 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f(x) = x²/2 - 4x + 8"
        self.questionnumber.config(text="Question 2/2")

class Quiz8P1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = Quiz8P2
        self.title.config(text="Integration;Kinematics")
        self.answerlist = ["a(t) = 4ms⁻²","a(t) = 2ms⁻²", 
            "a(t) = 0.5ms⁻²","v(t) = 4tms⁻¹"]
        self.imagefile.config(file = get_image("quiz8 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "a(t) = 4ms⁻²"
        self.questionnumber.config(text="Question 1/2")

class Quiz8P2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = False
        self.nextframe = QuizCongratulations
        self.title.config(text="Integration;Kinematics")
        self.answerlist = ["s(0) = 0m","v(0) = 4ms⁻¹",
            "v(t) = 2tms⁻¹","v(0) = 3ms⁻¹"]
        self.imagefile.config(file = get_image("quiz8 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "v(0) = 3ms⁻¹"
        self.questionnumber.config(text="Question 2/2")

# This is the congratulations page for each quiz, and displays upon successful completion of a lesson's quiz.
# Note that it is not an instance of anything, but merely a unique frame
# This is because it doesn't share many of the qualites/placements of widgets with a template class
# Therefore, using a template would mean more lines and more clutter, this was an easier way of doing things
class QuizCongratulations(tk.Frame):
    def __init__(self,master):
        # Frametype is defined
        self.frametype = "place"
        tk.Frame.__init__(self,master)
        # Background colour is set
        self.config(bg=BGCOLOUR)
        # Title is set to say congratulations
        self.title = tk.Label(self,text='Congratulations!',font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        # Imagefile is set to the dedicated "congratulations" image file
        self.imagefile = tk.PhotoImage(file=get_image("congratulations.png"))      
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile
        # A catch-all explanation is written so that this screen used for all lesson quizzes
        self.explanation = tk.Label(self,text=
            "Congratulations, you have finished this quiz! Redo this lesson if you feel " +
            "unsure about it, move on to other lessons if you feel confident, " + 
            "and if you're comfortable with everything then attempt the final quiz! ",
            font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.explanation.config(font=BUTTONFONT)
        # Button to back to the main menu is defined and placed bottom centre
        self.backbutton = tk.Button(self,text="Back to Menu",bg="spring green3",
            command=lambda:master.switch_frame(LessonSelect),font=BUTTONFONT)
        self.backbutton.place(relx = 0.5,rely=0.9,anchor="center")

class FinalQuizP1(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        # Because this quiz screen is part of the final quiz, this is set to true
        self.finalquiz = True
        # The number of correct questions is reset to 0, in case the user is reattempting the quiz
        # This ensures that the score count is accurate and points from another attempt are removed  
        master.FinalQuizScoreCount = 0
        self.nextframe = FinalQuizP2
        self.answerlist = ["f'(x) = 3x² + 4x + 2",
            "f'(x) = 6x + 4","f'(x) = 6x² + 6", "f'(x) = 3x + 4"]
        self.imagefile.config(file=get_image("quizfinal 1.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f'(x) = 6x + 4"
        self.questionnumber.config(text="Question 1/8")

class FinalQuizP2(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP3
        self.answerlist = ["f'(2) = 41","f'(2) = 8","f'(2) = 11","f'(2) = 12"]
        self.imagefile.config(file=get_image("quizfinal 2.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "f'(2) = 11"
        self.questionnumber.config(text="Question 2/8")

class FinalQuizP3(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP4
        self.answerlist = ["y = 12x - 6","y = 4x + 4","y = 8x - 17","y = x + 2"]
        self.imagefile.config(file=get_image("quizfinal 3.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "y = 12x - 6"
        self.questionnumber.config(text="Question 3/8")

class FinalQuizP4(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP5
        self.answerlist = ["Increasing","Decreasing","Stationary"]
        self.imagefile.config(file=get_image("quizfinal 4.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Increasing"
        self.questionnumber.config(text="Question 4/8")

class FinalQuizP5(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP6
        self.answerlist = ["Minimum","Maximum"]
        self.imagefile.config(file=get_image("quizfinal 5.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "Maximum"
        self.questionnumber.config(text="Question 5/8")

class FinalQuizP6(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP7
        self.answerlist = ["4x²+ 4x + 4","2x² + 4","2x⁴ + 4x + c","2x² + 4x + c"]
        self.imagefile.config(file=get_image("quizfinal 6.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "2x² + 4x + c"
        self.questionnumber.config(text="Question 6/8")

class FinalQuizP7(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalQuizP8
        self.answerlist = ["2x² + 2 + c","3x² - 3x + c","3x² + 3x + 4","3x² - 3x - 4"]
        self.imagefile.config(file=get_image("quizfinal 7.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "3x² - 3x - 4"
        self.questionnumber.config(text="Question 7/8")

class FinalQuizP8(Quiz):
    def __init__(self,master):
        Quiz.__init__(self,master)
        self.finalquiz = True
        self.nextframe = FinalCongratulations
        self.answerlist = ["a(t) = 2ms⁻²","a(t) = 3ms⁻²","a(t) = 4ms⁻²","a(t) = 55ms⁻²"]
        self.imagefile.config(file=get_image("quizfinal 8.png"))
        Quiz.refresh_menu(self)
        self.correctanswer = "a(t) = 2ms⁻²"
        self.questionnumber.config(text="Question 8/8")

# This is the congratulations class that runs upon successful completion of the final quiz. 
class FinalCongratulations(Quiz):
    def __init__(self,master):
        # Defining frametype
        self.frametype = "place"
        # This is the initial reading of the highscore
        with open(get_image(HIGHSCOREFILE),"r+") as TXT_FILE:
            self.highscore = TXT_FILE.readline()
        tk.Frame.__init__(self,master)
        # Background colour is set
        self.config(bg=BGCOLOUR)
        # Title is set
        self.title = tk.Label(self,text='Congratulations!',font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        # Image is set again to the congratulations image
        self.imagefile = tk.PhotoImage(file=get_image("congratulations.png"))      
        self.photolabel = tk.Label(self,image=self.imagefile,borderwidth=0)
        self.photolabel.place(relx=0.5,rely=0.4,anchor="center")
        self.photolabel.img = self.imagefile
        # Explanation is set to blank for now, will be changed in the upcoming if/else statement
        self.explanation = tk.Label(self,text="",font=BUTTONFONT,wraplength = 1000, bg = BGCOLOUR)
        # If the user got a perfect score:
        if int(master.FinalQuizScoreCount) == 8:
            # Set the highscore to 8
            self.highscore = int(master.FinalQuizScoreCount)
            # First congratulate them on their perfect score
            # Then recommend they go do practice tests
            # This is becausethey have finished the content offered in this program
            self.explanation.config(text=
                "Congratulations, you got all 8 questions right on the first try! " + 
                "You have finished all of the lessons within this program, " + 
                "and you should now be comfortable with all of the major topics " + 
                "covered in Level 2 Calculus. Feel free to go back through this program " + 
                "as required, otherwise start doing practice tests!")
        # If the user set a new high score:
        elif  int(master.FinalQuizScoreCount) > int(self.highscore):
            # Set the new highscore
            self.highscore = int(master.FinalQuizScoreCount)
            # Congratulation them, encourge them to try again and get a perfect score
            self.explanation.config(text=
                "Congratulations, you got " + str(master.FinalQuizScoreCount) + 
                " questions right on the first try! This is your new high score! " + 
                "Try again for a better high score!")
        # If the user equalled their old high score:
        elif int(self.highscore) == int(master.FinalQuizScoreCount):
            self.explanation.config(text=
                "Congratulations, you got " + str(master.FinalQuizScoreCount) + 
                " questions right on the first try! This is equal to your old high score! " +
                "Try again for a better high score!")
        # If the user did worse than their high score
        else:
            self.explanation.config(text=
                "Congratulations, you got " + str(master.FinalQuizScoreCount) + 
                " questions right on the first try! Unfortunately, " + 
                "you didn't beat your high score of " + str(self.highscore) + 
                ". Try again for a better high score!")
        self.explanation.place(relx = 0.5,rely=0.7,anchor="center")
        self.explanation.config(font=BUTTONFONT)
        self.backbutton = tk.Button(self,text="Back to Menu",bg="spring green3",
            command=lambda:self.export_score(),font=BUTTONFONT)
        self.backbutton.place(relx = 0.5,rely=0.9,anchor="center")
        
    # This is run when the user tries to go back to menu
    # It exports the high score to the txt file (whether it is new or the same) and then switches frames
    def export_score(self):
        with open(get_image(HIGHSCOREFILE),"r+") as TXT_FILE:
            TXT_FILE.write(str(self.highscore))
        self.master.switch_frame(LessonSelect)

#Defining the main subroutine
def main():
    # App is set equal to the maths object we definied above
    app = Maths()
    # The resolution of the app is set
    app.geometry("1280x720")
    # The background colour of the app is set
    app.config(bg=BGCOLOUR)
    # The option to resize the app is disabled
    # The maximize/minimize button is disabled
    # The resize app from corner option is also disabled 
    app.resizable(False, False)
    # Setting the programs icon to a custom one
    app.iconbitmap(get_image("maths.ico"))
    # Mainloop is run to keep the program running
    app.mainloop()

#Proper, conventional way to run main, prevents main accidentally running if the program is ever called
if __name__ == '__main__':
    main()