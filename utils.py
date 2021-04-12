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
    user_contract_address = '0xf19A2A01B70519f67ADb309a994Ec8c69A967E8b'
    compiled_user_contract = 'build/contracts/UserData.json'
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)
        contract_abi = contract_json['abi']
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    with open(compiled_user_contract) as file:
        user_contract_json = json.load(file)
        user_contract_abi = user_contract_json['abi']
    user_contract = web3.eth.contract(address=user_contract_address, abi=user_contract_abi)

from hexbytes import HexBytes

class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)
