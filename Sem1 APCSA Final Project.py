#File: Sem1 APCSA Final Project.py
#Student: Esteban Cornejo
#
#Date: December 19, 2024
#Description of Program: This is the final project of the semester, I chose to make a "Mr. Lopez Verification Program"
#it serves no real purpose except as a display of my coding abilities and a form of enjoyment
#GitHub: ejcornejo

from tkinter import * 
from tkinter import messagebox

#Beginning message
def start():
    messagebox.showinfo(title="New Message", message="Hello thealeph0 \nYou have  1  unread message from:\n‣ejcornejo\n(*You will need to verify that you are thealeph0 first.*)")
    createWindow1()

#Window
def createWindow1():
    global window
    window = Tk()                        #
    window.title("Verification")         #
    window.grid_columnconfigure(4)       # Creates window for the questions
    window.geometry("1700x1000")         #
    window.tk.call('tk', 'scaling', 5.0) #
    verify()
    #Grid
    window.columnconfigure(0, weight = 2)
    window.columnconfigure(1, weight = 1)
    window.columnconfigure((2,3,4,5), weight = 3)
    window.rowconfigure((1,2,3,4,5,6,7,8,9,10,11,12), weight = 1)

#Unread Messages Inbox
def createWindow2():
    global unreadMessages
    unreadMessages = Tk()                        #
    unreadMessages.title("Unread Messages")      #
    unreadMessages.grid_columnconfigure(4)       # Creates window for "unread message"
    unreadMessages.geometry("1500x800")          #
    unreadMessages.tk.call('tk', 'scaling', 5.0) #
    unreadMessages.columnconfigure((0,1,2,3), weight = 1)
    unreadMessages.rowconfigure((0,1,2,3), weight = 1)
    
    readmessage = Button(unreadMessages, text="1  unread message from:\n‣ejcornejo", font="Arial 50", background = 'light yellow', fg = 'cyan', command = Messages)
    readmessage.grid(column = 1, row = 1, columnspan = 2, rowspan=2, sticky = "news")
#ejcornejo's Message
def Messages():
    unreadMessages.destroy()
    global message
    message = Tk()
    message.title("Unread Messages")      #
    message.grid_columnconfigure(4)       # Creates window for "unread message"
    message.geometry("1400x700")          #
    message.tk.call('tk', 'scaling', 5.0) #
    message.columnconfigure(0, weight = 1)
    message.rowconfigure((0,1,2,3), weight = 1)
    
    ejcornejo1 = Label(message, text="Hello Mr. Lopez,", font = "Arial 20", padx = 20, pady =20)
    ejcornejo1.grid(row = 0, sticky = 'w')
    ejcornejo2 = Label(message, text="Please go to google and type the following link:", font = "Arial 20", padx = 20, pady =20)
    ejcornejo2.grid(row = 1, sticky = 'w')
    ejcornejo3 = Label(message, text="https://bit.ly/ejcornejo", font = "Arial 20", padx = 20, pady =20)
    ejcornejo3.grid(row = 2, sticky = 'w')
    ejcornejo4 = Label(message, text="-Esteban", font = "Arial 20", padx = 20, pady =20)
    ejcornejo4.grid(row = 3, sticky = 'w')
    
    
#Spinbox value
txt_spin_value = 28


#Warning and First question
def verify():
    label1 = Label(window, text="Don't\n\npress\n\nprevious\n\nanswers", pady = 20, font= "Arial 20", background = 'light yellow', fg = 'orange')
    label1.grid(column=1, rowspan = 13, sticky = 'news')
    
    question1 = Label(window, text="1. What is thealeph0's real name?", font= "Arial 25", padx=20)
    question1.grid(row = 1, column = 0, sticky = 'w')
    
    btn1Right = Button(window, text="Sahiv Lopez", font="Arial 20", padx = 10, command= pressBtn1Right)
    btn1Right.grid(row = 1, column = 3)
    
    btn1Wrong = Button(window, text="thealeph0", font="Arial 20", padx = 10, command = wrongAnswer)
    btn1Wrong.grid(row = 1, column = 5)

# If clicked, prints "Correct!" and asks next question (question 2)
def pressBtn1Right():
    
    correct1 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
    correct1.grid(row = 2, column = 0, sticky = 'ew')
    
    question2 = Label(window, text="2. Which UC did Mr. Lopez attend?", font= "Arial 25", padx=20)
    question2.grid(row = 3, column = 0, sticky = 'w')
    
    UCD = Button(window, text="UC Davis", font="Arial 20", command= wrongAnswer)
    UCD.grid(row = 3, column = 2)
    
    UCLA = Button(window, text="UCLA", font="Arial 20", command = wrongAnswer)
    UCLA.grid(row = 3, column = 4)
    
    UCI = Button(window, text="UC Irvine", font="Arial 20", command= pressUCI)
    UCI.grid(row = 3, column = 3)
    
    UCSD = Button(window, text="UC San Diego", font="Arial 20", command = wrongAnswer)
    UCSD.grid(row = 3, column = 5)
    
