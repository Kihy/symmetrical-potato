# pcl_from_r200.py

import pyrealsense as pyrs

import pcl
import pcl.pcl_visualization

visual = pcl.pcl_visualization.CloudViewing()  # Initialize the visualizer.

with pyrs.Service() as serv:
    with serv.Device() as cam:
        while not visual.WasStopped():  # Loop until "q" is pressed on the keyboard.
            cam.wait_for_frames()  # Wait for the next available image from the camera.

            pc = cam.pointcloud.reshape(-1,3)  # Convert the points into a simple array of X,Y,Z values.

            cloud = pcl.PointCloud(pc)  # Create a PointCloud object from the r200 points.
            visual.ShowMonochromeCloud(cloud, b'cloud')
