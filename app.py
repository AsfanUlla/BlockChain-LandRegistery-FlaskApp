import json
from web3 import Web3, HTTPProvider
from ethereum_input_decoder import ContractAbi


blockchain_address = 'http://52.66.236.97:5000'

web3 = Web3(HTTPProvider(blockchain_address))

web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'build/contracts/LandRegistery.json'

deployed_contract_address = '0x9561C133DD8580860B6b7E504bC5Aa500f0f06a7'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']

contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

message = contract.functions.sayHello().call()

tx_hash = contract.functions.setPayload('{name: land}').transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print('tx_hash: {}'.format(tx_hash.hex()))
tx_value = contract.functions.getPayload().call()

latest = web3.eth.blockNumber
blockNumbers = range(latest - 10, latest + 1, 1)

def tx_to_json(tx):
    result = {}
    for key, val in tx.items():
        result[key] = val

    return result

for idx in blockNumbers:
    block = web3.eth.getBlock(idx, full_transactions=True)

    for tx in block.transactions:
        txj = tx_to_json(tx).get('input')
        decoded_input = contract.decode_function_input(txj)
        print(decoded_input)
