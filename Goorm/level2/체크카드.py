class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.reservation_queue = []
    
    def deposit(self, amount):
        self.balance += amount
    
    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
    
    def reservation(self, amount):
        if self.balance >= amount and len(self.reservation_queue) == 0:
            self.balance -= amount
        else:
            self.reservation_queue.append(amount)
    
    def process_reservations(self):
        while len(self.reservation_queue) > 0:
            if self.balance >= self.reservation_queue[0]:
                self.balance -= self.reservation_queue.pop(0)
            else:
                break

def parse_transactions(account, transactions):
    for transaction in transactions:
        operation, amount = transaction
        if operation == "deposit":
            account.deposit(amount)
        elif operation == "pay":
            account.pay(amount)
        elif operation == "reservation":
            account.reservation(amount)
        account.process_reservations()
    
    print(account.balance)


init_balance, transaction_count = map(int, input().split())
account = BankAccount(init_balance)
transactions = []

for _ in range(transaction_count):
    operation, amount = map(str, input().split())
    transactions.append((operation, int(amount)))

parse_transactions(account, transactions)
