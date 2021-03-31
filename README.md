# Blockchain-Easy
A set of programs to learn and teach Blockchain. Almost every keyword in Blockchain has been given a class or function here.

Use working.py to run the program. All other methods, classes are called from user.py.

Classes and Their Description:
block.py ---> Class for Block. Each new block will be an object of this Class.
chain.py ---> Class for the Blockchain. One instance of this class will be called and all Blocks will be added to the instance of this class.
transaction.py ---> Class for Transactions. Defines all data a transaction must contain. All transactions will be an instance of this class.
wallet.py ---> Class for Wallets. The wallet contains a public key for each user. The wallet also keeps unverified transactions. To create a new user, create an instance of this class.
miner.py ---> Class for Miner. All operations performed by miners are defined as functions of this class.
