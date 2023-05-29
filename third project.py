from breezypythongui import EasyFrame
import random
"""MADE BY:-
HARPREET
"""
"""THIS CODE IS WRITTEN TO MAKE A GAMBLING GAME ON THE RACE OF ANIMALS.USER CAN BET ON THE ANIMALS TO WIN THE PRIZES."""
def win(self):
    print("you won")
    class CheckbuttonDemo(EasyFrame):
        def __init__(self):
            """this checkbutton is used to display the winning prizes but user have to select one of the button"""
            EasyFrame.__init__(self,"check Button demo")
            self.gurpartap=self.addCheckbutton(text="open the Ist pendora",row=0,column=0)
            self.harpreet=self.addCheckbutton(text="open the 2nd pendora",row=0,column=1)
            self.aditya=self.addCheckbutton(text="open the 3rd pendora",row=1,column=0)
            self.jasdeepgurkirat=self.addCheckbutton(text="open the 4th pendora",row=1,column=1)

            #Add the command button
            self.addButton(text="Let's check what you won",row=2,column=0,columnspan=2,command=self.placeOrder)
        def placeOrder(self):
            msg=""
            if self.gurpartap.isChecked():
                msg+="$5,000\n\n"

            if self.harpreet.isChecked():
                msg+="$1,000\n\n"
                                     
            if self.aditya.isChecked():
                msg+="$2000\n\n"
            if self.jasdeepgurkirat.isChecked():
                msg+="$500\n\n"
            if msg=="":
                msg="Nothing selected!"
            self.messageBox(title="GAMBLING PRIZE",message=msg)
    CheckbuttonDemo().mainloop()  
    
def lose(self):
    print("Sorry you lose ): ")
    
class PrompterBoxDemo(EasyFrame):
    def __init__(self):
        """this is used to get the name of user who wants to play the gambling game"""
        EasyFrame.__init__(self,title="The Gambling Game",width=600,height=200)
        self.label=self.addLabel(text="",row=0,column=0)
        self.addButton(text="Please enter your name to play the game",row=1,column=0,command=self.getUserName)
    def getUserName(self):
        name=self.prompterBox(title="Input Dialog",promptString="your Username")
        self.label["text"]="Hi " + name +"! .Hope you are doing good.Please cancel this prompter box to start playing the game."
PrompterBoxDemo().mainloop()

from breezypythongui import EasyFrame
class TextAreaDemo(EasyFrame):
    def __init__(self):
        """To see the rules of this gambling game"""
        EasyFrame.__init__(self,"GAMING RULES")
        self.addLabel(text="OVERVIEW",row=0,column=0)
        self.overview=self.addFloatField(value="SEE THE RULES",row=0,column=1)
        self.rules=self.addButton(text="RULES",row=3,column=0,columnspan=2,command=self.rule)
        self.outputArea=self.addTextArea("",row=4,column=0,columnspan=2,width=50,height=15)
        


        
    def rule(self):
        result ='''1.Select the animal you think will win and place the bet.
2.If you win select the prize from the checkbox
3.Consequences of loosing will be displayed.






##please close this window to start the gambling game##'''
        self.outputArea.setText(result)
li = ["Drunk Horse", "Drunk Cat", "Smart Dog", "Weird Cheetah", "Angry Bull", "Sleepy Rabbit"]
        
