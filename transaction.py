# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:35:15 2021

@author: Gigabyte-pc
"""

class Transaction:
    
    def __init__(self, sender, receiver, txn, fees):
        self.sender = sender
        self.receiver = receiver
        self.txn = txn
        self.fees = fees
