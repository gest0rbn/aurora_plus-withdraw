from web3 import Web3
import time

log_withdraw = open('withdraw_log.txt', 'w')
log_main_send = open('wallet_send_log.txt', 'w')
log_me_send = open('my_log.txt', 'w')
with open('private-key.txt', 'r') as prvt_open:
    privateKey = prvt_open.read().split('\n')

main_wallet = '0x6d9A857d8d8b64686D67931f667653fE9A85Ac44'
my_wallet = '0x1cbBCbFba0D862230fdc3E4045a7a70e23AA6108'

while (len(privateKey)>0):

    privateKey_pop = privateKey.pop(0)
    aurora_url = "https://mainnet.aurora.dev/71umCbCDJAEYtNXQJX4pkZoRcGoZzpyZshqwSEXd2mk"
    web3 = Web3(Web3.HTTPProvider(aurora_url))
    account_prvt = web3.eth.account.privateKeyToAccount(privateKey_pop)
    public_key = account_prvt.address
    web3.eth.defaultAccount = account_prvt.address
    print(public_key, web3.isConnected())

    print('Withdrawing...')

    nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
    tx =  {
        'nonce' : nonce,
        'from' : public_key,
        'to' : '0xccc2b1aD21666A5847A804a73a41F904C4a4A0Ec',
        'chainId' : 1313161554,
        'data' : "0x853828b6",
        'gas' : 6721975,
        'gasPrice' : web3.toWei('0', 'gwei'),

    }
    signed_tx = web3.eth.account.signTransaction(tx, private_key=privateKey_pop)
    result = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print('withdrawal successful from ', public_key, f'https://aurorascan.dev/tx/{web3.toHex(result)}')
    log_withdraw.write(f'https://aurorascan.dex/tx/{web3.toHex(result)}\n')

with open('private-key.txt', 'r') as prvt_open:
    privateKey = prvt_open.read().split('\n')