# If clicked, prints "Correct!" and asks next question (question 3)
def pressUCI():
    correct2 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
    correct2.grid(row = 4, column = 0, sticky = 'ew')
    
    question3 = Label(window, text="3. How old is Mr. Lopez?", font= "Arial 25", padx=20)
    question3.grid(row = 5, column=0, sticky = 'w')
    
    ageButton = Button(window, text="I have entered my age", font="Arial 15", padx = 20, command= ageCheck)
    ageButton.grid(row = 5, column = 5)
    
    global txt_spin_value
    global spinNumber
    spinNumber = Spinbox(window, from_ = 0, to = 100, font = "Arial 15", textvariable=txt_spin_value)
    spinNumber.grid(column = 3, row=5)

# If 28 is inputted, prints "Correct!" and asks next question (question 4)
# If not, program is closed
def ageCheck():
    #The user inputs "28"
    if int(spinNumber.get()) == 28:
        correct3 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
        correct3.grid(row = 6, column = 0, sticky = 'ew')
        
        question4 = Label(window, text="4. What is Mr. Lopez's Period 1 class?", font= "Arial 25", padx=20)
        question4.grid(row = 7, column = 0, sticky = 'w')
        
        APCALCBC = Button(window, text="AP Calculus BC", font="Arial 20", command= wrongAnswer)
        APCALCBC.grid(row = 7, column = 2)
        
        APCSA = Button(window, text="APCSA", font="Arial 20", command = wrongAnswer)
        APCSA.grid(row = 7, column = 3)
        
        APCALCAB = Button(window, text="AP Calculus AB", font="Arial 20", command= pressABCALCAB)
        APCALCAB.grid(row = 7, column = 5)
        
        HALG2TRIG = Button(window, text="H. Algebra II/Trig", font="Arial 20", command = wrongAnswer)
        HALG2TRIG.grid(row = 7, column = 4)

    else:
        wrongAnswer()

# If clicked, prints "Correct!" and asks next question (question 5)
def pressABCALCAB():
    correct4 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
    correct4.grid(row = 8, column = 0, sticky = 'ew')
    
    question5 = Label(window, text="5. What is Mr. Lopez's Period 2 class?", font= "Arial 25", padx=20)
    question5.grid(row = 9, column = 0, sticky = 'w')
        
    APCALCBC = Button(window, text="AP Calculus BC", font="Arial 20", command= pressAPCALCBC)
    APCALCBC.grid(row = 9, column = 2)
        
    APCSA = Button(window, text="APCSA", font="Arial 20", command = wrongAnswer)
    APCSA.grid(row = 9, column = 3)
        
    APCALCAB = Button(window, text="AP Calculus AB", font="Arial 20", command= wrongAnswer)
    APCALCAB.grid(row = 9, column = 5)
        
    HALG2TRIG = Button(window, text="H. Algebra II/Trig", font="Arial 20", command = wrongAnswer)
    HALG2TRIG.grid(row = 9, column = 4)


# If clicked, prints "Correct!" and asks next question (question 6 (final question))
def pressAPCALCBC():
    correct5 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
    correct5.grid(row = 10, column = 0, sticky = 'ew')
    
    question6 = Label(window, text="6. What is Mr. Lopez's Period 7 class?", font= "Arial 25", padx=20)
    question6.grid(row = 11, column = 0, sticky = 'w')
        
    APCALCBC = Button(window, text="AP Calculus BC", font="Arial 20", command= wrongAnswer)
    APCALCBC.grid(row = 11, column = 2)
        
    APCSA = Button(window, text="APCSA", font="Arial 20", command = pressAPCSA)
    APCSA.grid(row = 11, column = 3)
        
    APCALCAB = Button(window, text="AP Calculus AB", font="Arial 20", command= wrongAnswer)
    APCALCAB.grid(row = 11, column = 5)
        
    HALG2TRIG = Button(window, text="H. Algebra II/Trig", font="Arial 20", command = wrongAnswer)
    HALG2TRIG.grid(row = 11, column = 4)

# If clicked, prints "Correct!" and heads to next message box
def pressAPCSA():
    correct6 = Label(window, text="Correct!", padx = 10, pady = 10, font = "Arial 15",background = 'green',  fg = 'white')
    correct6.grid(row = 12, column = 0, sticky = 'ew')
    verified()

# Message Box pops up, saying user passed,
# Opens another window for the Inbox
# And closes orginal window
def verified():
    messagebox.showinfo(title = 'VERIFICATION COMPLETED', message="Welcome,\nMr. Lopez!\n(Press OK to open inbox)")
    createWindow2()
    window.destroy()

# Non synchronus code

#########################################################################################################################################################
    
# WRONG ANSWERS (DESTROY WINDOW)
# All wrong answers lead to this code
# Tells the user they failed and kills the window
def wrongAnswer():
    messagebox.showinfo(title = "Verification Failed!", message="Verification Failed!\nGoodbye!")
    window.destroy()
    
    
    
#Start Program on run 
start()