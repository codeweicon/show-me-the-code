from PIL import Image, ImageDraw, ImageFont
import sys

def add_num(filePath, num):
    print filePath
    img = Image.open(filePath)
    size = img.size
    print size
    fontsize = size[1]/4
    myfont = ImageFont.truetype('Futura.ttf', fontsize)
    ImageDraw.Draw(img).text((2 * fontsize, 0), str(num), font = myfont, fill = 'red')
    img.save('avatar_added.jpg')
    img.show(command = 'display')

if __name__=='__main__':
	add_num(sys.argv[1],sys.argv[2])
