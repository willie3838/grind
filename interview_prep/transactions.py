import math
class Transactions:
    def __init__(self):
        self.people = {
            "A":100
        }

    def outputTransactions(self, transactions):
        for payer, payee, percentage in transactions:
            # print(payer, payee, percentage)
            amount = self.people[payer] * percentage
            self.people[payer] = round(self.people.get(payer, 0) * (1-percentage), 2)
            self.people[payee] = round(self.people.get(payee, 0) + amount, 2)
            # print(self.people, "\n")
        
        return self.people
    
    def removeNthTransaction(self, transactions, person, n):
        for i, (payer, payee, percentage) in enumerate(transactions):
            if payer == person or payee == person:
                n -= 1
            if n == 0:
                return self.outputTransactions(transactions[:i] + transactions[i+1:])
            
        

    
    def findPersonsBalance(self, person):
        return self.people[person]
    




transactions = [
    ("A","B",0.2),
    ("A","C",0.4),
    ("B","D",0.3),
    ("C","D",0.5),
    ("C","F",0.2),
    ("B","E",0.5),
    ("D","E",0.25),
    ("F","G",0.1),
    ("E","C",0.5)
]


t = Transactions()
# t.outputTransactions(transactions)
print(t.removeNthTransaction(transactions, "B", 2))


