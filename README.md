# Code-Challenge-2021-Summer-of-Bitcoin

#### This is the Code challenge for Summer of Bitcoin.  

# Description of files for this repo

####  sb_README.pdf : Problem Statement

####  block_sample.txt : Sample output of Block Transacctions.

####  Solution.ipynb : The Jupyter Notebook containing all the functions & code.

####  main.py : Source Code for the problem

####  mempool.csv : Input Dataset for the mempool.

####  block.txt : output containing Block Transactions.

# Problem Statement :

### To simplify it, let's break down this into 3 simple steps:

### 1. Read a file mempool.csv, with the format:   txid , fee , weight , parent_txids

### 2. We need to output a block of transaction id's which should be less 4000000 (i.e. keep a track of weight)  

### 3. Condition for a block is transactions can be included only if it's parent transactions have been included before !

     
# Approach :
### 1. Read files using pandas module in python & sort the dataframe maximising the fee & minimising the weight.

### 2. Check for parent_txid's
    For Example :

    txid              parent_txids
     abc                   slv
     svt                   nan
     pqr                   slv
   
### So, in order to include "abc" to the output block, we first need to check for "slv" if it has appeared before since it's the "parent_id". 

### 3. Use global variables - highest_weight = 4000000 & min_weight & check whether the total weight of transactions in a block must not exceed 4,000,000 weight.

# Logic :

       read_csv data from mempool.csv   
       sort the dataframe                                                           (#1)
       
       loop through the txids:
         Check if the transaction already exists in the final output list           (#2)
         check if if has parent_txids :
           if included:
             go to that transaction:  
             include it in output block
           if not, add parent to the list(if eligible) before adding the child
           
           check_weight ( i.e. weight <= highest_weight (4000000) )                   (#3)
              if weight < highest_weight :
                  keep including trans_id's in the block
                  write_to_file the trans_id to the bllock.txt file
                                         
                          
                            


