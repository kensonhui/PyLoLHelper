import tkinter as tk



def importData(tipsAgainst, coolDowns): ##insert data about champion into here
        t = tk.Label(tipsAgainst, text="Tips against playing " + "DATA")
        t.grid(row = 0, column = 0)
        t = tk.Label(tipsAgainst, text="Insert data here")
        t.grid(row = 1, column = 0)
        c = tk.Label(coolDowns, text="Cooldowns for this champion")
        c.grid(row = 0, column = 0)

def viewPlayer(event): ##create second window to view player and champion
    root2 = tk.Tk()
    root2.title(event.widget.cget("text"))
    tipsAgainst = tk.Canvas(root2)
    coolDowns = tk.Canvas(root2)
    tipsAgainst.pack()
    coolDowns.pack()
    importData(tipsAgainst, coolDowns)
    root2.mainloop()

def on_enter(event): ##when mouse hovers over button
    event.widget["background"] = "purple"

def on_exit(event): ##when mouse leaves button
    event.widget["background"] = "SystemButtonFace"

def Table(): ##create a canvas and fill it with all participants in game

    for i in range(2): 
        e = tk.Label(teamWindow, text = "Team " + str(i + 1), width=20, fg =("blue","red")[i is 0], font=('Arial',16,'bold')) 
        
        e.grid(row = 0, column = i)
        for j in range(5):  
            e = tk.Label(teamWindow, text= "Player " + str(i * 5 + j), width=20, fg=("blue","red")[i is 0], font=('Arial',16,'bold')) 
            e.bind('<Enter>', on_enter) ##when mouse hovers over name
            e.bind('<Button-1>', viewPlayer) ##when mouse clicks name
            e.bind('<Leave>', on_exit) ##when mouse leaves name
            e.grid(row=j + 1, column=i)

    teamWindow.pack()

def getSummoner ():  ##search function, if error then except
    x1 = entry1.get()
    try:
        textOutput.set("Searched for Summoner:" + " " + x1)
        t = Table()
    except ValueError: ## if search cannot find summoner, execute
        textOutput.set("Error summoner not found")

def quit () :
    root.destroy()
    exit()


root = tk.Tk()
root.title("PyLoLHelper - Search Page")

searchWindow = tk.Canvas(root, width = 400, height = 300)
searchWindow.pack()
title = tk.Label(root, fg="blue", font=("Impact", 24, 'bold'), text="PyLoLHelper")
searchWindow.create_window(200, 20, window=title)
try:
    logo = tk.PhotoImage(file="logo.gif")
    searchWindow.create_window(200,110, window=tk.Label(root, image=logo))
except:
    print("Logo.gif must be in same folder as python file!")
##search bar and submit button
entry1 = tk.Entry (root) 
searchWindow.create_window(200, 200, window=entry1)
textOutput = tk.StringVar()
label1 = tk.Label(root, textvariable = textOutput)

searchWindow.create_window(200, 270, window=label1)



button1 = tk.Button(text='Search for Summoner', command=getSummoner)
searchWindow.create_window(200, 220, window=button1)
quitButton = tk.Button(root, text='Quit', command=quit)
quitButton.pack()
teamWindow = tk.Canvas(root, width = 400, height = 300)



root.mainloop()
