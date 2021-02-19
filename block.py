# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 19:14:05 2021

@author: Gigabyte-pc
"""

class Block:
    
    own_hash = ''
    prev_hash = ''
    
    # Defining the Block
    def __init__(self, own_hash, transacts):
        
        self.own_hash = own_hash
        self.transacts = transacts
        