import random
import sys
import numpy as np
import json
import ipfs_upload
import configparser

import PIL.ImageColor
from PIL import Image, ImageDraw, ImageColor

# Initialize Config
parser = configparser.ConfigParser()
parser.read('./config.ini')


def GetBitmap():
    nft_id = int(sys.argv[1])
    f = open(f'./data/{nft_id}.json')
    data = json.load(f)
    bitmap = data['bitmap']
    bitmap = bitmap.split("#")[1:]
    bitmap = np.reshape(bitmap, (100, 100))
    return nft_id, bitmap


def CreateCanvas(canvas_size, canvas_bg_color):
    canvas_element = Image.new("RGBA", canvas_size, canvas_bg_color)
    return canvas_element


def DrawLayer(canvas_element, bitmap, nft_id):
    draw = ImageDraw.Draw(canvas_element)
    for x in range(0, 1000, 10):
        for y in range(0, 1000, 10):
            if bitmap[int(x / 10)][int(y / 10)] != "000000":
                color = ImageColor.getcolor("#" + str(bitmap[int(x / 10)][int(y / 10)]), "RGB")
                draw.rectangle((x, y, x + 10, y + 10), color)
    canvas_element.save(f'./assets/layer/{nft_id}.png', 'PNG')


def Composite(nft_id):
    base = Image.open(f'./assets/base/{nft_id}.png').convert('RGBA')
    layer = Image.open(f'./assets/layer/{nft_id}.png').convert('RGBA')
    comp = Image.alpha_composite(base, layer)
    rgb_im = comp.convert('RGB')
    file_name = str(nft_id) + ".png"
    rgb_im.save("./assets/output/" + file_name)
    print(f'{nft_id} done')


def Upload(nft_id):
    handler = ipfs_upload.PinataPy(parser.get('Pinata', 'Key'), parser.get('Pinata', 'Secret'))
    response = handler.pin_file_to_ipfs(f'./assets/output/{nft_id}.png')
    ipfs_hash = response['IpfsHash']
    with open('./metadata/images_ipfs/ipfs.json', 'r+') as file:
        file_data = json.load(file)
        file_data.append({
            "imageIPFS": ipfs_hash,
            "tokenId": nft_id
        })
        file.seek(0)
        json.dump(file_data, file, indent=4)


def main():
    nft_id, bitmap = GetBitmap()
    canvas = CreateCanvas((1000, 1000), (255, 0, 0, 0))
    DrawLayer(canvas, bitmap, nft_id)
    Composite(nft_id)
    Upload(nft_id)


main()
