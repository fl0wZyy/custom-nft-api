import json
import os
from flask import *

# Set the Flask App
app = Flask(__name__)

# Initialize Minted Database
minted = [{'id': 1, 'bitmap': 'test'}]


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
    data_set = {minted[id_query]}
    json_dump = json.dumps(data_set)
    return json_dump


# Add An NFT to the Minted List
@app.route('/mint/', methods=['POST'])
def Mint():
    request_json = request.json
    mint = {'id': request_json['id'], 'bitmap': request_json['bitmap']}
    minted.append(mint)
    json_dump = json.dumps(minted)
    os.system('python image_generation.py 1 2')
    return json_dump


if __name__ == "__main__":
    # Initialize the Flask App at Specified Port
    # Forward the Port Using NGROK For Public Net Use
    app.run(port=7777)
