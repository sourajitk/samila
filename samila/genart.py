import math
import os
import random
import string

from samila import GenerativeImage
from samila import Projection

IMAGE_BG_COLOR = "slategrey"
IMAGE_COLOR = "springgreen"
IMAGE_PROJECTION = Projection.POLAR


def f1(x, y):
    """
    Generates a result to generate an image
    """
    result = random.gauss(0, 1) * x ** 2 - math.sin(y) + abs(y - x)
    return result


def f2(x, y):
    """
    Generates a result to generate an image
    """
    result = random.gauss(2, 1) * y ** 3 - math.cos(x ** 2)
    return -result


def generate_image():
    """
    Generates an image
    """

    file_name = id_generator()
    image = GenerativeImage(f1, f2)
    image.generate()
    image.plot(projection=IMAGE_PROJECTION, color=IMAGE_COLOR, bgcolor=IMAGE_BG_COLOR, spot_size=0.17)
    image.save_image(file_adr=f"outputs/{file_name}.png", depth=10)


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """
    Creates a short id for the image name
    """
    return "".join(random.choice(chars) for _ in range(size))


def main():
    """
    Entry point
    """
    os.makedirs("outputs", exist_ok=True)
    generate_image()


main()