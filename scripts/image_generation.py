import random
import sys
import numpy as np

import PIL.ImageColor
from PIL import Image, ImageDraw, ImageColor


def ParseData():
    nft_id = int(sys.argv[1])
    bitmap = sys.argv[2]
    bitmap = bitmap.split("#")[1:]
    bitmap = np.reshape(bitmap, (10,10))
    return nft_id, bitmap


def CreateCanvas(canvas_size, canvas_bg_color):
    canvas_element = Image.new("RGB", canvas_size, canvas_bg_color)
    return canvas_element


def DrawLayer(canvas_element, bitmap):
    draw = ImageDraw.Draw(canvas_element)
    for x in range(0, 100, 10):
        for y in range(0, 100, 10):
            color = ImageColor.getcolor("#"+str(bitmap[int(x / 10)][int(y / 10)]), "RGB")
            draw.rectangle((x, y, x + 10, y + 10), color)
    canvas_element.save("test3.jpg")


def LoadBase(nft_id):
    base = Image.open(f'../assets/base/{nft_id}.png').convert('RGBA')
    return base


def Composite(base, canvas_element, nft_id):
    comp = Image.alpha_composite(base, canvas_element)
    rgb_im = comp.convert('RGB')
    file_name = str(nft_id) + ".png"
    rgb_im.save("../assets/outputs/" + file_name)
    print(f'{nft_id} done')


def main():
    nft_id, bitmap = ParseData()
    canvas = CreateCanvas((100, 100), (255, 255, 255))
    DrawLayer(canvas, bitmap)


main()
