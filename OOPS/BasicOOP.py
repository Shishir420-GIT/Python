# Class is a blue print of a real life entitiy
# Object is the instance of a class

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def walks(self):
        print(f"{self.name} the {self.species} is walking")

class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount
        print(f"Money Deposited ${amount}, New balance is {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance is {self.balance}")
    
    def getBalance(self):
        print(f"Current Balance is {self.balance}")

if __name__ == "__main__":
    # Example 1
    dog = Animal("Buddy", 3, "Dog")
    dog.walks()  # Output: Buddy the Dog is walking
    
    # Example 2
    account = BankAccount("John Doe", "123456789", 1000)
    account.getBalance()  # Output: Current Balance is 1000
    account.deposit(500)  # Output: Money Deposited $500, New balance is
    account.getBalance()  # Output: Current Balance is 1500
    account.withdraw(200)  # Output: Withdrew $200. Remaining balance is
    account.getBalance()  # Output: Current Balance is 1300
