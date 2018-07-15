'''
add a number on your avatar picture
'''
from PIL import Image, ImageDraw, ImageFont
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fileName", default="../static/avatar.JPG")
    return parser.parse_args()

def add_number(fileName):
    im = Image.open(fileName)
    fnt = ImageFont.truetype('Times', 100) # set the font
    draw = ImageDraw.Draw(im)
    draw.text((im.size[0]*0.75, im.size[0]*0.2), '8', fill=(255,0,0), font=fnt)
    im.show()
    im.save("../static/result.png", "PNG")

if __name__ == "__main__":
    args = arg_parser()
    add_number(args.fileName)