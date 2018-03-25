# r200_segmentation.py

import numpy as np
import cv2
import os

color_path = "./colour/"
depth_path = "./depth/"
index = -1

# Load the list of image filenames.
# We are assuming that the depth files have the exact same filename.
color_images = os.listdir(color_path)
color_images.sort()  # Make sure we get all our images in order.

while True:  # Loop over the images until we decide to quit.
    index = (index + 1) % len(color_images)
    filename = color_images[index]

    # Note that if the cv2.IMREAD_ANYDEPTH flag is missing,
    # OpenCV will load the 16-bit depth data as an 8-bit image.
    c = cv2.imread("{}{}".format(color_path, filename))
    d = cv2.imread("{}{}".format(depth_path, filename), cv2.IMREAD_GRAYSCALE | cv2.IMREAD_ANYDEPTH)
    # Create a new 8-bit colour version of the depth data for drawing on later.
    # This is scaled for visibility (65536 / 3500 ~= 18)
    d_scaled = cv2.cvtColor(d, cv2.COLOR_GRAY2BGR)
    d_scaled = ((d_scaled*18)/(256)).astype('uint8')

    # Do a simple "in range" threshold to find all objects between 2 and 5 units of distance away.
    # Note that each increment is equal to approximately 256mm. This is because the inRange function
    # only accepts 8-bit integers, so we must scale it down.
    thresh = cv2.inRange((d / 256).astype(np.uint8), 2, 15)

    # Perform some morphological operations to help distinguish the features in the image.
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=5)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=10)

    # Detect the contour in the image.
    _, contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contour around the detected object.
    cv2.drawContours(c, contours, -1, (0,0,255), 1)
    cv2.drawContours(d_scaled, contours, -1, (0,0,255), 1)
    # Use the moments of the contour to draw a dot at the centroid of the object.
    for contour in contours:
        moments = cv2.moments(contour)
        cX = int(moments["m10"] / moments["m00"])
        cY = int(moments["m01"] / moments["m00"])
        # Draw the centroid on the colour and depth images.
        cv2.circle(c, (cX, cY), 7, (0, 255, 0), -1)
        cv2.circle(d_scaled, (cX, cY), 7, (0, 255, 0), -1)

    cv2.imshow('c', c)
    cv2.imshow('d', d_scaled)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
