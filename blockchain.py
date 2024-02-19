import json
from datetime import datetime
import hashlib
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List
from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        # type: (int, str) -> Block
        index = len(self.chain) + 1
        timestamp = datetime.now()
        block = Block(index=str(index), timestamp=str(timestamp), proof=proof, previous_hash=previous_hash)

        self.chain.append(block)

        return block

    def get_previous_block(self):
        # type: () -> Block
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        # type: (int) -> int
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = self.hash_operation(new_proof, previous_proof, self.get_previous_block())

            if self.is_hash_operation_valid(hash_operation):
                check_proof = True
            else:
                new_proof += 1

        return new_proof

    @staticmethod
    def hash_operation(new_proof, previous_proof, block):
        # type: (int, int, Block) -> str
        return hashlib.sha256(str(new_proof**2 - previous_proof**2).encode('utf-16')).hexdigest()

    @staticmethod
    def is_hash_operation_valid(hash_op):
        # type: (str) -> bool
        return hash_op[:4] == '0000'

    @staticmethod
    def hash(block):
        # type: (Block) -> str
        block_dict = block.get_block_dict()
        encoded_block = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        # type: (List[Block]) -> bool
        previous_block = chain[0]
        block_index = 1

        while block_index < len(chain):
            block = chain[block_index]

            if block['previous_hash'] != self.hash(previous_block):
                print('Not valid previous hash')
                return False

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = self.hash_operation(proof, previous_proof, block)

            if not self.is_hash_operation_valid(hash_operation):
                print('Hash operation not valid')
                return False

            previous_block = block
            block_index += 1

        return True






