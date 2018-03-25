# r200_to_file.py

import cv2
import pyrealsense as pyrs

color_path = "./colour/"
depth_path = "./depth/"
index = -1

write = False

with pyrs.Service() as serv:
    with serv.Device() as cam:
        while True:
            cam.wait_for_frames()  # Wait for the next available image from the camera.
            if write:
                index += 1  # Get the current index for the image filename.

            c = cam.color
            c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)  # Reverse the colour channels for OpenCV.

            dac = cam.dac

            cv2.imshow('Colour', c)
            cv2.imshow('Depth aligned to Colour', dac)

            if write:
                cv2.imwrite('{}{:04d}.png'.format(color_path, index), c)  # Write out the colour file
                cv2.imwrite('{}{:04d}.png'.format(depth_path, index), dac)  # Write out the depth file

            if cv2.waitKey(1) & 0xFF == ord('q') or index >= 10000:
                break

            if cv2.waitKey(1) & 0xFF == ord('r') and not write:
                print("Writing to File now")
                write = True

cv2.destroyAllWindows()
