class savings_account(bank):
    def __init__(self, bank, account_number, interest):
        super().__init__(bank)
        self.account_number = account_number
        self.interest = interest
