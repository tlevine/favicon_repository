#!/usr/bin/env python2

from PIL import Image
import os

MAX_NUMBER = int('1' * 256, 2)

def favicon(number, outpath = '.'):
    number_int = int(number)
    if number_int > MAX_NUMBER:
        raise ValueError('I do not generate favicons for numbers greater than %d.' % MAX_NUMBER)
    elif number_int < 0:
        raise ValueError('Favicon number must not be negative.')

    # This should be 256, not 258; is this a bug in Python?
    image_vector = map(int, '{:#0258b}'.format(number_int)[2:])
    #print image_vector

    im = Image.new("L", (16, 16))
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            im.putpixel((x,y), 255 * image_vector.pop(0))

    assert image_vector == [], "Something is wrong with the image-creation algorithm."

    im.save(os.path.join(outpath, '{0}.png'.format(number)))
    sh = 'cd {outpath}; convert {number}.png {number}.ico; cd - > /dev/null'
    os.system(sh.format(number = number, outpath = outpath))

# The Python Favicon Format (pff)

def pff_generator(proportion = 1):
    i = 0
    end = int(proportion * MAX_NUMBER)
    while i < end:
        i+=1 # This number, i, is the pff representation of a favicon
    if proportion == 1:
        print "Done generating all b/w favicons"
    else:
        print "Generating %d favicons" % end

def pff_reader(filename):
    "Generate a favicon from a .pff file"
    favicon(int(open(filename).read().strip()))

if __name__ == '__main__':
    import time
    p = 0.0000000000000000000000000000000000000000000000000000000000000000000001
    for p in [p/10, p, p*10]:
        start = time.time()
        pff_generator(proportion = p)
        end = time.time()
        delta = end - start
        years = (delta / p) * 3600 * 24 * 356.25
        print("Generating all favicons in pff should take about %d years on this CPU." % years)

    # Writing some to files
    print time.time()
    favicon(MAX_NUMBER - 3, 'results')
    print time.time()
    favicon(MAX_NUMBER/3, 'results')
    print time.time()
