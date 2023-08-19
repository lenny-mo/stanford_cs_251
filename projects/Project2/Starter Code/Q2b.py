from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import P2PKH_scriptPubKey
from Q2a import Q2a_txout_scriptPubKey
from Q2a import int_to_little_endian_bytes

######################################################################
# TODO: set these parameters correctly
amount_to_send = 0.00001436 # amount of BTC in the output you're sending minus fee
## 使用在Q2a中创建的交易id
txid_to_spend = (
        '83ca122017b9a0a38ce7dac8ee202c4a2e077fe932fec673034eea81ef7b9366')
utxo_index = 0 # index of the output you are spending, indices start at 0
######################################################################

txin_scriptPubKey = Q2a_txout_scriptPubKey
######################################################################
# TODO: implement the scriptSig for redeeming the transaction created
# in  Exercise 2a.

txin_scriptSig = [
        # fill this in!
        1,
        150,
        50,
        150,
        50      
]       
######################################################################
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)


response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
