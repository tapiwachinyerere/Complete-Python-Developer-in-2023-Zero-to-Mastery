from PIL import Image, ImageFilter

# im = Image.open('pikachu.jpg')

# print(im.format)
# print(im.size) #Size
# print(im.mode) #Shows us the colouring
# print(dir(im)) 

# filtered_im = im.filter(ImageFilter.BLUR)

# filtered_im.save('blur.png', 'png') #blurred image filter

# filtered_im2 = im.convert('L') #convert to greyscale

# filtered_im2.save('grey.png', 'png') #save as greyscale

# filtered_im2.show() #opens the image

# resize = filtered_im2.resize((300, 300)) #resize accepts a tuple!
# resize.save('resize.png', 'png')

# box = (100, 100, 400, 400)
# region = filtered_im2.crop(box)

# region.save('cropped.png', 'png')

##Reducing file size
im = Image.open('astro.jpg')

im.thumbnail((400,400))

im.save('thumbnail.jpg')