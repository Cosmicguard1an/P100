class Atm:
    def __init__(self,cardNum, pinNum):
        self.cardNum = cardNum
        self.pinNum = pinNum
    def CashWithdrawal(self, cardNum, pinNum):
        print("Cash has been withdrawn!")
    def BalanceEnquiry(self, cardNum, pinNum):
        print("You have some money in your account!")
obj = Atm(192,192)
obj.CashWithdrawal(192,192)
obj.BalanceEnquiry(192,192)
