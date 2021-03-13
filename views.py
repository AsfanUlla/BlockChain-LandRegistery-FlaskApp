from flask import request, jsonify, make_response, render_template
from utils import Utils
from utils import tx_to_json
from flask.views import MethodView


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
                decoded_input = self.contract.decode_function_input(txj)
                response.append(decoded_input)
        return make_response(
            str(response),
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
        payload = request.get_json()
        tx_hash = self.contract.functions.setPayload(payload).transact()
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        tx_value = self.contract.functions.getPayload().call()
        response = {
            'tx_hash': tx_hash,
            'tx_receipt': tx_receipt,
            'tx_value' : tx_value
        }
        return make_response(
            jsonify(response),
            200
        )

