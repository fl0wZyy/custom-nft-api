## Installation

To install all the required dependencies and start the API server please ensure both Python and Pip are set as an environment variable. Running Friendly Frogs.bat will automatically install dependencies required to run the API server as well as initialize an NGROK redirect for the API's public use.

## Setup

### Base Metadata

Please ensure that the metadata for the NFT is stored as a JSON file under the folder Metadata. Follow the format of the test file included in the repo. Ensure that the data does not contain a reference to any IPFS hashes. Also, please ensure to change the following code in scripts/api.py to match your attributes/traits.

```python
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
```


### Base Images

Please ensure all base images are stored under Assets/Base in a .png format and are named according to their tokend ID.


### IPFS Hashes

Under Metadata/images_ipfs you'll find a test JSON file containing some test values. Please clear this data set (do not delete the file) before pushing to production.

### Config File

Change all values in the config file to match your project specifications.

### Use

With the installation and setup now complete you are all set to go. Once running, NGROK will provide a fowarding address. 

#### Metadata API
Take this base address and add ```diff /id/?id=``` to the end to create the Base URI to be used in your contract. For example:```diff http://a17e-213-149-62-137.ngrok.io/id/?id=.``` It is important to note that permanent redirects can be purchased from NGROK to stop unwanted changes if the server goes down. 

#### Minting API

When minting on your website, and after completing ALL contract interactions, please send a POST request to the base forwarding address with the appendix /mint.  For example: ```diff http://a17e-213-149-62-137.ngrok.io/mint```. The post request should contain a package with the following structure:
```json
{
    "bitmap": "#99FE9D#8BA12C#7C4660#917D35#DB5253....",
    "id": 2
}
```

Where a bitmap is a single string containing the hex values of the colors of all the 10x10 boxes in the drawing layer. 


#### Conclusion

After setting up the POST request and the base URI, you're all set. Opensea will be able to retrieve meta data from your server with an average response time of 150 ms. For a more permanent solution, after sellout or after closing the minting function, you can upload the concatenated images to IPFS and set that folder as the base URI to remove the need for a running server.

## License
[MIT](https://choosealicense.com/licenses/mit/)