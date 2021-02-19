# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:02:55 2021

@author: Gigabyte-pc
"""

class Chain:

    def __init__(self):
        self.chn = []
        
    def add_block(self, bl):
        if len(self.chn)==0:
            bl.prev_hash = '0'
        else:
            bl.prev_hash = self.chn[-1].own_hash
        self.chn.append(bl)