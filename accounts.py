
from graphics import*
from Button import Button

bankAccounts = {}
checkingAccounts = {}
savingAccounts = {}
idNumber = 0
infile = open("C:/Users/kcste/Desktop/Python/hw12SteitzKendra/BankAccounts.txt", "r")

for line in infile:
    idNumber, pinNumber, checking, savings = line.split()
    bankAccounts[idNumber] = pinNumber
    checkingAccounts[idNumber] = checking
    savingAccounts[idNumber] = savings

infile.close()

print(bankAccounts.items())
print(checkingAccounts.items())
print(savingAccounts.items())

def teller():

    win = GraphWin("Automatic Teller Machine (ATM)", 600, 400)
    win.setBackground("gray")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Welcome to the Bank")
    banner.setSize(24)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    Text(Point(14, 11), "Enter ID:").draw(win)
    id = Entry(Point(20, 11), 10)
    id.setText(" ")
    id.draw(win)

    Text(Point(14, 8), "Enter pin:").draw(win)
    pin = Entry(Point(20, 8), 10)
    pin.setText(" ")
    pin.draw(win)

    submit = Button(win, Point(20, 3), 12, 2, "Enter")
    submit.activate()

    pt = win.getMouse()

    idNumb = eval(id.getText())
    pinNumb = eval(pin.getText())
    match = 0

    for i in bankAccounts:
        if idNumb == int(i):
            match = match + 1
            p = bankAccounts.get(i, 'Error')
            if pinNumb == int(p):
                accounts()
            else:
                error()


def error():
    win = GraphWin("Error", 300, 150)
    win.setBackground("red")
    win.setCoords(0, 0, 6, 7)
    banner = Text(Point(3, 5), "Error")
    banner.setSize(29)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)
    Text(Point(3, 2), "Invalid ID or pin number").draw(win)

    pt = win.getMouse()


def accounts():
    win = GraphWin("Automatic Teller Machine (ATM)", 600, 400)
    win.setBackground("gray")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Welcome to the Bank")
    banner.setSize(24)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    withdraw = Button(win, Point(18, 10), 12, 3, "Withdrawal")
    withdraw.activate()
    deposit = Button(win, Point(18, 5), 12, 3, "Deposit")
    deposit.activate()

    pt = win.getMouse()

    if withdraw.clicked(pt):
        withdrawal()
    if deposit.clicked(pt):
        deposit()

    win.close()

def withdrawal():
    win = GraphWin("Withdrawal", 600, 400)
    win.setBackground("gray")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Which account would you like to\nmake a withdrawal from?")
    banner.setSize(17)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    check = Button(win, Point(18, 10), 12, 3, "Checking")
    check.activate()
    saving = Button(win, Point(18, 5), 12, 3, "Savings")
    saving.activate()

    pt = win.getMouse()

    if check.clicked(pt):
        print("Getting to it still")

    if saving.clicked(pt):
        deposit()

    win.close()

def deposit():
    win = GraphWin("Deposits", 600, 400)
    win.setBackground("gray")
    win.setCoords(0, 0, 30, 20)
    banner = Text(Point(15, 17), "Which account would you like to\nmake a deposit into?")
    banner.setSize(17)
    banner.setFill("black")
    banner.setStyle("bold")
    banner.draw(win)

    check = Button(win, Point(18, 10), 12, 3, "Checking")
    check.activate()
    saving = Button(win, Point(18, 5), 12, 3, "Savings")
    saving.activate()

    pt = win.getMouse()

    if check.clicked(pt):
        withdrawal()
    if saving.clicked(pt):
        deposit()

    win.close()


def main():

    teller()


main()