class ATM:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = 1000

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Funds. Please try lower amount")
        elif amount<= 0:
            print("Enter value amount to withdraw.")
        else:
            self.balance-=amount
            print("Cash Withdrawal Successful")

    def balanceInquiry(self):
        print("Your current balance is $" + str(self.balance))
        

user_atm = ATM("1234567890","1234")
user_atm.withdraw(500)
user_atm.balanceInquiry()