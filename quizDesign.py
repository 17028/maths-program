import tkinter as tk
from tkinter.constants import BOTH, TRUE
import os

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
        self.switch_frame(Quiz)
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

class Quiz(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)  
        self.frametype = "place"
        self.config(bg=BGCOLOUR)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1,min=500)
        title = tk.Label(self,text='Integration;Kinematics',font = HEADINGFONT, bg = BGCOLOUR)
        title.place(relx = 0.5, rely = 0.1, anchor="center")
        imagefile = tk.PhotoImage(file=get_image("quizDesign.png"))      
        photolabel = tk.Label(self,image=imagefile,borderwidth=0)
        photolabel.place(relx=0.5,rely=0.4,anchor="center")
        photolabel.img = imagefile
        a = tk.StringVar()
        explanation = tk.OptionMenu(self,a,*answerList)
        explanation.place(relx = 0.5,rely=0.7,anchor="center")
        explanation.config(font=BUTTONFONT)
        options = self.nametowidget(explanation.menuname)
        options.config(font=BUTTONFONT)
        questionnumber = tk.Label(self,text="Question 1/6",bg=BGCOLOUR,font=BUTTONFONT)
        questionnumber.place(relx = 0.5,rely=0.9,anchor="center")
        submitbutton = tk.Button(self,text="Submit",bg="spring green3",command=lambda:print(a.get()),font=BUTTONFONT)
        submitbutton.place(relx = 0.8,rely=0.9,anchor="center")
        backbutton = tk.Button(self,text="Back to Menu",bg="orange red2",font=BUTTONFONT)
        backbutton.place(relx = 0.2,rely=0.9,anchor="center")

answerList = ["s = 1m","s = 2m","s = 3m","s = 4m"]

def main():
    app = Maths()
    app.geometry("1280x720")
    app.config(bg=BGCOLOUR)
    app.resizable(False, False)
    app.mainloop()

if __name__ == '__main__':
    main()