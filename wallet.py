import random
import string
from transaction import Transaction
import pickle
import glob
import os

class Wallet:
    
    
    def __init__(self):
        self.public_id = ''.join(random.choices(string.ascii_uppercase+string.digits, k=20))
        self._money = 100
    
    def transact(self, receiver, amount, fees):
        txn = Transaction(self.public_id, receiver, amount, fees)
        st = ''.join(random.choices(string.digits,k=10))
        st = 'TXN'+st
        tmp = pickle.dump(txn, open(st,'wb'))
        pickle.STOP
                
        
    def show_transaction():
        txns = glob.glob('TXN*')
        li = []
        for i in txns:
            tmp = open(i,'rb')
            li.append(pickle.load(tmp))
            tmp.close()
            pickle.STOP
        for i in li:
            print(i.sender, i.receiver, i.amount, i.fees)
        n = list(map(int, input('Choose Transactions to Verify:').split(' ')))
        n.sort(reverse=1)
        n = [x-1 for x in n]
        li2=[]
        for i in n:
            os.remove(txns[i])
            li2.append(li[i])
        return li2
    
    def add_money(self,n):
        self._money+=n
      