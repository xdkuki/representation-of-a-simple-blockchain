import datetime
import json
import hashlib
from flask import Flask, jsonify

class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_blockchain(proof=1, previous_hash='0')
    
    def create_blockchain(self,proof,previous_hash):
        block={
            'index':len(self.chain)+1,
            'timestamp':str(datetime.datetime.now()),
            'proof':proof,
            'previous_hash':previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        last_block=self.chain[-1]
        return last_block
    
    def proof_of_work(self,previous_proof):
        new_proof=1
        check_proof=False

        while check_proof is False:
            hash_operation=hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof==True
            else:
                new_proof+=1
        return new_proof

    def hash(self,block):
        encode_bloc=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encode_bloc).hexdigest()