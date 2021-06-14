# Importing pandas module [pd alias]
import pandas as pd

# Importing mempool.csv file into a Dataframe using pandas
df  = pd.read_csv("mempool.csv")
print(df.head())

# number of rows and columns
print(df.shape)

#check the data types 
print(df.dtypes)

#concise summary of ur DataFrame
print(df.info)

#The describe() method is used for computing some statistical calculations 
print(df.describe())

# This function takes 3 parameters - dataframe and two features as parameters 
# Sorting the Dataframe using sort_values for multiple columns i.e. Fee & Weight & maximise the fee & minimise the weight

def sort_trans(df, maxfee, minwght):
    df = df.sort_values([maxfee, minwght], ascending=[False, True]).reset_index(drop=True)
    return df


def check_weight(x):
    if min_weight + x['weight'] <= highest_weight:
        return True
    else:
        return False


def check_list(x):
    if str(x) in final_set_of_txids:
        return True
    else:
        return False

def check_parent(x):
    if str(x[3]) != "nan":
        parent_list = str(x[3]).split(";")
        for i in parent_list:
            if(check_list(i)):
                continue
            else:
                txnindex = df[df['tx_id'] == i].index.item()
                k = df.loc[txnindex]
                check_add_txn(k)


def add_to_block(x):
    global min_weight
    txnID = x[0]
    weight = x[2]
    min_weight += weight
    final_set_of_txids.append(txnID)

def check_add_txn(x):
    if(check_weight(x)):
        if(not check_list(x)):
            check_parent(x)
            if(check_weight(x)):
                add_to_block(x)


def Main(df):
    sorted_transactions = sort_trans(df, "fee", "weight")
    for i in range(len(sorted_transactions)):
        txnVar =  sorted_transactions.loc[i]
        check_add_txn(txnVar)


def write_to_file(fin_list):
    file = open("block.txt","a")
    for i in fin_list:
        file.write(str(i) + '\n')
    file.close()


highest_weight = 4000000
min_weight = 0
final_set_of_txids = []

data = df
Main(data)

write_to_file(final_set_of_txids)










