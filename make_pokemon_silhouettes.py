import os
import glob
import numpy as np
import cv2
import imutils

BACKGROUND_IMAGE = cv2.imread('pokemon_images/whos_that_pokemon_background.png')

image_paths = glob.glob('pokemon_images/pokemon/*')

for image_path in image_paths:
    # Read, resize, note new dims
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    image = imutils.resize(image, height=600)
    h, w = image.shape[:2]

    # Copy background and place pokemon on
    x1 = 200
    y1 = 240
    background_copy = BACKGROUND_IMAGE.copy()
    poke_place = background_copy[y1:y1 + h, x1:x1 + w]
    poke_place[np.where(image[:, :, 3] > 0)] = [0, 0, 0]
    background_copy[y1:y1 + h, x1:x1 + w] = poke_place

    file_name = os.path.basename(image_path)
    output_path = os.path.join('pokemon_images/silhouettes', file_name)

    cv2.imwrite(output_path, background_copy)
