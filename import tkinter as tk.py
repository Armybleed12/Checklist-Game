import tkinter as tk
import time
import random
from tkinter import messagebox
from playsound import playsound
import os
import openai


openai.api_key = "your-own-api-BRO!!"
openai.Model.list()



# create a new window to display the 


points = 100
player1Points = 0
player2Points = 0

GameWindow = tk.Tk()
GameWindow.title("Task Timer")
GameWindow.geometry("800x900")
GameWindow.configure(background='#000000')







# create a frame for the game
GameFrame = tk.Frame(GameWindow, width=400, height=400)
GameFrame.pack()

# create a scroll bar and frame
scrollBar = tk.Scrollbar(GameFrame)
listBox = tk.Listbox(GameFrame, width=30, height=20, yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
listBox.pack(side=tk.LEFT, fill=tk.BOTH)


# create a settings Frame
SettingsFrame = tk.Frame(GameWindow, width=900, height=200, bg='#ffffff', relief='raised', borderwidth=15, padx=5, pady=5)
SettingsFrame.pack()

# add player 1 and player 2 labels
player1 = tk.Label(GameWindow, text="Player 1", bg='#000000', fg='#ffffff')
player1.place(x=30, y=0)

player2 = tk.Label(GameWindow, text="Player 2", bg='#000000', fg='#ffffff')
player2.place(x=700, y=0)

player1Score = tk.Label(GameWindow, text="Score: " + str(player1Points), bg='#000000', fg='#ffffff')
player1Score.place(x=30, y=20)
player2Score = tk.Label(GameWindow, text="Score: " + str(player2Points), bg='#000000', fg='#ffffff')
player2Score.place(x=700, y=20)


# make a list for task for player 1
taskPlayer1 = []
taskPlayer2 = []

todaysTasks = []



# add timer to the gameFrame    
timer = tk.Label(GameWindow, text="Timer", font=("Helvetica", 20), fg="white", bg="#000000")
timer.pack()

def updateTimer():
    # get the current time in am pm format
    currentTime = time.strftime("%I:%M:%S %p")
    # update the timer label
    timer.configure(text=currentTime)

    #timer.config(text=str(time.strftime("%H:%M:%S")))
    


    timer.after(1000, updateTimer)

updateTimer()

TodaysPoints = tk.Label(GameWindow, text="Today's Points Remaining: " + str(points), font=("Helvetica", 20), fg="white", bg="#000000")
TodaysPoints.pack()


# create a label that says " Assign your next task"
taskPlayer1Label = tk.Label(SettingsFrame, text="Assign your next task", font=("Helvetica", 20), fg="black", bg="#ffffff")
taskPlayer1Label.place(x=10, y=20)



# create a slider for points
pointsSlider = tk.Scale(SettingsFrame, from_=0, to=100, orient=tk.HORIZONTAL, label="How many points is this task worth?", length=230)
pointsSlider.place(x=533, y=-5)



# create a form field that will allow the user to assign a task to todays tasks
todaysTasks = tk.Entry(SettingsFrame, width=50, font=("Helvetica", 20))
todaysTasks.place(x=0, y=75)


# function that adds the task

def summitTodaysTasks():
    if todaysTasks.get()=="":
        messagebox.showinfo("BRO! Dont be lazy! ", "You need to assign a task to play the game!")
    else:
        todaysTasks.get()
        theTask = todaysTasks.get()
        print(theTask)
        # get points from the slider
        currentPoints = pointsSlider.get()
        # subtract points from the total points
        remainingPoints = points - currentPoints
        # update the points label
        TodaysPoints.configure(text="Today's Points Remaining: " + str(remainingPoints))

        print("this is the money response from the AI")

        # run AI to get a response
        makeMoneyresponse = openai.Completion.create(
            model="text-davinci-002",
            prompt="How can I make money while doing " + theTask,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
            )
        print(makeMoneyresponse.choices[0].text)
        # add the AI response to the AI response under time
        #moneyListBox.insert(tk.END, makeMoneyresponse.choices[0].text)
        #moneyListBox.grid(row=1, column=0)

        print("this is the Time response from the AI")

        getDoneFasterresponse = openai.Completion.create(
            model="text-davinci-002",
            prompt="Brainstorm some unique ideas that can get" + theTask + "done way faster",
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
            )
        print(getDoneFasterresponse.choices[0].text)

        # add the AI response to the AI response under time
        TimelistBox.insert(tk.END, getDoneFasterresponse.choices[0].text)

        print("this is the Lazy response from the AI")

        lazyWayresponse = openai.Completion.create(
            model="text-davinci-002",
            prompt="Brainstorm some SUPER lazy ways to accomplish" + theTask,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
            )
        print(lazyWayresponse.choices[0].text)

        # add the AI response to the AI response under time
        lazyListBox.insert(tk.END, lazyWayresponse.choices[0].text)

        # fit the AI response to the list box
        


        moneyListBox.grid(row=1, column=0)
        TimelistBox.grid(row=1, column=1)
        lazyListBox.grid(row=1, column=2)

        # add moneyresponse to the money window
        aiResponseLabel = tk.Label(moneyWindow, text=makeMoneyresponse.choices[0].text, font=("Helvetica", 20), fg="black", bg="#ffffff")
        aiResponseLabel.place(x=30, y=0)

        moneyWayLabel = tk.Label(moneyWindow, text="How to make money doing Your task", font=("Helvetica", 20), fg="black", bg="#ffffff")
        moneyWayLabel.place(x=00, y=0)

        

        # only allow the aiResponseLabel to be 30 words long and then go the the next line  
        aiResponseLabel.configure(wraplength=400)

        # add timeresponse to the money window
        aiResponseLabel2 = tk.Label(moneyWindow, text=getDoneFasterresponse.choices[0].text, font=("Helvetica", 20), fg="black", bg="#ffffff")
        aiResponseLabel2.place(x=430, y=0)

        timeWayLabel = tk.Label(moneyWindow, text="How to get your task done faster", font=("Helvetica", 20), fg="black", bg="#ffffff")
        timeWayLabel.place(x=400, y=0)


        # only allow the aiResponseLabel to be 30 words long and then go the the next line
        aiResponseLabel2.configure(wraplength=400)

        # add lazyresponse to the money window
        aiResponseLabel3 = tk.Label(moneyWindow, text=lazyWayresponse.choices[0].text, font=("Helvetica", 20), fg="black", bg="#ffffff")
        aiResponseLabel3.place(x=30, y=400)

        lazyWayLabel = tk.Label(moneyWindow, text="Lazy Way", font=("Helvetica", 20), fg="black", bg="#ffffff")
        lazyWayLabel.place(x=30, y=350)

        # only allow the aiResponseLabel to be 30 words long and then go the the next line
        aiResponseLabel3.configure(wraplength=400)




        

        



        askTime = openai.Completion.create(
            model="text-curie-001",
            prompt="on a scale of 1-100 how many points show this task of" + theTask + "is worth?",
            temperature=0.6,
            max_tokens=150,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=1
            )
        print(askTime.choices[0].text)
    

    

        def removeTodaysTasks():
            global player1Points
            todaysTasksLabel.destroy()
            print("removed")
        
            print("deleted")
            # give the player points for the task
            player1Points = player1Points + currentPoints
            player1Score.configure(text="Score: " + str(player1Points))


        def removeTodaysTasks2(self):
            global player2Points
            todaysTasksLabel.destroy()
            print("removed")
        
            print("deleted")
            # give the player points for the task
            player2Points = player2Points + currentPoints
            player2Score.configure(text="Score: " + str(player2Points))

        def deleteTask(self):
            todaysTasksLabel.destroy()
            print("deleted")



        todaysTasksLabel = tk.Button(GameFrame, text= str(theTask) + " - " + str(currentPoints) + " points", font=("Helvetica", 20), fg="black", command=removeTodaysTasks)
        # place the label at the top of the screen and each new label underneath it
        ranX = random.randint(0, 200)
        ranY = random.randint(0, 350)
        # when right click is pressed, remove the task and give the player 2 points
        todaysTasksLabel.bind("<Button-2>", removeTodaysTasks2)
        todaysTasksLabel.bind("<Button-3>", deleteTask)

        # update todaysTasksLabel text

        listBox.insert(tk.END, str(theTask) + " - " + str(askTime.choices[0].text) + " points")
    
    

    


def resetPlayersPoints():
    global player1Points
    global player2Points
    player1Points = 0
    player2Points = 0

    player1Score.configure(text="Score: " + str(player1Points))
    player2Score.configure(text="Score: " + str(player2Points))


# create button to reset the players points
resetPoints = tk.Button(SettingsFrame, text="Reset Points", font=("Helvetica", 20), fg="black", command=resetPlayersPoints)
resetPoints.place(x=300, y=0)




# submit the form when the uses presses enter
todaysTasks.bind("<Return>", lambda event: summitTodaysTasks())






def saveList():
    #we will open a file(in write mode) and write the required contents
    #with checklist.txt opened in write mode named as f for your future reference
    with open("checklist.txt","w") as f:
        #pass
        listTuple = listBox.get(0,tk.END)
        
        for items in listTuple:
            f.write(items+"\n")

    # save players points
    with open("player1Points.txt","w") as f:
        f.write(str(player1Points))
    with open("player2Points.txt","w") as f:
        f.write(str(player2Points))


def openList():
    try:
        with open("checklist.txt","r") as f:
            for line in f:
                listBox.insert(tk.END,line)
    except:
        pass  

    try:
        with open("player1Points.txt","r") as f:
            player1Points = int(f.read())
            player1Score.configure(text="Score: " + str(player1Points))
            print(player1Points)
    except:
        pass
    try:
        with open("player2Points.txt","r") as f:
            player2Points = int(f.read())
            player2Score.configure(text="Score: " + str(player2Points))
            print(player2Points)
    except:
        pass


def clearList():
        listBox.delete(0,tk.END)

# create a button to save the list
saveList = tk.Button(SettingsFrame, text="Save List", font=("Helvetica", 20), fg="black", command=saveList)
saveList.place(x=643, y=130)

# create button to clear the list
clearList = tk.Button(SettingsFrame, text="Clear List", font=("Helvetica", 20), fg="black", command=clearList)
clearList.place(x=643, y=50)

def removeItemAndGivePoints():
    global player1Points
    # get the current task
    currentTask = listBox.get(listBox.curselection())
    # remove the task from the list
    listBox.delete(listBox.curselection())
    # get the points from the task
    currentPointsOnText = currentTask.split(" ")[-2]
    print(currentPointsOnText)
    # give the player points for the task
    player1Points = player1Points + int(currentPointsOnText)
    player1Score.configure(text="Score: " + str(player1Points))
    playsound('Pop.mp3')

def removeItemAndGivePoints2():
    global player2Points
    # get the current task
    currentTask = listBox.get(listBox.curselection())
    # remove the task from the list
    listBox.delete(listBox.curselection())
    # get the points from the task
    currentPointsOnText = currentTask.split(" ")[-2]
    print(currentPointsOnText)
    # give the player points for the task
    player2Points = player2Points + int(currentPointsOnText)
    player2Score.configure(text="Score: " + str(player2Points))
    playsound('Pop.mp3')

# create button to removeItemAndGivePoints
removeItemAndGivePoints = tk.Button(SettingsFrame, text="Give Player 1 The Points", font=("Helvetica", 20), fg="black", command=removeItemAndGivePoints)
removeItemAndGivePoints.place(x=0, y=120)

# create button to removeItemAndGivePoints2
removeItemAndGivePoints2 = tk.Button(SettingsFrame, text="Give Player 2 The Points", font=("Helvetica", 20), fg="black", command=removeItemAndGivePoints2)
removeItemAndGivePoints2.place(x=300, y=120)

def openAdminsWindowPopup():
    # create a popup window
    adminWindow = tk.Toplevel()
    adminWindow.title("Admin Window")
    adminWindow.geometry("300x300")

    # create a label that says "enter points to give to player 1"
    adminLabel = tk.Label(adminWindow, text="Enter points to give to player", font=("Helvetica", 20), fg="black")
    adminLabel.place(x=0, y=0)

    # create a text box to enter the points
    adminTextBox = tk.Entry(adminWindow, font=("Helvetica", 20), fg="black")
    adminTextBox.place(x=0, y=50)




    def givePointsToPlayer1():
        # get the points from the text box
        points = adminTextBox.get()
        # give the player points
        global player1Points
        player1Points = player1Points + int(points)
        player1Score.configure(text="Score: " + str(player1Points))
        # close the popup window
        adminWindow.destroy()
    
    # create a button to give the points
    givePoints = tk.Button(adminWindow, text="Give Points To Player 1", font=("Helvetica", 20), fg="black", command=givePointsToPlayer1)
    givePoints.place(x=0, y=100)

    def givePointsToPlayer2():
        # get the points from the text box
        points = adminTextBox.get()
        # give the player points
        global player2Points
        player2Points = player2Points + int(points)
        player2Score.configure(text="Score: " + str(player2Points))
        # close the popup window
        adminWindow.destroy()

    # create a button to give the points
    givePoints2 = tk.Button(adminWindow, text="Give Points To Player 2", font=("Helvetica", 20), fg="black", command=givePointsToPlayer2)
    givePoints2.place(x=0, y=150)

    def closeAdminWindow():
        adminWindow.destroy()
    # create a button to close the popup window
    closeAdminWindow = tk.Button(adminWindow, text="Close", font=("Helvetica", 20), fg="black", command=closeAdminWindow)
    closeAdminWindow.place(x=0, y=200)





# create button to open admins Window
openAdminsWindow = tk.Button(SettingsFrame, text="Admin", font=("Helvetica", 20), fg="black", command=openAdminsWindowPopup)
openAdminsWindow.place(x=643, y=85)


# create a canvas with create 3 columns with a header on each column
aiCanvas = tk.Canvas(GameWindow, width=1000, height=500, bg="white")
aiCanvas.place(x=0, y=600)


aiCanvas.create_line(0, 0, 1000, 0, fill="black")
aiCanvas.create_line(0, 0, 0, 500, fill="black")
aiCanvas.create_line(0, 500, 1000, 500, fill="black")
aiCanvas.create_line(1000, 0, 1000, 500, fill="black")

aiCanvas.create_line(250, 0, 250, 500, fill="black")
aiCanvas.create_line(500, 0, 500, 500, fill="black")

aiCanvas.create_text(35, 20, text="Time", font=("Helvetica", 20), fill="black")
aiCanvas.create_text(285, 20, text="Money", font=("Helvetica", 20), fill="black")
aiCanvas.create_text(575, 20, text="The Lazy Way", font=("Helvetica", 20), fill="black")

TimelistBox = tk.Listbox(aiCanvas, font=("Helvetica", 20), fg="white", bg="black")
TimelistBox.place(x=0, y=50)
# make the listbox scrollable with a scrollbar and keep all text in the listbox
TimelistScrollbar = tk.Scrollbar(TimelistBox, orient="vertical")

TimelistBox.config(yscrollcommand=TimelistScrollbar.set)
TimelistScrollbar.config(command=TimelistBox.yview)


moneyListBox = tk.Canvas(aiCanvas, width=1000, height=500, bg="white")
moneyListBox.place(x=250, y=50)

lazyListBox = tk.Listbox(aiCanvas, font=("Helvetica", 20), fg="white", bg="black")
lazyListBox.place(x=500, y=50)





# open a new window called moneyWindow
moneyWindow = tk.Toplevel()
moneyWindow.title("Money Window")
moneyWindow.geometry("300x300")


# add label for AI response
aiResponseLabel = tk.Label(moneyWindow, text="AI Response", font=("Helvetica", 20), fg="black")
aiResponseLabel.place(x=0, y=0)



openList()
GameWindow.mainloop()

