class checking_account(bank):
    def __init__(self, bank, account_number, transfer_max):
        super().__init__(bank)
        self._account_number = account_number
        self.__transfer_max = transfer_max

