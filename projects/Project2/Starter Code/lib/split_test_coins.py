from bitcoin import SelectParams
from bitcoin.core import CMutableTransaction, x
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from config import (my_private_key, my_public_key, my_address,
    alice_secret_key_BTC, alice_public_key_BTC, alice_address_BTC, 
    bob_secret_key_BTC, bob_public_key_BTC, bob_address_BTC,
    alice_secret_key_BCY, alice_public_key_BCY, alice_address_BCY, 
    bob_secret_key_BCY, bob_public_key_BCY, bob_address_BCY,
    faucet_address, network_type)

from utils import create_txin, create_txout, broadcast_transaction



def split_coins(amount_to_send, txid_to_spend, utxo_index, n, network):
    txin_scriptPubKey = address.to_scriptPubKey()
    txin = create_txin(txid_to_spend, utxo_index)
    txout_scriptPubKey = address.to_scriptPubKey()
    txout = create_txout(amount_to_send / n, txout_scriptPubKey)
    tx = CMutableTransaction([txin], [txout]*n)
    sighash = SignatureHash(txin_scriptPubKey, tx,
                            0, SIGHASH_ALL)
    txin.scriptSig = CScript([private_key.sign(sighash) + bytes([SIGHASH_ALL]),
                              public_key])
    VerifyScript(txin.scriptSig, txin_scriptPubKey,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    response = broadcast_transaction(tx, network)
    print(response.status_code, response.reason)
    print(response.text)

if __name__ == '__main__':
    SelectParams('testnet')

    ######################################################################
    # TODO: set these parameters correctly
    ## 1. 在此处把config文件的myself, alice, bob的privatekey对象拷贝过来
    private_key = CBitcoinSecret(
    'cUae5GMgjstodGCA8RowUxZkoPb8PhhHFvSZc3cftnM1mT83LvqR')

    public_key = private_key.pub
    address = P2PKHBitcoinAddress.from_pubkey(public_key)

    ## 2. 根据发送测试代币的交易输出的金额，设置amount_to_send
    amount_to_send = 0.00013372 # amount of BTC in the output you're splitting minus fee
    ## 3. 根据水龙头的交易id，设置txid_to_spend·
    txid_to_spend = (
        'd1ea0d700767c81e6ba7c4fa25e83b5122f1ae34a905d882c108754489b939b2')
    ## 4. 一般都是1
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ## 5. 根据需要分割的份数，设置n，保险起见，n可以设置大一点
    n = 8 # number of outputs to split the input into
    # For n, choose a number larger than what you immediately need, 
    # in case you make mistakes.
    ######################################################################

    split_coins(amount_to_send, txid_to_spend, utxo_index, n, network_type)
