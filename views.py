from flask import request, jsonify, make_response, render_template
from utils import Utils, HexJsonEncoder
from utils import tx_to_json
from flask.views import MethodView
import json


class GetRecords(MethodView):
    def __init__(self):
        self.web3 = Utils.web3
        self.contract = Utils.contract

    def get(self):
        latest = self.web3.eth.blockNumber
        block_numbers = range(latest - 10, latest + 1, 1)
        response = list()
        for idx in block_numbers:
            block = self.web3.eth.getBlock(idx, full_transactions=True)
            for tx in block.transactions:
                txj = tx_to_json(tx).get('input')
                tx_hash = tx_to_json(tx).get('hash')
                decoded_input = list(self.contract.decode_function_input(txj))
                decoded_input.pop(0)
                decoded_input[0]['hash'] = tx_hash.hex()
                decoded_input[0]['content'] = decoded_input[0]['content'].replace("{", "").replace("}", "")
                decoded_input[0]['content'] = {i.split(': ')[0]: i.split(': ')[1] for i in decoded_input[0]['content'].split(', ')}
                response.append(decoded_input[0])
        #response = response.reverse()
        return make_response(
            jsonify(response),
            200
        )


class ServeRecords(MethodView):
    def __init__(self):
        self.web3 = Utils.web3
        self.contract = Utils.contract

    def get(self):
        tx_hash = request.args.get("tx_hash")
        tx = self.web3.getTransactionByHash(tx_hash)
        decoded_input = self.contract.decode_function_input(tx.input)
        response = decoded_input
        print(response)
        return make_response(
            jsonify(tx),
            200
        )

    def post(self):
        payload = request.get_json(force=True)
        payload = json.dumps(payload).replace("\"", "")

        tx_hash = self.contract.functions.setPayload(payload).transact()
        tx_receipt = dict(self.web3.eth.waitForTransactionReceipt(tx_hash))
        tx_receipt = json.dumps(tx_receipt, cls=HexJsonEncoder)
        tx_value = self.contract.functions.getPayload().call().replace("{", "").replace("}", "")
        tx_value = {i.split(': ')[0]: i.split(': ')[1] for i in tx_value.split(', ')}
        response = {
            'tx_hash': tx_hash.hex(),
            'tx_receipt': tx_receipt,
            'tx_value' : tx_value
        }
        return make_response(
            jsonify(response),
            200
        )

class SignUp(MethodView):
    def __init__(self):
        self.web3 = Utils.web3
        self.user_contract = Utils.user_contract
        self.contract = Utils.contract

    def post(self):
        payload = request.get_json(force=True)
        payload = json.dumps(payload).replace("\"", "")

        tx_hash = self.user_contract.functions.setPayload(payload).transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        tx_value = self.user_contract.functions.getPayload().call()

        response = {
            'tx_hash': tx_hash.hex(),
            'tx_value' : tx_value
        }
        return make_response(
            jsonify(response),
            200
        )

class Login(MethodView):

    def __init__(self):
        self.web3 = Utils.web3
        self.user_contract = Utils.user_contract

    def post(self):
        payload = request.get_json(force=True)
        user_hash = payload["user_key"]
        tx = self.web3.eth.get_transaction(user_hash)
        decoded_input = list(self.user_contract.decode_function_input(tx.input))
        decoded_input.pop(0)
        decoded_input[0]['user_key'] = user_hash
        decoded_input[0]['content'] = decoded_input[0]['content'].replace("{", "").replace("}", "")
        decoded_input[0]['content'] = {i.split(': ')[0]: i.split(': ')[1] for i in decoded_input[0]['content'].split(', ')}
        response = decoded_input
        return make_response(
            jsonify(response),
            200
        )

