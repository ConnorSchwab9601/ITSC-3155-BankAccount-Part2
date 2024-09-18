from bank_account import bank


class checking_account(bank):
    def __init__(
        self,
        name,
        balance,
        minimum_balance,
        routing_number,
        account_number,
        transfer_max,
    ):
        super().__init__(name, balance, minimum_balance, routing_number)
        self.__account_number = account_number
        self.__transfer_max = transfer_max

    def tranfer(self, transfer):
        if transfer <= self.__transfer_max:
            return True
        else:
            return False
