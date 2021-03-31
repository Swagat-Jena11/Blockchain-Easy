# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:28:18 2021

@author: Gigabyte-pc
"""
import hashlib


class Block:
    
    def __init__(self):
        self.__own_hash = 0
        self.__prev_hash = 0
        self._transactions = ''
        
    def set_prev(self, prev_hash):
        self.prev_hash = prev_hash
        
    def hashing(self, x):
        h = []
        for i in x:
            st = i.sender + i.receiver + str(i.amount) + str(i.fees)
            h.append(hashlib.sha256(st.encode()).hexdigest())
        return h
    
    def merkle_root(self, x):
        if(len(x)%2!=0):
            x.append('')

        # Merkle Root
        while(len(x)!=1):
            for i in range(0, len(x)//2):
                x[i] = hashlib.sha256((x[i].join(x[i+1])).encode()).hexdigest()
                x.pop(i+1)
        return x[0]
    
    def set_transactions(self, transactions):
        self._transactions = transactions
        x = self.hashing(self._transactions)
        self.__m = self.merkle_root(x)
        return self.__m
        
    def mine(self, nonce):
        return hashlib.sha256((self.__m.join(str(nonce))).encode()).hexdigest()
    
    def set_final(self, c, nonce, own_hash):
        self.difficulty = c
        self.__nonce = nonce
        self.__own_hash = own_hash
    
    
    def get_hash(self):
        return self.__own_hash
    
    def get_m(self):
        return self.__m
    
    def get_prev(self):
        return self.prev_hash
    
    def get_nonce(self):
        return self.__nonce