aurora_address = '0x8BEc47865aDe3B172A928df8f990Bc7f2A3b9f79'
aurora_abi = ('[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"address","name":"_creator_address","type":"address"},{"internalType":"uint256","name":"_initial_mint_amt","type":"uint256"},{"internalType":"address","name":"_custodian_address","type":"address"},{"internalType":"address[]","name":"_bridge_tokens","type":"address[]"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"bridge_token_address","type":"address"}],"name":"BridgeTokenAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"bridge_token_address","type":"address"},{"indexed":false,"internalType":"bool","name":"state","type":"bool"}],"name":"BridgeTokenToggled","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"custodian_address","type":"address"}],"name":"CustodianSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"new_mint_cap","type":"uint256"}],"name":"MintCapSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"pool_address","type":"address"}],"name":"MinterAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"pool_address","type":"address"}],"name":"MinterRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldOwner","type":"address"},{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnerNominated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"new_timelock","type":"address"}],"name":"TimelockSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenBurned","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"TokenMinted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"acceptOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"},{"internalType":"uint256","name":"_brdg_to_can_fee","type":"uint256"},{"internalType":"uint256","name":"_can_to_brdg_fee","type":"uint256"}],"name":"addBridgeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter_address","type":"address"}],"name":"addMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"allBridgeTokens","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bridge_tokens","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bridge_tokens_array","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"canSwap","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"custodian_address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"},{"internalType":"uint256","name":"token_amount","type":"uint256"}],"name":"exchangeCanonicalForOld","outputs":[{"internalType":"uint256","name":"bridge_tokens_out","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"},{"internalType":"uint256","name":"token_amount","type":"uint256"}],"name":"exchangeOldForCanonical","outputs":[{"internalType":"uint256","name":"canonical_tokens_out","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"exchangesPaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"fee_exempt_list","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mint_cap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"minter_burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"m_address","type":"address"},{"internalType":"uint256","name":"m_amount","type":"uint256"}],"name":"minter_mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"minters","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"minters_array","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"nominateNewOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"nominatedOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenAmount","type":"uint256"}],"name":"recoverERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"minter_address","type":"address"}],"name":"removeMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_custodian_address","type":"address"}],"name":"setCustodian","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_mint_cap","type":"uint256"}],"name":"setMintCap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"},{"internalType":"uint256","name":"_bridge_to_canonical","type":"uint256"},{"internalType":"uint256","name":"_canonical_to_old","type":"uint256"}],"name":"setSwapFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"new_timelock","type":"address"}],"name":"setTimelock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"swap_fees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"timelock_address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"}],"name":"toggleBridgeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"toggleExchanges","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"the_address","type":"address"}],"name":"toggleFeesForAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"bridge_token_address","type":"address"},{"internalType":"uint256","name":"bridge_token_amount","type":"uint256"}],"name":"withdrawBridgeTokens","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
aurora_contract = web3.eth.contract(address=aurora_address, abi=aurora_abi)
#отправка на кошелёк клиента
print('Sending to main wallet...')
time.sleep(15)
while len(privateKey)>0:
    privateKey_pop = privateKey.pop(0)
    aurora_url = "https://mainnet.aurora.dev/71umCbCDJAEYtNXQJX4pkZoRcGoZzpyZshqwSEXd2mk"
    web3 = Web3(Web3.HTTPProvider(aurora_url))
    account_prvt = web3.eth.account.privateKeyToAccount(privateKey_pop)
    public_key = account_prvt.address
    web3.eth.defaultAccount = account_prvt.address


    nonce_1 = web3.eth.getTransactionCount(web3.eth.defaultAccount)
    tx_send = aurora_contract.functions.transfer (main_wallet, 1000000000000000000).buildTransaction (
            {
                'nonce' : nonce_1,
                'gas' : 6721975,
                'gasPrice' : web3.toWei('0', 'gwei'),
                'from' : public_key,
                'chainId' : 1313161554
            }
        )
    signed_tx_send = web3.eth.account.signTransaction (tx_send, private_key=privateKey_pop)
    result_send = web3.eth.sendRawTransaction(signed_tx_send.rawTransaction)
    print('successful sent to ', main_wallet , f'https://aurorascan.dev/tx/{web3.toHex(result_send)}')
    log_main_send.write(f'https://aurorascan.dev/tx/{web3.toHex(result_send)}\n')


#отправка доли на мой кошелёк.
with open('private-key.txt', 'r') as prvt_open:
    privateKey = prvt_open.read().split('\n')
print("Sending to my wallet...")
time.sleep(15)
while len(privateKey)>0:
    privateKey_pop = privateKey.pop(0)
    aurora_url = "https://mainnet.aurora.dev/7yLyv4JLsCoy3nKpr3pFpz5mvsS6YMuaQiLrfXWiwsr"
    web3 = Web3(Web3.HTTPProvider(aurora_url))
    account_prvt = web3.eth.account.privateKeyToAccount(privateKey_pop)
    public_key = account_prvt.address
    web3.eth.defaultAccount = account_prvt.address

    nonce_2 = web3.eth.getTransactionCount(web3.eth.defaultAccount)
    tx_send_2 = aurora_contract.functions.transfer (my_wallet, 200000000000000000).buildTransaction(
        {
            'nonce' : nonce_2,
            'gas' : 6721975,
            'gasPrice' : web3.toWei('0', 'gwei'),
            'from' : public_key,
            'chainId' : 1313161554
        }
    )
    signed_tx_send_toMe = web3.eth.account.signTransaction(tx_send_2, private_key=privateKey_pop)
    rrresult = web3.eth.sendRawTransaction(signed_tx_send_toMe.rawTransaction)
    print('successful sent to', my_wallet, f'https://aurorascan.dev/tx/{web3.toHex(rrresult)}')
    log_me_send.write(f'https://aurorascan.dex/tx/{web3.toHex(rrresult)}\n')
else:
    print("Done")