class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
  
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}"+f"{item['amount']:>7.2f}" + '\n'
      total += item["amount"]
    output = title + items + "Total: " + str(total)
    return output
      

  def deposit(self, amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
  
  def withdraw(self, amount, description=""):
    if (self.check_funds(amount)):
      self.ledger.append({"amount":-amount,"description":description})
      return True;
    return False

  def get_balance(self):
    total_sum = 0
    for item in self.ledger:
      total_sum += item["amount"]
    return total_sum
  
  def transfer(self,amount,category):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from "+self.name)
      return True
    return False
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    return True

  def get_withdrawls(self):
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total


def flip(n):
  multiplier = 10
  return int(n*multiplier) / multiplier

def getTotals(categories):
  total = 0
  breakdown = []
  for category in categories:
    total += category.get_withdrawls()
    breakdown.append(category.get_withdrawls())
  rounded = list(map(lambda x: flip(x/total), breakdown))
  return rounded

def create_spend_chart(categories):
  titl = "Percentage spent by category\n"
  i = 100
  totals = getTotals(categories)
  while i >= 0:
    spaces = " "
    for total in totals:
      if total * 100 >= i:
        spaces += "o  "
      else:
        spaces += "   "
    titl += str(i).rjust(3) + "|" + spaces + "\n"
    i -= 10
  
  dashes = "-" + "---"*len(categories)
  names = []
  x_names = ""
  for category in categories:
    names.append(category.name)
  
  maxi = max(names, key=len)

  for x in range(len(maxi)):
    nam = '     '
    for name in names:
      if x >= len(name):
        nam += "   "
      else:
        nam += name[x] + "  "
    if (x != len(maxi) - 1):
      nam += '\n'
    
    x_names += nam
      

  titl += dashes.rjust(len(dashes)+4) + "\n" + x_names
  return titl
