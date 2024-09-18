from bank_account import bank


class savings_account(bank):
    def __init__(
        self, name, balance, minimum_balance, routing_number, account_number, interest
    ):
        super().__init__(name, balance, minimum_balance, routing_number)
        self.__account_number = account_number
        self.interest = interest

    def interest_acc(self):
        self.interest = self.current_balance * 0.05
        return self.interest
