import os
from PIL import Image
from numpy import resize

def resize_image(image, size, fill_color = (0, 0, 0)):
    '''
    Takes an image and returns a image of size width x height
    Input will keep the same aspect ratio. If target aspect
    ratio is different from the input image aspect ratio, the empty
    area will be filled with fill_color.

    :param image: PIL.Image object - The image that is going to be resized
    :param size: tuple. (width, height)
    :param fill_color: tuple. RGB color code of background color
    :return: PIL.Image object - Imaged resized.
    '''
    x, y = image.size
    ratio = x / y
    width, height = size

    if ratio > width / height:
        new_width = width
        new_height = int(new_width / ratio)
        upper_left = ((0, int(abs(new_height - height) / 2)))
    else:
        new_height = height
        new_width = int(ratio * new_height)
        upper_left = ((int(abs(new_width - width) / 2), 0))

    image = image.resize((new_width, new_height))

    new_image = Image.new('RGBA', (width, height), fill_color)
    new_image.paste(image, upper_left)
    return new_image


def resize_all_images_in_folder(size, fill_color = (0, 0, 0)):
    '''
    Takes all images in a folder and resized them using resize_image()

    :param folder: string. Location of the images
    :param width: integer. Size in pixels of new image width
    :param height: integer. Size in pixels of new image height
    :param fill_color: tuple. RGB color code of background color
    '''
    directory = sorted(os.listdir('images/original'))

    for i, filename in enumerate(directory):
        if filename != '.gitkeep':
            image = Image.open('images/original/' + filename)
            new_image = resize_image(image, size, fill_color = fill_color)
            new_image.save(f'images/resized/resized{i:03d}.png')


def images_need_resizing(size):
    '''
    Return False if all images have the same size.
    returns True otherwise.

    :param size: tuple. Size expected for the images.
    '''
    directory = sorted(os.listdir('images/original'))
    for image in directory:
        if image != '.gitkeep':
            image = Image.open('images/original/' + image)
            if image.size != size: return True
    return False