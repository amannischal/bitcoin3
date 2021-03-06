from web3 import Web3
from hexbytes import HexBytes

IP_ADDR = '18.188.235.196'
PORT = '8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))


# if w3.isConnected():
#   This line will mess with our autograders, but might be useful when debugging
#     print( "Connected to Ethereum node" )
# else:
#    print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    tx = w3.eth.get_transaction(tx)
    return tx


# Return the gas price used by a particular transaction,
#   tx is the transaction
def get_gas_price(tx):
    tx = w3.eth.get_transaction(tx)
    gas_price = tx['gasPrice']
    return gas_price


def get_gas(tx):
    tx = w3.eth.get_transaction_receipt(tx)
    gas = tx['gasUsed']  # YOUR CODE HERE
    return gas


def get_transaction_cost(tx):
    tx_cost = get_gas(tx) * get_gas_price(tx)  # YOUR CODE HERE
    return tx_cost


def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    txs = block['transactions']
    block_cost = 0
    for tx in txs:
        block_cost += get_transaction_cost(tx)
        # YOUR CODE HERE
    return block_cost


# Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    # max_tx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    block = w3.eth.get_block(block_num)
    txs = block['transactions']
    max = 0
    max_tx = 0
    for tx in txs:
        if get_transaction_cost(tx) > max:
            max = get_transaction_cost(tx)
            max_tx = tx
    max_tx = HexBytes(max_tx)  # YOUR CODE HERE
    return max_tx
