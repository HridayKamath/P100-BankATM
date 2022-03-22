class ATM (object):
    def __init__ (self, cardNumber, pinNumber):
        self.cardNumber =cardNumber
        self.pinNumber = pinNumber
        

    def cashWithdrawal(self):
        print("Cash Withdrawn")

    def balanceEnquiry(self):
        print("Balance amount sent to phone")

abc = ATM("12345678", "1234")

print(abc.pinNumber)
print(abc.cardNumber)
print(abc.balanceEnquiry())
print(abc.cashWithdrawal())
