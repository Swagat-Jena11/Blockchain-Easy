# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:16:05 2021

@author: Gigabyte-pc
"""
from wallet import Wallet
from block import Block
import hashlib
import random


class Miner:
    
    def __init__(self):
        self.wallet = Wallet()
    
    def show(self):
        print('Advertised Transactions:')
        return Wallet.show_transaction()
    
    def mine(self, x):
        b = Block()
        b.set_prev(0)
        m = b.set_transactions(x)
        c=1
        print('Generating Proof of Work...')
        print('Please Wait.')
        while(m[0:6]!='000000'):
            nonce = random.randint(-9999999999999999999, 9999999999999999999)
            m = b.mine(nonce)
            c+=1
        print('Difficulty =', c)
        print('Nonce =', nonce)
        print('Hash =', m)
        b.set_final(c, nonce, m)
        return b
    
    def consensus(self, b):
        t1 = b.get_m()
        h1 = hashlib.sha256((t1.join(str(b.get_nonce()))).encode()).hexdigest()
        if(h1 == b.get_hash() and h1[0:4]=='0000'):
            return 1
        else:
            return 0
    
    
    