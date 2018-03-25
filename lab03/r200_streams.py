# r200_streams.py

import cv2
import pyrealsense as pyrs

with pyrs.Service() as serv:
    with serv.Device() as cam:

        while True:
            cam.wait_for_frames()  # Wait for the next available image from the camera.

            c = cam.color
            c = cv2.cvtColor(c, cv2.COLOR_RGB2BGR)  # Reverse the colour channels for OpenCV.

            cad = cam.cad
            cad = cv2.cvtColor(cad, cv2.COLOR_RGB2BGR)  # Reverse the colour channels for OpenCV.

            d = cam.depth * 18  # Roughly map a maximum range of 3500mm to 65535 (16-bit integer).
            dac = cam.dac * 18  # Roughly map a maximum range of 3500mm to 65535 (16-bit integer).

            cv2.imshow('Colour', c)
            cv2.imshow('Depth', d)
            cv2.imshow('Depth Aligned to Colour', dac)
            cv2.imshow('Colour Aligned to Depth', cad)
            cv2.imshow('Infrared', cam.infrared)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cv2.destroyAllWindows()
