class yourBank(object):
  '''A demonstration of a class'''

  # an attribute to keep track of total number of accounts
  numb_accounts=0

  def __init__(self,name,balance):
    '''Class initialiser'''
    print("Creating a class")
    self.name=name
    self.balance=balance
    yourBank.numb_accounts+=1

  # methods
  def deposit(self,amt):
    '''Adds an amount of money'''
    self.balance=self.balance+amt

  def withdraw(self,amt):
    '''Removes an amount of money'''
    self.balance=self.balance-amt

  def inquiry(self):
    '''Returns the current balance'''
    return self.balance

class bank2(yourBank):
    def inquiry(self):
      self.balance=self.balance*0.2+ self.balance
      print(self.balance)

if __name__ == '__main__':
  bb=bank2("mm",1000)
  bb.inquiry()
  print(bb.inquiry())
