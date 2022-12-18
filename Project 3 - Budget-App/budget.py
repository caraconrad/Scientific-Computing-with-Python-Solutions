class Category:

    def __init__(self, name):
        self.name = name     
        self.ledger = []   
        self.balance = 0
        self.total_withdrawal = 0


    def __str__(self):
        category_str = self.name.center(30, "*")
        
        for i in self.ledger:
            line = ""
            description = i["description"]
            amount = i["amount"]

            if len(str(amount)) > 7:
                amount = amount[:7]
                print("{:.2f}".format(amount))
            if len(description) > 23:
                description = description[:23]
                print(description)
            
            line += "\n" + description + (30 - (len(description) + len(str("{:.2f}".format(amount))))) * " "  + str("{:.2f}".format(amount))
            category_str += line
        
        category_str += "\nTotal: " + str(self.balance)

        return category_str

    def deposit(self, amount, description = ""):
        self.balance += amount
        self.ledger.append({"amount" : amount, "description" : description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.balance -= amount
            self.total_withdrawal += amount
            self.ledger.append({"amount" : -1 * amount, "description" : description})
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True


def create_spend_chart(categories):
    all_withdrawals = 0
    
    for cat in categories:
        all_withdrawals += cat.total_withdrawal
    
    withdrawal_percent = []
    for cat in categories:
        withdrawal_percent.append(int((((cat.total_withdrawal/all_withdrawals)*100)/10))*10)
        
    bar_chart = "Percentage spent by category\n"

    i = 100
    while i >= 0:
        bar_chart += "{0:>3}".format(str(i)) + "|"
        for percent in withdrawal_percent:
            if percent >= i:
                bar_chart += " o "
            else:
                bar_chart += "   "
        bar_chart += " \n"
        i -= 10
    bar_chart += "    " + ((len(categories) * 3) + 1)  * "-"
    
    name_len_list = []
    for cat in categories:
        name_len_list.append(len(cat.name))

    max_name_len = max(name_len_list)

    i = 0
    while i < max_name_len:
        bar_chart += "\n    "
        for cat in categories:
            if len(cat.name) > i:
                bar_chart += " " + cat.name[i] + " "
            else:
                bar_chart += "   "
        bar_chart += " "
        i += 1        
    
    return bar_chart