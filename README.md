# Code-Challenge-2021-Summer-of-Bitcoin

#### This is the Code challenge for Summer of Bitcoin.  

## Description of files of this repo

#####  sb_README.pdf : Problem Statement

#####  block_sample.txt : Sample output of Block Transacctions.

#####  Solution.ipynb : The Jupyter Notebook containing all the functions & code.

#####  main.py : Source Code for the problem

#####  mempool.csv : Input Dataset for the mempool.

#####  Block.txt : output containing Block Transactions.

## Problem Statement :

### 1. Read a file mempool.csv, with the format:   txid , fee , weight , parent_txids

### 2. We need to output a block of transaction id's which should be less than the maximum weight of 4000000 (i.e. keep a track of weight)  

### 3. Condition for a block is transactions can be included only if it's parent transactions have been included before !

     
## Approach :
### 1. Read files using pandas module in python 

### 2. For Example :

    txid              parent_txids
     abc                   slv
     svt                   nan
     pqr                   slv
   
   So, in order to include "abc" to the output block, we first need to check for "slv" if it has appeared before since it's the parent_id
