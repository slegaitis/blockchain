from flask import Flask, jsonify

from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

@app.route('/mine-block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)

    block = blockchain.create_block(proof=proof, previous_hash=previous_hash)

    response = {
        'message': "Congratulations you just mined a block!",
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200


@app.route('/get-chain', methods=['GET'])
def get_chain():
    chain = blockchain.chain

    response = {
        'chain': chain,
        'length': len(chain)
    }

    return jsonify(response), 200

@app.route('/is_valid', methods=['GET'])
def is_chain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    
    if is_valid:
        return jsonify({'message': 'Blockchain is valid.' }), 200
    
    
    return jsonify({'message': 'Chain is not valid!'}), 200
    
    
if __name__ == "__main__":
    app.run(debug=True)