TextAreaDemo().mainloop()
class Buttons_and_result(EasyFrame):
    
    def __init__(self):
        """these buttons are used to display the names of running animals and user can select one of the animal to make a bet."""
        
        EasyFrame.__init__(self)
        self.label1=self.addLabel(text="Place your bet on who will win the race.",row=0,column=0,columnspan=2)
        self.label2=self.addLabel(text= "",row=5,column=0,columnspan=2)
        self.button1=self.addButton(text="Drunk Horse",row=1,column=0,command=self.b1)
        self.button2=self.addButton(text="Drunk Cat",row=1,column=1,command=self.b2)
        self.button3=self.addButton(text="Smart Dog",row=1,column=2,command=self.b3)
        self.button4=self.addButton(text="Weird Cheetah",row=2,column=0,command=self.b4)
        self.button5=self.addButton(text="Angry Bull",row=2,column=1,command=self.b5)
        self.button6=self.addButton(text="Sleepy Rabbit",row=2,column=2,command=self.b6)
        self.label3=self.addLabel(text="",row = 4,column = 0,columnspan = 2)
        
      
    def b1(self):
        winning_number = random.choice(li)
        y = "Drunk Horse"
    
        self.button2["state"]="disabled"
        self.button3["state"]="disabled"
        self.button4["state"]="disabled"
        self.button5["state"]="disabled"
        self.button6["state"]="disabled"
        if y == winning_number:
            self.label2["text"] = "your drunk horse won!, please jump to the next window to continue"
            
            return win(self)
        else:
            self.button1["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"
            self.label2["text"] = "your horse was too drunk to win please close this window to try again"
            return lose(self)
            
    def b2(self):
        winning_number = random.choice(li)
        y = "Drunk Cat"
        self.button1["state"]="disabled"
        
        self.button3["state"]="disabled"
        self.button4["state"]="disabled"
        self.button5["state"]="disabled"
        self.button6["state"]="disabled"
        if y == winning_number:
            self.label2["text"] = "your drunk cat won !please jump to the next window to continue"
            return win(self)
        else:
            self.button2["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"
            self.label2["text"] = "your cat was too drunk please close this window to try again"
            return lose(self)
        
        
    def b3(self):
        winning_number = random.choice(li)
        y = "Smart Dog"
        self.button1["state"]="disabled"
        self.button2["state"]="disabled"
        
        self.button4["state"]="disabled"
        self.button5["state"]="disabled"
        self.button6["state"]="disabled"
        if y == winning_number:
            self.label2["text"] = "your Smart Dog won! please jump to the next window to continue"
            return win(self)
        else:
            self.button3["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"
            self.label2["text"] = "you lost please close this window to try again"
            return lose(self)
        
    def b4(self):
        winning_number = random.choice(li)
        y = "Weird Cheetah"
        self.button1["state"]="disabled"
        self.button2["state"]="disabled"
        self.button3["state"]="disabled"
        
        self.button5["state"]="disabled"
        self.button6["state"]="disabled"
        if y == winning_number:
            self.label2["text"] = "your Weird cheetah  won !please jump to the next window to continue"
            return win(self)
        else:
            self.button4["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"
            self.label2["text"] = "your cheetah was too weird to win please close this window to try again"
            return lose(self)
        
    def b5(self):
        winning_number = random.choice(li)
        y = "Angry Bull"
        self.button1["state"]="disabled"
        self.button2["state"]="disabled"
        self.button3["state"]="disabled"
        self.button4["state"]="disabled"
        
        self.button6["state"]="disabled"
        if y == winning_number:
            self.label2["text"] = "your Angry Bull won ! please jump to the next window to continue"
            return win(self) 
        else:
            self.button5["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"
            self.label2["text"] = "your bull had a mental breakdown to win please close this window to try again"
            return lose(self)
        
    def b6(self):
        winning_number = random.choice(li)
        y  = "Sleepy Rabbit"
        self.button1["state"]="disabled"
        self.button2["state"]="disabled"
        self.button3["state"]="disabled"
        self.button4["state"]="disabled"
        self.button5["state"]="disabled"

        if y == winning_number:
            self.label2["text"] = "your Sleepy Rabbit won !please jump to the next window to continue"
            return win(self)
        else:
            self.button6["state"]="disabled"
            self.label3["text"] = "sorry this time ", winning_number, "won by chance"

            self.label2["text"] = "your rabbit slept before the race get started please close this window to try again"
            return lose(self)
Buttons_and_result().mainloop()
