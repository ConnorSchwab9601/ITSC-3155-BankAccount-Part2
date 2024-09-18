from bank_account import bank
from checking_account import checking_account
from savings_account import savings_account


class main:
    s1 = savings_account("Connor", 10000, 10, 1, 1234, 0)
    c1 = checking_account("Schwab", 500, 100, 2, 4321, 1500)
    s2 = savings_account("Jason", 1000, 10, 3, 1, 0)
    c2 = checking_account("what", 5000, 400, 4, 2, 1000)

    print("Reading information from the first saving account. ")
    s1.print_customer_information()
    print("Routing number: " + str(s1._routing_number))
    print("accumlating a 5% interest for routing number " + str(s1._routing_number))
    print("Account number " + str(s1._routing_number) + "now has $" + str(s1.interest_acc()) + " in interest")

    print("Reading information from the first checking account. ")
    c1.print_customer_information()
    print("Routing number: " + str(c1._routing_number))
    transfer = int(input("How much would you like to transfer from checking account"))
    if(c1.tranfer(transfer)):
        c1.current_balance -= transfer
        print("Transfer went through account balance has been updated")
    else:
        print("The amount you entered is above the transfer limit for the account please try again later")


