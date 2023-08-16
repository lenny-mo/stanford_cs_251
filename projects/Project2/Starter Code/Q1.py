from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    
    ## get pubkey hash from address
    pubkey_hash = P2PKHBitcoinAddress.to_scriptPubKey(address)
    return pubkey_hash
    # return [
    #     # fill this in!
    #     OP_DUP,
    #     OP_HASH160,
    #     pubkey_hash,
    #     OP_EQUALVERIFY,
    #     OP_CHECKSIG
    # ]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        # fill this in!
        signature,
        public_key
    ]
    ######################################################################

def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    ## 使用压缩的公钥，长度33bytes
    public_key_bytes = bytes(sender_public_key)
    print("Public key length:", len(public_key_bytes))

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    ## BUG: EvalScript: OP_EQUALVERIFY failed
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                    txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.000011 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'f45b7e08854c6760890e795e3e4d73aaf483dc1efb3985b0ca486dc584440e79')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
