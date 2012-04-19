from PIL import Image
import os

MAX_NUMBER = int('1' * 256, 2)

def favicon(number):
    number_int = int(number)
    if number_int > MAX_NUMBER:
        raise ValueError('I do not generate favicons for numbers greater than %d.' % MAX_NUMBER)
    elif number_int < 0:
        raise ValueError('Favicon number must not be negative.')

    # This should be 256, not 258; is this a bug in Python?
    image_vector = map(int, '{:#0258b}'.format(number_int)[2:])

    im = Image.new("RGB", (16, 16))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            im.putpixel((x,y), image_vector.pop(0))

    assert image_vector == [], "Something is wrong with the image-creation algorithm."

    im.save('tmp.png')
    os.system('convert tmp.png %d.ico; rm tmp.png' % number)

favicon(426986986969696969696998798798798789263492349823416230512368051246089)
