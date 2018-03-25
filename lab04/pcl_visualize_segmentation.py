# pcl_visualize_segmentation.py

import numpy as np
import pcl
import pcl.pcl_visualization

# Load the two point clouds.
original = pcl.load("./point_clouds/table_scene_mug_stereo_textured.pcd")
inliers = pcl.load("./point_clouds/table_scene_mug_stereo_textured_plane.pcd")
outliers = pcl.load("./point_clouds/table_scene_mug_stereo_textured_cylinder.pcd")

visual = pcl.pcl_visualization.PCLVisualizering('3D Viewer')  # Initialize the visualizer.

# Provide a colour for each of the point clouds.
original_color = pcl.pcl_visualization.PointCloudColorHandleringCustom(original, 255, 255, 255)
outliers_color = pcl.pcl_visualization.PointCloudColorHandleringCustom(outliers, 255, 0, 0)
inliers_color = pcl.pcl_visualization.PointCloudColorHandleringCustom(inliers, 0, 255, 0)
# Display both of the point clouds in the same frame.
visual.AddPointCloud_ColorHandler(original, original_color, b'original')
visual.AddPointCloud_ColorHandler(outliers, outliers_color, b'outliers')
visual.AddPointCloud_ColorHandler(inliers, inliers_color, b'inliers')

while not visual.WasStopped():  # Quit if "q" is pressed.
    visual.SpinOnce()  # Update the screen.
