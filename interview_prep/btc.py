import collections

'''
- Input could have been an array but opted for a class to improve readability
- Saved space complexity in comparison to array approach
'''
class Transaction:
    def __init__(self, date, type, price, amount):
        self.date = date
        self.type = type
        self.price = price
        self.amount = amount


class System:
    '''
    Assumptions
    - Cost basis is the total investment / amount of btc we have
    - Acquisition date can include multiple dates
    - Used a queue assuming we'd process transactions in a FIFO manner and to get o(1) access to previous transactions
    
    '''
    def __init__(self):
        self.buys = collections.deque()
        self.costBasis = 0
        self.btcAmount = 0
        self.investment = 0
        self.acquisitionDates = ""
    
    '''
    Changes (after coding the main functionality)
    - Added a check to see if the amount we're trying to sell is > than the amount we have
    - Added a check to see if the amount / price are valid
    - Modified if-else to make sure we only run code when the transaction type is buy or sell

    '''
    def processTransaction(self, transaction):
        if transaction.amount < 0 or transaction.price < 0:
            print("Your amount or price is invalid, please try again")
        else:
            if transaction.type == "buy":
                self.buys.appendleft(transaction)
                self.investment += transaction.price * transaction.amount
                self.btcAmount += transaction.amount
                self.costBasis = self.investment / self.btcAmount
            elif transaction.type == "sell":
                if self.btcAmount < transaction.amount:
                    print("You currently own less BTC than you want to sell, unable to fulfill your transaction")
                else:
                    gain = self.sellTransaction(transaction)
                    self.investment -= transaction.price * transaction.amount
                    self.btcAmount -= transaction.amount
                    self.outputData(transaction, gain)
        


    def sellTransaction(self, transaction):
            n = transaction.amount
            self.acquisitionDates = []
            gains = (transaction.price - self.costBasis) * n

            while n > 0:
                self.acquisitionDates.append(str(self.buys[-1].date))
                if n >= self.buys[-1].amount:
                    n -= self.buys[-1].amount
                    self.buys.pop()
                else:
                    self.buys[-1].amount -= n
                    n = 0     
            self.acquisitionDates = ",".join(self.acquisitionDates)
            return gains

    def outputData(self, transaction, gains):
        print("Date of sale: ", transaction.date)
        print("Date(s) of acquisition: ", self.acquisitionDates)
        print("Cost basis: ", self.costBasis)
        print("Proceeds: ", transaction.price * transaction.amount)
        print("Gains/Loss: ", gains)
        print("BTC Amount: ", self.btcAmount)
        print("\n")
    
    def currentPosition(self, transaction):
        print("Date: ", transaction.date)
        print("BTC Amount: ", self.btcAmount)
        print("Cost basis: ", self.costBasis)
        print("\n")

    


def main():
    system = System()


    # case when there's invalid data: we get something diff than buy/sell or numbers are negative...
    # tests = [
    #     Transaction(1, "dwwad", -24, -2)
    # ]

    # case when transactions are empty
    # tests = []

    # case when we don't have enough funds
    # tests = [
    #     Transaction(1, "buy", 200, 1),
    #     Transaction(2, "sell", 100, 4)
    # ]

    # happy case
    # tests = [
    #     Transaction(1, "buy", 25, 5),
    #     Transaction(2, "buy", 40, 10),
    #     Transaction(3, "sell", 42, 7),
    #     Transaction(4, "sell", 3, 1),
    #     Transaction(5, "buy", 25, 5),
    #     Transaction(6, "sell", 20, 10)
    # ]

    for transaction in tests:
        system.processTransaction(transaction)

main()
# import collections
# import math

# '''
# bought $20, 2
# sell   $10, 1

# bought $5, 3
# sell   $10, 1

# '''
# class Transactions:
#     def __init__(self):
#         pass

#     def processTransactions(self, transactions):
#         # stores all the btc bought
#         btc = collections.deque()
#         for date, type, price, amount in transactions:
#             if type == "buy":
#                 btc.appendleft([price, amount, date])
#             else:
#                 n = amount
#                 while n > 0:
#                     buyPrice, buyAmount, buyDate = btc[-1][0], btc[-1][1], btc[-1][2]
                    
#                     if buyAmount < n:
#                         gains = price*amount - buyPrice*buyAmount
#                         amount -= buyAmount
#                         btc.pop()
#                         n -= buyAmount
#                     else:
#                         gains = price*amount - buyPrice*amount
#                         btc[-1][1] -= amount
#                         n = 0
#                     print(date, buyDate, price, gains, amount)

# t = Transactions()

# transactions = [
#     [-1,"buy",100,1],
#     [-1,"buy",5,1],
#     [-1,"sell",10,2]
# ]

# print(t.processTransactions(transactions))



