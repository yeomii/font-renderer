from PIL import Image, ImageDraw, ImageFont
import os, glob, string

size = (56, 56)
# 42pt == 56px
font_size = 40

for font_path in glob.iglob("fonts/**/*.ttf", recursive=True):
    font_name = os.path.basename(font_path)
    font = ImageFont.truetype(font_path, font_size)
    
    for c in string.ascii_lowercase:
        im = Image.new('L', size, color=255)
        draw = ImageDraw.Draw(im)
        text_size = draw.textsize(c, font=font, spacing=0)
        padding = ((size[0] - text_size[0])/2, (size[1] - text_size[1])/2)

        draw.text(padding, c, font=font)
        im.save("images/%s_%s.bmp"%(font_name.replace('.ttf', ''), c), "BMP")
