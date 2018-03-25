# r200_parameters.py

import cv2
import pyrealsense as pyrs

with pyrs.Service() as serv:
    with serv.Device() as cam:

        while True:
            cam.wait_for_frames()  # Wait for the next available image from the camera.

            # It is possible to set multiple parameters at once using a list of
            # (parameter, value) tuples
            custom_options_list = [(rs_option.RS_OPTION_R200_LR_AUTO_EXPOSURE_ENABLED, 0),
                                    (rs_option.RS_OPTION_R200_EMITTER_ENABLED, 1)]
            cam.set_device_options(*zip(*custom_options))

            # Alternatively, a single option can be set with a function call.
            cam.set_device_option(rs_option.RS_OPTION_R200_LR_GAIN, 100)

            # Finally, this function will retrieve the value of a particular parameter.
            x = cam.get_device_option(rs_option.RS_OPTION_R200_LR_GAIN)


            cv2.imshow('Infrared', cam.infrared)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cv2.destroyAllWindows()
