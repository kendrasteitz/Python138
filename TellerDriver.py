# Exercise No.   2
# File Name:     ATM.py
# Programmer:    Kendra Steitz
# Date:          November 19, 2016
#
# Problem Statement:
#   Create a ATM that allows the user to deposit, withdraw, or transfer
#   money from their savings/checking account.
#
# Overall Plan:
#   1. Create a class for ATM (TellerMachine)
#   2. Define the initial data for the class
#       Read in the file that contains all the bank account information
#       Assign values into the correct python dictionary, the key is their ID number
#           bankAccounts(contains pin numbers)
#           checkingAccounts(contains the amount of money in their checking)
#           savingAccounts(contains the amount of money in their savings)
#   3. Create GUI asking user to enter their ID number and pin number
#       Check if pin matches ID - if not, output error message
#   4. If ID and pin match, go to next GUI asking user what they want to do
#       withdraw, deposit, or transfer
#   5. Depending on which choice the user makes, go to appropriate GUI asking user
#       whether from checking or savings
#   6. Depending on user choice, take to appropriate GUI and have user input the
#       amount they would like to use
#   7. Make the correct calculations, delete the value changed from the dictionary
#       and add the new information into it.
#   8. Write all the account information back onto txt file so to update any new values
#   9. Ask user if they would like to perform any more transactions
#       If so, take them back to the beginning
#


from TellerMachine import*

def main():

    inter = TellerMachine()
    inter.teller()

main()
