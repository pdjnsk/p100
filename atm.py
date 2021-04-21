class Atm(object):

  def __init__(self,cashWithdrawl, BalanceEnquiry, withdrawalLimit):
    self.cashWithdrawl = cashWithdrawl
    self.BalanceEnquiry = BalanceEnquiry
    self.withdrawalLimit = withdrawalLimit

  def Withdrawl(self):
    print("1000")

  def Balance(self):
    print("10000")

  def Limit(self):
    print("5000")


atm1 = Atm("1000", "10000", "5000")

print(atm1.Withdrawl(), atm1.Balance(), atm1.Limit())