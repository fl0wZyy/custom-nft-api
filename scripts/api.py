import json
import os
from flask import *
from web3 import Web3
import configparser

# Initialize Config
parser = configparser.ConfigParser()
parser.read('./config.ini')

# Set the Flask App and Establish Web3 Connection
app = Flask(__name__)
w3 = Web3(Web3.HTTPProvider(parser.get('Contract', 'Infura')))

print(f'Web3 Connection: {w3.isConnected()}')

# Initialize Minted Database
minted = [{'id': 1, 'bitmap': 'test'}]

# Connect Smart Contract
contract_address = parser.get('Contract', 'Address')
file = open('./data/abi.json')
contract_abi = json.load(file)
contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# Setting the API Endpoints

# Return All Minted NFTs
@app.route('/', methods=['GET'])
def ReturnAll():
    json_dump = json.dumps(minted)
    return json_dump


# Return A Specific Minted NFT
@app.route('/id/', methods=['GET'])
def ReturnById():
    id_query = int(request.args.get('id'))
    total_supply = contract.functions.totalSupply().call()
    if id_query < total_supply:
        f = open('./metadata/traits.json')
        traits_all = json.load(f)
        trait = traits_all[id_query]
        f = open('./metadata/images_ipfs/ipfs.json')
        ipfs = json.load(f)
        attributes = [
            {
                "trait_type": "Health",
                "value": trait["Health"]
            },
            {
                "trait_type": "Attack Power",
                "value": trait["Attack Power"]
            },
        ]
        token_name = f'Friendly Frog #{id_query}'
        image_ipfs = ipfs[id_query]['imageIPFS']
        metadata = {
            "name": token_name,
            "description": "Description",
            "tokenId": id_query,
            "image": f'https://gateway.pinata.cloud/ipfs/{image_ipfs}',
            "external_url": parser.get('Website', 'Address'),
            "attributes": attributes
        }
        json_dump = json.dumps(metadata)
        return json_dump
    else:
        return make_response(jsonify("The Requested Friendly Frog is Out of Range"), 404)


# Add An NFT to the Minted List
@app.route('/mint/', methods=['POST'])
def Mint():
    request_json = request.json
    mint = {'id': request_json['id'], 'bitmap': request_json['bitmap']}
    minted.append(mint)
    json_dump = json.dumps(mint)
    with open(f'data/{request_json["id"]}.json', 'w') as f:
        json.dump(mint, f, indent=4)
    os.system(f"python scripts/image_generation.py {request_json['id']}")
    return json_dump


if __name__ == "__main__":
    # Initialize the Flask App at Specified Port
    # Forward the Port Using NGROK For Public Net Use
    app.run(port=7777)
