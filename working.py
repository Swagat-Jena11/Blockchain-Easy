# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:39:14 2021

@author: Gigabyte-pc
"""


from wallet import Wallet
from miner import Miner
from chain import Chain

# Creating Blockchain
blockchain = Chain()

# Create some Wallet accounts First

user1 = Wallet()
print('Generated User1')
print('Public ID:', user1.public_id)

user2 = Wallet()
print('Generated User2')
print('Receiver Public ID:', user2.public_id)

while(True):
    n = int(input('Enter 1 to Transact, 0 to Exit:'))
    if(n==1):
        # About to Start Transaction
        receiver = user2.public_id
        txn = input('Enter Amount: ')+'DBC'
        fees = input('Enter Fees: ')+'DBC'
        # Initiate a Transaction. Repeat in a loop for multiple Transactions
        user1.transact(receiver, txn, fees)
    else:
        break

# Create Miner Accounts
miner1 = Miner()
miner2 = Miner()
miner3 = Miner()
print('Miners Generated...')

# Show Advertised Transactions to start Verification
print('Verification Start:')
transacts = miner1.show()

# Start Mining
print('Mining...')
h2 = miner1.mine(transacts.copy())


# Start of Consensus Mechanism. If Consensus happens, the block gets added to the Chain.
print('Trying to Achieve Consensus:')
if(miner2.consensus(h2)==1 and miner3.consensus(h2)==1):
    print('Verified.')
    print('Creating Block')
    print('Adding Block to Chain')
    blockchain.add_block(h2)
else:
    print("Can't Verify.")

# Show information in the Blockchain Now
print('Printing Complete Blockchain:')
c=1
for i in blockchain.chn:
    print('Block', c)
    print('Transactions')
    for j in i._transactions:
        print(j.sender, 'to', j.receiver, 'Amount:', j.amount, 'Fees:', j.fees)
    print('Own Hash', i.get_hash())
    print('Previous Hash',i.get_prev())
    print()
    c+=1

