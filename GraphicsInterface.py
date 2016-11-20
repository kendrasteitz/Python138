
from graphics import*
from Button import Button
from dieview2 import DieView

class GraphicsInterface:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300, 100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        self.helper = Button(self.win, Point(30, 375), 40, 30, "help")
        self.helper.activate()
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"

    def close(self):
        self.win.close()

    def chooseDice(self):
        choices = []
        while True:
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", "Roll Dice", "Score"])
            if b[0] == "D":
                i = eval(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices

    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.getMouse()
            if self.helper.clicked(p):
                self.helpMenu()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()


    def helpMenu(self):
        win = GraphWin("Help", 500, 300)
        win.setCoords(0, 0, 50, 50)
        win.setBackground("orange")

        banner = Text(Point(25, 46), "Payout Table")
        banner.setSize(16)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Rectangle(Point(3, 9), Point(47, 38)).draw(win)
        Rectangle(Point(3, 38), Point(47, 42)).draw(win)

        Text(Point(6, 40), "Hand").draw(win)
        Text(Point(45, 40), "Pay").draw(win)
        Text(Point(7, 35), "Two Pairs").draw(win)
        Text(Point(45, 35), "5").draw(win)
        Text(Point(9, 31), "Three of a Kind ").draw(win)
        Text(Point(45, 31), "8").draw(win)
        Text(Point(18, 27), "Full House (A Pair and a Three of a Kind) ").draw(win)
        Text(Point(45, 27), "12").draw(win)
        Text(Point(9, 23), "Four of a Kind   ").draw(win)
        Text(Point(45, 23), "15").draw(win)
        Text(Point(12, 19), "Straight (1 - 5 or 2 - 6)     ").draw(win)
        Text(Point(45, 19), "20").draw(win)
        Text(Point(9, 15), "Five of a Kind   ").draw(win)
        Text(Point(45, 15), "30").draw(win)

        exit = Button(win, Point(25, 4), 10, 4, "Exit")
        exit.activate()
        pt = win.getMouse()
        while not exit.clicked(pt):
            pt = win.getMouse()
        if exit.clicked(pt):
            win.close()