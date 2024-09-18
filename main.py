from bank_account import bank
from checking_account import checking_account
from savings_account import savings_account

class main:
    b1 = bank("Connor", 10000, 10)
    b2 = bank("Schwab", 500, 100)
    s1 = savings_account(b1, 1234, 0)
    c1 = checking_account(b1, 4321, 1500)
    while(True)