import math

class Category:

  def __init__(self, category):
    self.category = category
    self.balance = 0
    self.ledger = []

  def __str__(self):
    output = self.category.center(30, "*")
    for i in self.ledger:
      amount = i["amount"]
      description = i["description"][0:23]
      desc = len(description)
      output += f"\n{description:23} {amount:.2f}"
    output += f"\nTotal: {self.balance:.2f}"
    return output

  def deposit(self, money, description=""):
    self.balance += money
    self.ledger.append({"amount": money, "description": description})

  def withdraw(self, money, description=""):
    self.balance -= money
    if self.balance < 0:
      return False
    else:
      self.ledger.append({"amount": money * -1, "description": description})
      return True

  def get_balance(self):
    return self.balance
  
  def transfer(self, money, abc): # abc = another budget category
    if self.withdraw(money, f"Transfer to {abc.category}"):
      abc.deposit(money, f"Transfer from {self.category}")
      return True
    else:
      return False

  def check_funds(self, money):
    if self.balance >= money: 
      return True
    else:
      return False







def create_spend_chart(categories):
  totalspent = 0     # total amount spent by all categories to count percentage
  spent_by_category = {} # spent by each category. format: {"category name": amount}
  per_spent_by_category = {} # percentage spent by each category
  categories_len = [] # length of the character of a category name to print it correctly on the chart
  chart = "Percentage spent by category\n" # chart of the percentage spent by each category 


  # retrieve total spent  and spent_by_category form the categories
  for category in categories:
    name = category.category
    # categories_len.append(len(name))
    for ledge in category.ledger:
      if ledge["amount"] < 0:
        if name in spent_by_category:
          spent_by_category[name] += ledge["amount"] * -1
        else:
          spent_by_category[name] = ledge["amount"] * -1
        totalspent += ledge["amount"] * -1
  
  # calculate the percentage spent by each category
  for i in spent_by_category:
    per_spent_by_category[i] = math.floor(spent_by_category[i] / (totalspent*10) * 100) * 10

  # print all of them for debugging and see what's going on
  print(per_spent_by_category)
  print(spent_by_category)
  print(totalspent)

  # show the chart data
  for i in range(100, -10, -10):
    print(f"{i:3}|", end="")
    chart += f"{i:3}|"
    for category in per_spent_by_category:
      if per_spent_by_category[category] >= i:
        print(" o ", end="")
        chart += " o "
      else:
        print("   ", end="")
        chart += "   "
    print()
    chart += " \n"
  print("    " + "-" * (3 * len(per_spent_by_category) + 1))
  chart += "    " + "-" * (3 * len(per_spent_by_category) + 1) + "\n"
  

  # print(max(iter(categories_len)))
  for category in per_spent_by_category:
    categories_len.append(len(category))

  # labels o the chart
  for i in range(max(iter(categories_len))):
    print("    ", end="")
    chart += "    "
    for cat in per_spent_by_category:
      try:
        print(f" {cat[i]} ", end="")
        chart += f" {cat[i]} "
      except:
        print("   ",end="")
        chart += "   "
    print()
    if not i == max(iter(categories_len)) -1:
      chart += " \n"
    else:
      chart += " "
  return chart

