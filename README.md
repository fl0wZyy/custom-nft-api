## Installation

To install all the required dependencies and start the API server please ensure both Python and Pip are set as an environment variable. Running setup.bat will automatically install dependencies required to run the API server as well as initialize an NGROK redirect for the API's public use.

## API

### Index

```python
@app.route('/', methods=['GET'])
def ReturnAll():
    json_dump = json.dumps(minted)
    return json_dump

```

The index endpoint simply returns all of the minted NFTs in JSON format.

### /id/

```python
@app.route('/id/', methods=['GET'])
def ReturnById():
    id_query = int(request.args.get('id'))
    data_set = {minted[id_query]}
    json_dump = json.dumps(data_set)
    return json_dump
```

The /id/ endpoint simply returns a minted NFT by specified ID.

### /mint/

```python
@app.route('/mint/', methods=['POST'])
def Mint():
    request_json = request.json
    mint = {'id': request_json['id'], 'bitmap': request_json['bitmap']}
    minted.append(mint)
    json_dump = json.dumps(minted)
    os.system('python image_generation.py 1 2')
    return json_dump
```

The /mint/ endpoint allows for communication between the website and the image generation infrastructure. The endpoint accepts a JSON with the id of the NFT, to be used for the base layer and a bitmap to be used to reconstruct the drawn layer. Once a request is successfully received, the script runs "image_generation.py" to use the passed data (id and bitmap) to construct the NFT image.

## Image Generation
To be completed.

## License
[MIT](https://choosealicense.com/licenses/mit/)