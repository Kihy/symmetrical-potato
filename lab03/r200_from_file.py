# r200_from_file.py

import cv2
import os

color_path = "./colour/"
depth_path = "./depth/"
index = -1

# Load the list of image filenames.
# We are assuming that the depth files have the exact same filename.
color_images = os.listdir(color_path)
color_images.sort()

while True:  # Loop over the images until we decide to quit.
    index = (index + 1) % len(color_images)
    filename = color_images[index]

    # Note that if the cv2.IMREAD_ANYDEPTH flag is missing, OpenCV will load the 16-bit depth data as an 8-bit image.
    c = cv2.imread("{}{}".format(color_path, filename))
    d = cv2.imread("{}{}".format(depth_path, filename), cv2.IMREAD_GRAYSCALE | cv2.IMREAD_ANYDEPTH)

    cv2.imshow('c', c)
    cv2.imshow('d', d * 18)  # Scale the depth data for visibiliy (65536 / 3500 ~= 18)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
