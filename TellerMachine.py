
from graphics import*
from Button import Button

class TellerMachine():

    def __init__(self) -> object:
        self.bankAccounts = {}
        self.checkingAccounts = {}
        self.savingAccounts = {}
        self.idNumber = 0
        infile = open("C:/Users/kcste/Desktop/Python/hw12SteitzKendra/BankAccounts.txt", "r")

        for line in infile:
            self.idNumber, self.pinNumber, self.checking, savings = line.split()
            self.bankAccounts[self.idNumber] = self.pinNumber
            self.checkingAccounts[self.idNumber] = self.checking
            self.savingAccounts[self.idNumber] = savings

        infile.close()

    def setIDNumber(self, idNumb):
        self.idNumber = idNumb

    def getIDNumber(self):
        return self.idNumber

    def teller(self):
        win = GraphWin("Automatic Teller Machine (ATM)", 600, 400)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Welcome to Falcon Bank")
        banner.setSize(24)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)

        Image(Point(6, 9), "eagle.png").draw(win)

        Text(Point(15, 11), "Enter ID: ").draw(win)
        id = Entry(Point(20, 11), 10)
        id.setText(0)
        id.draw(win)

        Text(Point(15, 8), "Enter pin:").draw(win)
        pin = Entry(Point(20, 8), 10)
        pin.setText(0)
        pin.draw(win)

        submit = Button(win, Point(20, 3), 12, 2, "Enter")
        submit.activate()

        pt = win.getMouse()

        idNumb = eval(id.getText())
        pinNumb = eval(pin.getText())
        match = 0
        isValid = False

        for i in self.bankAccounts:
            if idNumb == int(i):
                match = match + 1
                p = self.bankAccounts.get(i, 'Error')
                if pinNumb == int(p):
                    self.setIDNumber(idNumb)
                    win.close()
                    self.accounts()
                    isValid = True
        if not isValid:
            win.close()
            self.error()


    def error(self):
        win = GraphWin("Error", 475, 250)
        win.setBackground("red")
        win.setCoords(0, 0, 20, 15)
        banner = Text(Point(14, 10), "Error")
        banner.setSize(29)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(5, 7), "eagle.png").draw(win)
        Text(Point(14, 5), "Invalid ID or pin number").draw(win)
        Text(Point(14, 4), "Please try again").draw(win)

        pt = win.getMouse()
        win.close()

    def accounts(self):
        win = GraphWin("Automatic Teller Machine (ATM)", 550, 350)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Welcome to Falcon Bank")
        banner.setSize(24)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(7, 8), "eagle.png").draw(win)
        withdraw = Button(win, Point(21, 11), 11, 2.5, "Withdrawal")
        withdraw.activate()
        deposit = Button(win, Point(21, 7), 11, 2.5, "Deposit")
        deposit.activate()
        transfer = Button(win, Point(21, 3), 11, 2.5, "Transfer")
        transfer.activate()

        pt = win.getMouse()
        win.close()

        if withdraw.clicked(pt):
            self.withdrawal()
        if deposit.clicked(pt):
            self.deposit()
        if transfer.clicked(pt):
            self.transfer()

    def withdrawal(self):
        win = GraphWin("Withdrawal", 550, 375)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Which account would you like to\nmake a withdrawal from?")
        banner.setSize(17)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(7, 8), "eagle.png").draw(win)
        check = Button(win, Point(21, 9), 11, 3, "Checking")
        check.activate()
        saving = Button(win, Point(21, 4), 11, 3, "Savings")
        saving.activate()

        key = self.getIDNumber()
        pt = win.getMouse()
        win.close()

        if check.clicked(pt):
            win = GraphWin("Checking", 550, 300)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 15),
                 "You have {0} in your account".format(self.checkingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to withdrawal?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Withdraw")
            calculate.activate()
            win.getMouse()
            withdrawn = eval(amount.getText())
            total = self.checkingAccounts.get(str(key), 'Error')
            newTotal = float(total) - float(withdrawn)
            del self.checkingAccounts[str(key)]
            self.checkingAccounts[str(key)] = str(newTotal)

        if saving.clicked(pt):
            win = GraphWin("Savings", 550, 300)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 15),
                 "You have {0} in your account".format(self.savingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to withdrawal?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Withdraw")
            calculate.activate()
            win.getMouse()
            withdrawn = eval(amount.getText())
            total = self.savingAccounts.get(str(key), 'Error')
            newTotal = float(total) - float(withdrawn)
            del self.savingAccounts[str(key)]
            self.savingAccounts[str(key)] = str(newTotal)

        self.saveInfo()
        win.close()
        self.anotherTrans()

    def deposit(self):
        win = GraphWin("Deposit", 550, 375)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Which account would you like to\nmake a deposit into?")
        banner.setSize(17)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(7, 8), "eagle.png").draw(win)
        check = Button(win, Point(21, 9), 11, 3, "Checking")
        check.activate()
        saving = Button(win, Point(21, 4), 11, 3, "Savings")
        saving.activate()

        pt = win.getMouse()
        key = self.getIDNumber()
        win.close()

        if check.clicked(pt):
            win = GraphWin("Checking", 550, 300)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 15),
                 "You have {0} in your account".format(self.checkingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to deposit?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Deposit")
            calculate.activate()
            win.getMouse()
            deposit = eval(amount.getText())
            total = self.checkingAccounts.get(str(key), 'Error')
            newTotal = float(total) + float(deposit)
            del self.checkingAccounts[str(key)]
            self.checkingAccounts[str(key)] = str(newTotal)

        if saving.clicked(pt):
            win = GraphWin("Savings", 550, 300)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 15),
                 "You have {0} in your account".format(self.savingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to deposit?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Deposit")
            calculate.activate()
            win.getMouse()
            deposit = eval(amount.getText())
            total = self.savingAccounts.get(str(key), 'Error')
            newTotal = float(total) + float(deposit)
            del self.savingAccounts[str(key)]
            self.savingAccounts[str(key)] = str(newTotal)

        self.saveInfo()
        win.close()
        self.anotherTrans()

    def transfer(self):
        win = GraphWin("Transfer", 550, 375)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Which account would you like to \n transfer from?")
        banner.setSize(17)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(7, 8), "eagle.png").draw(win)
        check = Button(win, Point(21, 9), 11, 3, "Checking")
        check.activate()
        saving = Button(win, Point(21, 4), 11, 3, "Savings")
        saving.activate()

        pt = win.getMouse()
        key = self.getIDNumber()
        win.close()

        if check.clicked(pt):
            win = GraphWin("Checking", 550, 325)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 16),
                 "You have {0} in your account".format(self.checkingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to transfer \ninto your savings?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Transfer")
            calculate.activate()
            win.getMouse()
            withdrawn = eval(amount.getText())
            total = self.checkingAccounts.get(str(key), 'Error')
            newTotal = float(total) - float(withdrawn)
            del self.checkingAccounts[str(key)]
            self.checkingAccounts[str(key)] = str(newTotal)
            deposit = withdrawn
            total = self.savingAccounts.get(str(key), 'Error')
            newTotal = float(total) + float(deposit)
            del self.savingAccounts[str(key)]
            self.savingAccounts[str(key)] = str(newTotal)

        if saving.clicked(pt):
            win = GraphWin("Savings", 550, 325)
            win.setBackground("white")
            win.setCoords(0, 0, 30, 20)
            Text(Point(20, 16),
                 "You have {0} in your account".format(self.savingAccounts.get(str(key), 'Error'))).draw(win)
            Text(Point(20, 13), "How much would you like to transfer \ninto your checking?").draw(win)
            amount = Entry(Point(20, 7), 10)
            amount.setText("0")
            amount.draw(win)
            Image(Point(7, 10), "eagle.png").draw(win)
            calculate = Button(win, Point(20, 4), 10, 2.5, "Transfer")
            calculate.activate()
            win.getMouse()
            withdrawn = eval(amount.getText())
            total = self.savingAccounts.get(str(key), 'Error')
            newTotal = float(total) - float(withdrawn)
            del self.savingAccounts[str(key)]
            self.savingAccounts[str(key)] = str(newTotal)
            deposit = withdrawn
            total = self.checkingAccounts.get(str(key), 'Error')
            newTotal = float(total) + float(deposit)
            del self.checkingAccounts[str(key)]
            self.checkingAccounts[str(key)] = str(newTotal)

        self.saveInfo()
        win.close()
        self.anotherTrans()

    def saveInfo(self):
        outfile = open("C:/Users/kcste/Desktop/Python/hw12SteitzKendra/BankAccounts.txt", "w")
        for key in self.bankAccounts.keys():
            print(key + " " + self.bankAccounts.get(key, 'Error') + " " + self.checkingAccounts.get(key, 'Error') + " " +
                  self.savingAccounts.get(key, 'Error'), file=outfile)
        outfile.close()

    def anotherTrans(self):
        win = GraphWin("Transaction Complete", 550, 375)
        win.setBackground("gray")
        win.setCoords(0, 0, 30, 20)
        banner = Text(Point(15, 17), "Transaction Complete")
        banner.setSize(25)
        banner.setFill("black")
        banner.setStyle("bold")
        banner.draw(win)
        Image(Point(7, 8), "eagle.png").draw(win)
        Text(Point(20, 13), "Thank you for your business at Falcon Bank.").draw(win)
        Text(Point(20, 12), "Would you like to make another transaction?").draw(win)
        yes = Button(win, Point(21, 7), 11, 2.5, "Yes")
        yes.activate()
        no = Button(win, Point(21, 3), 11, 2.5, "No")
        no.activate()

        pt = win.getMouse()
        win.close()

        if yes.clicked(pt):
            self.__init__()
            self.teller()

        if no.clicked(pt):
            win = GraphWin("Thank You", 525, 250)
            win.setBackground("yellow")
            win.setCoords(0, 0, 20, 15)
            banner = Text(Point(14, 10), "Falcon Bank")
            banner.setSize(27)
            banner.setStyle("bold")
            banner.draw(win)
            Image(Point(5, 8), "eagle.png").draw(win)
            thanks = Text(Point(14, 6), "Thank you for your business \n Have a good day!")
            thanks.setStyle("bold")
            thanks.draw(win)

            win.getMouse()
            win.close()
