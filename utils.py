import json
from web3 import Web3, HTTPProvider
import pandas as pd
import json
from hexbytes import HexBytes

ALLOWED_EXTENSIONS = {'xls', 'xlsx'}


def tx_to_json(tx):
    result = {}
    for key, val in tx.items():
        result[key] = val

    return result


class Utils:
    blockchain_address = 'http://18.219.214.162:5000'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'build/contracts/LandRegistery.json'
    deployed_contract_address = '0xf9eCa6E22156cb3fc17922A435653BFE1e0283AE'
    user_contract_address = '0x1d2F0B41E3A89d1E12Ea9eB8b6eFD1b61cA1c521'
    compiled_user_contract = 'build/contracts/UserData.json'
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)
        contract_abi = contract_json['abi']
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
    with open(compiled_user_contract) as file:
        user_contract_json = json.load(file)
        user_contract_abi = user_contract_json['abi']
    user_contract = web3.eth.contract(address=user_contract_address, abi=user_contract_abi)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class HexJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, HexBytes):
            return obj.hex()
        return super().default(obj)


def read_excel(excel_file):
    excel_records = pd.read_excel(excel_file)
    excel_records_df = excel_records.loc[:, ~excel_records.columns.str.contains('^Unnamed')]
    data = excel_records_df.to_dict(orient='record')
    return data


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if not isinstance(o, str):
            return str(o)
        return json.JSONEncoder.default(self, o)
