class Banking:
    def __init__(self, balance=0):
        # Initialize balance
        self.balance = balance

    def show_balance(self):
        # Show the current balance
        print(f"Current balance: {self.balance} RS")

    def deposit(self):
        while True:
            try:
                amount = float(input("Please enter the amount to deposit: \n"))
                if amount > 0:
                    self.balance += amount
                    print(f"The amount {amount} RS has been deposited")
                    break
                else:
                    print("Please enter a valid amount")
            except ValueError:
                print("Please enter a valid amount")

    def withdraw(self):
        while True:
            try:
                amount = float(input("Please enter the withdrawal amount: \n"))
                if amount > 0 and amount <= self.balance:
                    self.balance -= amount
                    print(f"The amount {amount} RS has been withdrawn")
                    break
                else:
                    print("Insufficient fund")
            except ValueError:
                print("Please enter a valid amount")

# Create a Banking object
transaction = Banking()

# List of possible transactions
list_of_transactions = {
    1: "1. show_balance", 
    2: "2. deposit", 
    3: "3. withdraw", 
    4: "4. exit"
}

while True:
    try:
        # Print the available transactions
        for key in list_of_transactions.keys():
            print(list_of_transactions[key])
        
        # Get the user input for transaction selection
        customer_input = int(input("Please enter the transaction key: "))
            # Dynamically calling the method based on the user input
        if customer_input == 1:
                transaction.show_balance()
        elif customer_input == 2:
                transaction.deposit()
        elif customer_input == 3:
                transaction.withdraw()
        elif customer_input == 4:
            print("Exit")
            break  # Exit the loop if the user selects 4
    except ValueError:
        print("Please enter a valid key")

#testing pull command
#pull command worked