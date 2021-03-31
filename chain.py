# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:02:55 2021

@author: Gigabyte-pc
"""
import pickle
import glob
class Chain:

    def __init__(self):
        chn = glob.glob('Blocks\Block*')
        print('Chain:', chn)
        self.chn = []
        if(chn==''):
            return
        for i in chn:
            tmp = open(i,'rb')
            self.chn.append(pickle.load(tmp))
            tmp.close()
            pickle.STOP
        
        
    def add_block(self, bl):
        if len(self.chn)==0:
            print('Creating Genesis Block')
            bl.prev_hash = '0'
            n = 1
        else:
            bl.prev_hash = self.chn[-1].get_hash()
            tmp = glob.glob('Blocks\Block*')[-1]
            n = int(tmp[-1])+1
        
        self.chn.append(bl)
        st = 'Blocks\Block' + str(n)
        f = open(st, 'wb')
        pickle.dump(bl,f)