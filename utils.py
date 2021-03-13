import json
from web3 import Web3, HTTPProvider


def tx_to_json(tx):
    result = {}
    for key, val in tx.items():
        result[key] = val

    return result


class Utils:
    blockchain_address = 'http://52.66.236.97:5000'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'build/contracts/LandRegistery.json'
    deployed_contract_address = '0x9561C133DD8580860B6b7E504bC5Aa500f0f06a7'
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)
        contract_abi = contract_json['abi']
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

