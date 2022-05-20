import os
from PIL import Image
from numpy import resize

def resize_image(image, width, height, fill_color = (0, 0, 0)):
    '''
    Takes an image and returns a image of size width x height
    Input will keep the same aspect ratio. If target aspect
    ratio is different from the input image aspect ratio, the empty
    area will be filled with fill_color.

    :param image: PIL.Image object - The image that is going to be resized
    :param width: integer. Size in pixels of new image width
    :param height: integer. Size in pixels of new image height
    :param fill_color: tuple. RGB color code of background color
    :return: PIL.Image object - Imaged resized.
    '''
    x, y = image.size
    ratio = x / y

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

def resize_all_images_in_folder(folder, width, height, fill_color = (0, 0, 0)):
    '''
    Takes all images in a folder and resized them using resize_image()

    :param folder: string. Location of the images
    :param width: integer. Size in pixels of new image width
    :param height: integer. Size in pixels of new image height
    :param fill_color: tuple. RGB color code of background color
    '''
    directory = sorted(os.listdir(folder))

    for i, filename in enumerate(directory):
        if filename != '.gitkeep':
            image = Image.open(f'{folder}/' + filename)
            new_image = resize_image(image, width, height, fill_color = fill_color)
            new_image.save(f'images/resized/resized{i:03d}.png')