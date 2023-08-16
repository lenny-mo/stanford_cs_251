from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mohjSavDdQYHRYXcS3uS6ttaHP8amyvX78')

# For questions 1-3, we are using 'btc-test3' network. For question 4, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'btc-test3'


######################################################################
# This section is for Questions 1-3
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

my_private_key = CBitcoinSecret(
    'cSQ2ZCQeEF8VAU9LHsamCzBpUEndiDoucpH7QicNndf6kUjfQfGL')

my_public_key = my_private_key.pub
## my_address = mwmWAg4apLHaMFmNhMGt3wi1D7VpvXECdr
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
######################################################################


######################################################################
# NOTE: This section is for Question 4
#
# Create address in Base58 with keygen.py
# Send coins at https://testnet-faucet.mempool.co/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cTjNcq5Z7y4B67XA8UGUtXaMtZpXecQieqsthWtDZo3L84jkq5yt')
## alice_address = mwsK5W82dYyqGNnCHrrt9Hn7ckZwEx751K

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cUae5GMgjstodGCA8RowUxZkoPb8PhhHFvSZc3cftnM1mT83LvqR')
## bob_address = mpXF8roHPh3ioccaZ4LNoHeUcnUu73YhVp

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=YOURTOKEN
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('e1fc8e8f2a287df7d2a6eba7f73ae8f9fb50e83a3b3de7bb13b5da67146b4de5'))
## address = C6DETkWxBbjN9NJtiYxQ4KwRyynCbjNQbr

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('e9e371358e48a3b756f92bacc221affac35e3c554a464f20a5ac4ad1016ce0e1'))
## address = C4rHNUftQgg4KTCbTzxs9AuMipWVPHX6aB

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################
