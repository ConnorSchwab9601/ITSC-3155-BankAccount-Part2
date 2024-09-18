class checking_account(bank):
    def __init__(self, bank, account_number, transfer_max):
        super().__init__(bank)
        self.__account_number = account_number
        self.__transfer_max = transfer_max

    def tranfer(self, transfer):
        if(transfer <= self.__transfer_max):
            return  True
        else:
            return False