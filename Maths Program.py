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
        self.switch_frame(titleScreen)
        self.title("L2 Calculus Program")

    #The frame switch method
    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        if str(frame_class) == ("<class '__main__." + testvar + "'>"):
            self._frame.pack(expand=TRUE,fill="both")
        else:
            self._frame.pack()        

#Title screen widgets
class titleScreen(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="Calculus",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,pady=100)
        tk.Button(self,text="Start",font=BUTTONFONT,bg="spring green3",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=lambda:master.switch_frame(lessonSelect)) .grid(column=1)
        tk.Label(self,text="",bg=BGCOLOUR) .grid(column=1)
        tk.Button(self,text="Quit",font=BUTTONFONT,bg="orange red2",width = BUTTONWIDTH, height = BUTTONHEIGHT,command=quit) .grid(column=1,pady=30)

#Lesson select screen widgets
class lessonSelect(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.config(bg=BGCOLOUR)
        tk.Label(self,text="Lessons",font=TITLEFONT,bg=BGCOLOUR) .grid(column=1,row=0)
        tk.Button(self,text='Differentiation;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(lessonInfo1),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=1,padx=BUTTONGAPX,pady=BUTTONGAPY)
        tk.Button(self,text='Differentiation;Gradients',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(lessonInfo2),bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Differentiation;Tangents',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=2,row=1,padx=BUTTONGAPX)
        tk.Button(self,text='Differentiation;Δ Graident',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=0,row=2,pady=BUTTONGAPY)
        tk.Button(self,text='Differentiation;Max/Min',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=DIFFBG,font = SMALLBUTTONFONT) .grid(column=1,row=2)
        tk.Button(self,text='Integration;Basics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=INTBG,font = SMALLBUTTONFONT) .grid(column=2,row=2)
        tk.Button(self,text='Integration;Functions',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg=INTBG,font = SMALLBUTTONFONT) .grid(column=0,row=3)
        tk.Button(self,text='Integration;Kinematics',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg= INTBG,font = SMALLBUTTONFONT) .grid(column=1,row=3,pady=BUTTONGAPY)
        tk.Button(self,text='Final Quiz',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command="",bg= "chocolate2",font = SMALLBUTTONFONT) .grid(column=2,row=3)
        tk.Button(self,text='Back',width=SSBUTTONWIDTH,height=SSBUTTONHEIGHT,command=lambda:master.switch_frame(titleScreen),bg="orange red2",font = SMALLBUTTONFONT) .grid(column=1,row=4,pady=BACKBUTTONGAPY)

    def switchLessonFrame(self,text):
        pass 


#Lesson info screen widgets
class lessonInfo(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.config(bg=BGCOLOUR)
        self.title = tk.Label(self,text='Differentiation;Basics',font = HEADINGFONT, bg = BGCOLOUR)
        self.title.place(relx = 0.5, rely = 0.1, anchor="center")
        self.imagefile = tk.PhotoImage(file="LeibnizNotation.png") 
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
        self.backbutton = tk.Button(self,text="Back",bg="orange red2",font=BUTTONFONT,command=lambda:master.switch_frame(lessonSelect))
        self.backbutton.place(relx = 0.2,rely=0.9,anchor="center")
    

class lessonInfo1(lessonInfo):
    def __init__(self,master):
        lessonInfo.__init__(self,master)
        tk.Label(self,text="hello") .place(relx=0.5,rely=0.9,anchor="center")
        self.nextbutton.config(text="next2")

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