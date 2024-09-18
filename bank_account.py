class bank:
    bankTitle = "Not America Bank"

    def __init__(self, name, balance, minimum_balance, routing_number):
        self.customer_name = name
        self.current_balance = balance
        self.minimum_balance = minimum_balance
        self._routing_number = routing_number

    def print_customer_information(self):
        print("Printing customer information below for ", bank.bankTitle)
        print("Name-", self.customer_name)
        print("Current Balance-", self.current_balance)
        print("Minimum Balance-", self.minimum_balance)

    def deposit(self):
        inp = int(input("Enter the amount of money you would like to deposit: "))
        self.current_balance += inp
        print(self.current_balance, " is the new current balance after deposit")

    def withdraw(self):
        inp = int(input("Enter the amount of money you would like to withdraw: "))
        temp = self.current_balance - inp
        if self.minimum_balance >= temp:
            print(
                "unable to withdraw because withdraw would put you under minimum balance"
            )
        else:
            self.current_balance -= inp
            print(self.current_balance, " is the new current balance after withdraw")

