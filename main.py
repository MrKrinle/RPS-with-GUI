
import random
import tkinter as tk
import tkinter.font as tkFont
import webbrowser
import os
import sys


i = 0
out = [0, 0, 0] #The order here is Wins, Losses, Ties


def check_win(player):
      global i
      global out
      options = ['rock', 'paper', 'scissors']
      computer = random.choice(options)
      if player == computer:
        out[2] += 1
        GMessage_735["text"] = "It's a tie!"
      elif player == 'rock':
        if computer == 'scissors':
          out[0] += 1
          GMessage_735["text"] = 'Rock smashes scissors! You win!'
        else:
          out[1] += 1
          GMessage_735["text"] = 'Paper covers rock! You lost!'
      elif player == 'paper':
        if computer == 'rock':
          out[0] += 1
          GMessage_735["text"] = 'Paper covers rock! You win!'
        else:
          out[1] += 1
          GMessage_735["text"] = 'Scissors cuts paper! You lost!'
      elif player == 'scissors':
        if computer == 'paper':
          out[0] += 1
          GMessage_735["text"] = 'Scissors cuts paper! You win!'
        else:
          out[1] += 1
          GMessage_735["text"] = 'Rock smashes scissors! You lost!'
      if out[1] == i and i != 0:
          GMessage_735["text"] =  'You have lost the game!'
          out = [0, 0, 0]
          
      Update_score()
      

def Update_score():
    GLabel_793["text"] = 'Wins: ' + str(out[0])
    GLabel_989["text"] = "Losses: " + str(out[1])
    GLabel_698["text"] = "Ties: " + str(out[2])

def Game_end():  
    if out[1] == i and i != 0:
        input()
        time.sleep(3)
        os.execv(sys.executable, ['python'] +  sys.argv)

global GMessage_735
global GLabel_793
global GLabel_989
global GLabel_698

class App:
            
    def __init__(self, root):
        global GMessage_735
        global GLabel_793
        global GLabel_989
        global GLabel_698
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        GMessage_735=tk.Message(root)
        GMessage_735["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=32)
        GMessage_735["font"] = ft
        GMessage_735["fg"] = "#f8f4f4"
        GMessage_735["justify"] = "center"
        GMessage_735["text"] = "This is my Rock Paper Scissors game!"
        GMessage_735.place(x=80,y=30,width=418,height=223)

        GButton_918=tk.Button(root)
        GButton_918["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=18)
        GButton_918["font"] = ft
        GButton_918["fg"] = "#000000"
        GButton_918["justify"] = "center"
        GButton_918["text"] = "Rock"
        GButton_918.place(x=30,y=325,width=125,height=37)
        GButton_918["command"] = self.GButton_918_command

        GButton_533=tk.Button(root)
        GButton_533["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=18)
        GButton_533["font"] = ft
        GButton_533["fg"] = "#000000"
        GButton_533["justify"] = "center"
        GButton_533["text"] = "Paper"
        GButton_533.place(x=220,y=325,width=125,height=37)
        GButton_533["command"] = self.GButton_533_command

        GButton_832=tk.Button(root)
        GButton_832["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=18)
        GButton_832["font"] = ft
        GButton_832["fg"] = "#000000"
        GButton_832["justify"] = "center"
        GButton_832["text"] = "Scissors"
        GButton_832.place(x=410,y=325,width=125,height=37)
        GButton_832["command"] = self.GButton_832_command

        GLabel_793=tk.Label(root)
        GLabel_793["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_793["font"] = ft
        GLabel_793["fg"] = "#f8f4f4"
        GLabel_793["justify"] = "left"
        GLabel_793["text"] = "Wins: 0"
        GLabel_793.place(x=80,y=250,width=143,height=41)

        GLabel_989=tk.Label(root)
        GLabel_989["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_989["font"] = ft
        GLabel_989["fg"] = "#f8f4f4"
        GLabel_989["justify"] = "left"
        GLabel_989["text"] = "Losses: 0"
        GLabel_989.place(x=220,y=250,width=143,height=41)

        GLabel_698=tk.Label(root)
        GLabel_698["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_698["font"] = ft
        GLabel_698["fg"] = "#f8f4f4"
        GLabel_698["justify"] = "left"
        GLabel_698["text"] = "Ties: 0"
        GLabel_698.place(x=362,y=251,width=136,height=40)

        GButton_291=tk.Button(root)
        GButton_291["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=13)
        GButton_291["font"] = ft
        GButton_291["fg"] = "#000000"
        GButton_291["justify"] = "center"
        GButton_291["text"] = "RESET"
        GButton_291.place(x=520,y=420,width=71,height=30)
        GButton_291["command"] = self.GButton_291_command

        GButton_163=tk.Button(root)
        GButton_163["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_163["font"] = ft
        GButton_163["fg"] = "#000000"
        GButton_163["justify"] = "center"
        GButton_163["text"] = "Secret"
        GButton_163.place(x=20,y=440,width=104,height=34)
        GButton_163["command"] = self.GButton_163_command

        GButton_371=tk.Button(root)
        GButton_371["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_371["font"] = ft
        GButton_371["fg"] = "#000000"
        GButton_371["justify"] = "center"
        GButton_371["text"] = "E"
        GButton_371.place(x=20,y=20,width=30,height=30)
        GButton_371["command"] = self.GButton_371_command

        GButton_97=tk.Button(root)
        GButton_97["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_97["font"] = ft
        GButton_97["fg"] = "#000000"
        GButton_97["justify"] = "center"
        GButton_97["text"] = "H"
        GButton_97.place(x=20,y=60,width=30,height=30)
        GButton_97["command"] = self.GButton_97_command

        GButton_449=tk.Button(root)
        GButton_449["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=18)
        GButton_449["font"] = ft
        GButton_449["fg"] = "#000000"
        GButton_449["justify"] = "center"
        GButton_449["text"] = "Exit"
        GButton_449.place(x=520,y=460,width=71,height=30)
        GButton_449["command"] = self.GButton_449_command

        

    def GButton_918_command(self):
        check_win('rock')


    def GButton_533_command(self):
        check_win('paper')


    def GButton_832_command(self):
        check_win('scissors')

    def GButton_291_command(self):
        os.execv(sys.executable, ['python'] +  sys.argv)

    def GButton_163_command(self):
        webbrowser.open('www.mrkrinle.com', new=1)

    def GButton_371_command(self):
        global i
        i = 10
        GMessage_735["text"] = 'You have chosen Easy mode! '


    def GButton_97_command(self):
        global i
        i = 2
        GMessage_735["text"] = 'You have chosen Hard mode! '

    def GButton_449_command(self):
        os._exit(0)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()





