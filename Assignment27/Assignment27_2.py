class BankAccount:
    # Class Varibale
    ROI = 10.5
    
    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
        
    # Display details
    def Display(self):
        print("Account Holder Name : ", self.Name)
        print("Current Balance : ", self.Amount)
        
    # Deposit money
    def Deposit(self):
        amt = float(input("Enter amount to deposit : "))
        self.Amount += amt
        print("Amount deposited successfully.")
        
    # Withdraw money
    def Withdraw(self):
        amt = float(input("Enter amount to withdraw : "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")
            
    # Calculate Interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest = ", interest)
        
# Main program
obj = BankAccount("Poonam", 10000)

obj.Display()
obj.Deposit()
obj.Display()

obj.Withdraw()
obj.Display()

obj.CalculateInterest()