class Transaction:
    
    def __init__(self, sender, receiver, amount, fees=0.0):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.fees = fees
