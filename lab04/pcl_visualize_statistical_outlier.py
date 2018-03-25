# pcl_visualize_statistical_outlier.py

import numpy as np
import pcl
import pcl.pcl_visualization

# Load the two point clouds.
inliers = pcl.load("./point_clouds/table_scene_lms400_inliers.pcd")
outliers = pcl.load("./point_clouds/table_scene_lms400_outliers.pcd")

visual = pcl.pcl_visualization.PCLVisualizering('3D Viewer')  # Initialize the visualizer.

# Provide a colour for each of the point clouds.
outliers_color = pcl.pcl_visualization.PointCloudColorHandleringCustom(outliers, 255, 0, 0)
inliers_color = pcl.pcl_visualization.PointCloudColorHandleringCustom(inliers, 0, 255, 0)
# Display both of the point clouds in the same frame.
visual.AddPointCloud_ColorHandler(outliers, outliers_color, b'outliers')
visual.AddPointCloud_ColorHandler(inliers, inliers_color, b'inliers')

while not visual.WasStopped():  # Quit if "q" is pressed.
    visual.SpinOnce()  # Update the screen.
