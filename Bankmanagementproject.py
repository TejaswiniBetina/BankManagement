
import random
Options = '''
1   Create account
2   login
3   Credit
4   Debit
5   Transfer
6   Check Balance
7   Exit
'''
login_credentials = {}
Balance = 1000

Amount = 0

def Create_account(username,password):
    login_credentials[username] = {"password":password , "email":email}
    return(login_credentials)

def Generate_passwords(length=8):
    password = ""
    for index in range(length):
        value = random.randint(1, 10)
        password += str(value)
    return password

def login(username, password):
    if username in login_credentials:
        if password == login_credentials[username]["password"]:
            print("Welcome to City Bank of Country")
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")
   
   

def credit(Amount):
    global Balance
    Balance += Amount
    return(Balance)

def debit(Amount):
    global Balance
    if Amount <= Balance:
       Balance -= Amount
       return(Balance)
    else:
        return("insufficient Balance")
    
def Transfer(Amount):

    global Balance
    
    if Amount <= Balance:
        Balance -= Amount
        print("Amount transferred successfully.")
        print("Updated balance:", Balance)
    else:
        print("Insufficient funds.")

    return Balance  


    
def CheckBalance():
    print(Balance)


while True:
    Options = int(input("Enter option:  "))

    if Options == 1:
        username = input("Enter the username: ").lower()
        email = input("Enter the emailid: ").lower()
        print("Need to generate password Randomly Enter Option 1")
        print("Need to create specific password Enter Option 2")
        Subchoice = int(input("Enter option:  "))

        if Subchoice == 1:
            password = Generate_passwords()
            Create_account(username, password)
            print("Randomly generated password:", password)
            print("Login credentials saved successfully.")

        elif Subchoice == 2:
            password = input("Enter the password: ").lower()
            Create_account(username, password)
            print("Login credentials saved successfully.")

        else:
            print("Please enter the correct option to create password")

    elif Options == 2:
        username = input("Enter the username: ").lower()
        password = input("Enter the password: ").lower()
        login(username, password)

    
    elif Options == 3:
        Amount = int(input("Enter the amount: "))
        print("Amount is Credited Succesfully")
        print(f"The Total Balance:", credit(Amount))
        

    elif Options == 4:
         Amount = int(input("Enter the amount: "))
         print("Amount is Debited Sucessfully")
         print(f"The totalBlance is:",debit(Amount))

    elif Options == 5:
        Account = input("Enter the account Number: ")
        Name = input("Enter the Recipient name: ").upper()
        Amount = int(input("Enter the amount: "))
        Bank = input("Enter the Bank name: ").upper()
        print(f"Amount is Transferred to {Name} Successfully")
        print(Transfer(Amount))


    elif Options == 6:
        print(f"The current Balance is:",Balance)

    elif Options == 7:
        print("Thank you for visting Online City Bank service")
        break

    else:
        print("Invalid Options please select the proper option")

    
          









    