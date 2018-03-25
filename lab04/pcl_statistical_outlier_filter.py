# pcl_statistical_outlier_filter.py

import pcl

p = pcl.load("./point_clouds/table_scene_lms400.pcd")  # Load the point cloud.

fil = p.make_statistical_outlier_filter()  # Create the filter object.
fil.set_mean_k(50)  # Analyze the nearest 50 neighbours.
fil.set_std_dev_mul_thresh(1.0)  # Set the filter threshold to 1 standard deviation.

# Save the filtered pointcloud.
pcl.save(fil.filter(), "./point_clouds/table_scene_lms400_inliers.pcd")
# Save the outliers to a separate point cloud.
fil.set_negative(True)
pcl.save(fil.filter(), "./point_clouds/table_scene_lms400_outliers.pcd")
