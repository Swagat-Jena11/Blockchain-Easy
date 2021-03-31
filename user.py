# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 19:25:01 2021

@author: Gigabyte-pc
"""

from wallet import Wallet
from miner import Miner
from block import Block
from chain import Chain

# Creating Blockchain
blockchain = Chain()

# Create some Wallet accounts First
user1 = Wallet()
user2 = Wallet()

print('My Public ID:', user1.public_id)
print('Receiver Public ID:', user2.public_id)

# About to Start Transaction
receiver = user2.public_id
txn = '1.00200000 DBC'
fees = '0.5 DBC'

# Initiate a Transaction. Repeat in a loop for multiple Transactions
user1.transact(receiver, txn, fees)

# Create Miner Accounts
miner1 = Miner()
miner2 = Miner()
miner3 = Miner()

# Show Advertised Transactions to start Verification
transacts = miner1.show()

# Start Mining
h2 = miner1.mine(transacts.copy())


# Start of Consensus Mechanism. If Consensus happens, the block gets added to the Chain.
if(miner2.consensus(h2[0],h2[1],h2[2],h2[3])==1 and miner3.consensus(h2[0],h2[1],h2[2],h2[3])==1):
    print('Verified.')
    print('Creating Block')
    bl = Block(h2[2], transacts)
    print('Adding Block to Chain')
    blockchain.add_block(bl)
else:
    print("Can't Verify.")

# Show information in the Blockchain Now
for i in blockchain.chn:
    print('Transactions')
    for j in i.transacts:
        print(j.sender, 'to', j.receiver, '| Money', j.txn, '| Fees', j.fees)
    print('Own Hash', i.own_hash)
    print('Previous Hash',i.prev_hash)
    print()
    
    
import pickle

f = open('Block1', 'wb')
pickle.dump(bl,f)

f = open('Block1', 'rb')
b = pickle.load(f)
