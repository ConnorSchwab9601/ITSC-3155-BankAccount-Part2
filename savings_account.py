class savings_account(bank):
    def __init__(self, bank, account_number, interest):
        super().__init__(bank)
        self.__account_number = account_number
        self.interest = interest

    def interest_acculated(self, bank, interest):
        interest = bank.balance * 0.05
        return interest
