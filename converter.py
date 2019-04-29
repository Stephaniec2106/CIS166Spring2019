#name: Stephanie Camacho
#module: converter.py
#date: 04/28/2019
#description: This program will convert pounds into grams, kilograms & ounces.
# A valid number must be entered or a message will display "invalid input please enter a # under the entry"


from graphics import *

def convert():

    win = GraphWin("converter",500,500)

    modTitle = Text(Point(250,50),"Weight Converter")
    modTitle.setFace("arial")
    modTitle.setSize(20)
    modTitle.setStyle("bold")
    modTitle.draw(win)

    Text(Point(415,100),"lb(s)").draw(win)
    lbinput = Entry(Point(250,100),30)
    lbinput.setFill("white")
    lbinput.setText("0.0")
    lbinput.draw(win)

    Button = Rectangle(Point(370,400),Point(460,450))
    Button.setFill("orange")
    Button.setOutline("orange")
    Button.draw(win)
    buttonLabel = Text(Point(415,425),"Convert")
    buttonLabel.setTextColor("white")    
    buttonLabel.draw(win)

    Text(Point(140,180),"Grams:").draw(win)
    gBox = Rectangle(Point(110,190),Point(300,220))
    gBox.setFill("White")
    gBox.draw(win)
    goutput = Text(Point(205,205),"0.0").draw(win)
    Text(Point(150,250),"Kilograms:").draw(win)
    kBox = Rectangle(Point(110,263),Point(300,293))
    kBox.setFill("White")
    kBox.draw(win)
    koutput = Text(Point(205,278),"0.0").draw(win)
    Text(Point(140,320),"Ounces:").draw(win)
    oBox = Rectangle(Point(110,330),Point(300,360))
    oBox.setFill("White")
    oBox.draw(win)
    ooutput = Text(Point(205,345),"0.0").draw(win)
    error = Text(Point(250,130),"")

    i = 0
    while i <=10:

        win.getMouse()

        try:

            int(lbinput.getText())
    
        except ValueError:
        
            error.setText("Invalid input, please enter a number under the entry")
            error.setTextColor("red")
            error.draw(win)
            goutput.setText("n/a")
            koutput.setText("n/a")
            ooutput.setText("n/a")
            continue

        else:
            lb = int(lbinput.getText())
      
            g = lb * 453.592
            goutput.setText("%0.2f" % g)
            kg = lb * 0.453592
            koutput.setText("%0.2f" % kg)
            oz = lb * 16.0
            ooutput.setText("%0.2f" % oz)
            error.setText(" ")

convert()

    
