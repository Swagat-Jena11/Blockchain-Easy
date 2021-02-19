# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:07:15 2021

@author: Gigabyte-pc
"""
import random
import string
from transaction import Transaction


class Wallet:
    
    txns = []
    
    def __init__(self):
        self.public_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 20))
    
    def advertise(self, txn):
        self.txns.append(txn)
    
    def transact(self, receiver, txn, fees):
        self.txn = Transaction(self.public_id, receiver, txn, fees)
        self.advertise(self.txn)
        
        
    def show_transactions(self):
        for i in self.txns:
            print(i.sender, i.receiver, i.txn, i.fees)
        print('Select Transactions to Verify')
        inp_list = []
        while(True):
            x = int(input())
            if(x==-1):
                break;
            else:
                print(x, type(x))
                inp_list.append(x)
        print(inp_list)
        n=[]
        for i in inp_list:
            n.append(self.txns[i-1])
        inp_list.reverse()
        for i in inp_list:
            self.txns.pop(i-1)
        return n
        
        