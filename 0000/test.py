import Image

im = Image.open('test.jpg')
print im.size

#print 1
for i in range(1,50):
	im.putpixel((101,i),(255,0,0))
	im.putpixel((102,i),(255,0,0))
	im.putpixel((103,i),(255,0,0))
	im.putpixel((104,i),(255,0,0))

#print 2
for i in range(0,25):
	im.putpixel((125+i,1),(255,0,0))
	im.putpixel((125+i,2),(255,0,0))
	im.putpixel((125+i,3),(255,0,0))
	im.putpixel((125+i,4),(255,0,0))

	im.putpixel((125+i,23),(255,0,0))
	im.putpixel((125+i,24),(255,0,0))
	im.putpixel((125+i,25),(255,0,0))
	im.putpixel((125+i,26),(255,0,0))

	im.putpixel((125+i,47),(255,0,0))
	im.putpixel((125+i,48),(255,0,0))
	im.putpixel((125+i,49),(255,0,0))
	im.putpixel((125+i,50),(255,0,0))

	im.putpixel((147,1+i),(255,0,0))
	im.putpixel((148,2+i),(255,0,0))
	im.putpixel((149,3+i),(255,0,0))
	im.putpixel((150,4+i),(255,0,0))

	im.putpixel((125,24+i),(255,0,0))
	im.putpixel((126,25+i),(255,0,0))
	im.putpixel((127,26+i),(255,0,0))
	im.putpixel((128,28+i),(255,0,0))

#in my os ,there doesn't exit xv viewer
#and the function show() didn't work with out a command 
#to open a image viewer
#apt-get install imagemagick to let display command work
im.show(command = 'display')
