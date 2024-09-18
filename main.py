from bank_account import bank
from checking_account import checking_account
from savings_account import savings_account


class main:
    s1 = savings_account("Connor", 10000, 10, 1, 1234, 0)
    c1 = checking_account("Schwab", 500, 100, 2, 4321, 1500)

    while True:
        new_balance = int(input("Please input the balance of your checking account"))
        c1.current_balance = new_balance
        c1.withdraw()
        c1.print_customer_information()

        s1.interest_acc()
