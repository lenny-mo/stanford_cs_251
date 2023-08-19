from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction

## 把数字转换成小端字节序
def int_to_little_endian_bytes(value, byteorder='little'):
    """
    Convert an integer to its byte representation in little endian format.
    
    Args:
    - value (int): The integer value to be converted.
    - byteorder (str): The byte order format. Default is 'little' for little endian.
    
    Returns:
    - bytes: The byte representation of the integer.
    """
    # Calculate the number of bytes needed to represent the integer
    num_bytes = (value.bit_length() + 7) // 8
    return value.to_bytes(num_bytes, byteorder)

######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        # OP_DUP,fill this in
        # !
        OP_ADD,
        200,
        OP_EQUALVERIFY, 
        OP_SUB,
        100,
        OP_EQUALVERIFY
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    ## 和Q1 一样，使用拆分之后的交易id，但是不同的输出
    amount_to_send = 0.00001436   # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f46a6c9d3951047c1dd21158b5db7505169d7304898f6f6bc2f0071dce1a1221')
    utxo_index = 0 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)

