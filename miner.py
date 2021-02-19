# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:06:08 2021

@author: Gigabyte-pc
"""

from wallet import Wallet
from block import Block
import hashlib
import random


class Miner:
    
    def show(self):
        print('Advertised Transactions:')
        return Wallet.show_transactions(Wallet)


    def hashing(self, x):
        # Hash of Each Transaction
        for i in range(0,len(x)):
            x[i] = hashlib.sha256(x[i].txn.encode()).hexdigest()
        return x
            
            
    def merkle_root(self, x):
        if(len(x)%2!=0):
            x.append('')

        # Merkle Root
        while(len(x)!=1):
            for i in range(0, len(x)//2):
                x[i] = hashlib.sha256((x[i].join(x[i+1])).encode()).hexdigest()
                x.pop(i+1)
        return x
                
                
    def mine(self, x):
        
        n = self.hashing(x)
        m = self.merkle_root(n)
        # Proof Of Work
        h = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        c=1
        while(h[0:4]!='0000'):
            print('Generating Proof of Work')
            nonce = random.randint(-9999999999999999999, 9999999999999999999)
            h = hashlib.sha256((x[0].join(str(nonce))).encode()).hexdigest()
            c+=1
        return m, nonce, h, c
    
    
    def consensus(self, x, nonce, h, c):
        h1 = hashlib.sha256((x[0].join(str(nonce))).encode()).hexdigest()
        if(h1 == h and h1[0:4]=='0000'):
            return 1
        else:
            return 0
    
    
    

    

               

    
    


