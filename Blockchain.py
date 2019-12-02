import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request


class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        # Створення блоку генезису
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = \
            {
                'index': len(self.chain) + 1,
                'timestamp': time(),
                'transaction': self.current_transaction,
                # proof - доказ проведеної роботи
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1])
            }
        # перезагрузка поточного списку транзакцій
        self.current_transaction = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transaction.append({'sender': sender, 'recipient': recipient, 'amount': amount})
        # вернет индекс блока, в которой должна будет быть внесена транзакция — а именно следующая
        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            return proof

    @staticmethod
    # Подтверждение доказательства: Содержит ли hash(last_proof, proof) 4 заглавных нуля?
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigets()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigets

    @property
    def last_block(self):
        pass


app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    blockchain.new_transaction(sender='0', recipient=node_identifier, amount=1)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = \
        {
            'message': "New Block Forged",
            'index': block['index'],
            'transaction': block['transaction'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash']
        }
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return "Missing value", 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = \
        {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }
    return \
        jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
