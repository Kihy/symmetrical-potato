# pcl_segmentation.py

import pcl

cloud = pcl.load('./point_clouds/table_scene_mug_stereo_textured.pcd')

print("Original Point Cloud Size:", cloud.size, "points")

# Create a passthrough filter that removes points outside of the range 0 to 1.5 in the Z axis.
fil = cloud.make_passthrough_filter()
fil.set_filter_field_name("z")
fil.set_filter_limits(0, 1.5)
cloud_filtered = fil.filter()

print("Filtered Point Cloud Size:", cloud_filtered.size, "points")

# Calculate the surface normals for each point by fitting a plane to the nearest
# 50 neighbours to the candidate point.
seg = cloud_filtered.make_segmenter_normals(ksearch=50)
seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)  # Fit a plane to the points.
seg.set_optimize_coefficients(True)  # Do a little bit more optimisation once the plane has been fitted.
seg.set_normal_distance_weight(0.1)
seg.set_method_type(pcl.SAC_RANSAC)  # Use RANSAC for the sample consensus algorithm.
seg.set_max_iterations(100)  # Number of iterations for the RANSAC algorithm.
seg.set_distance_threshold(0.03)  # The max distance from the fitted model a point can be for it to be an inlier.
inliers, model = seg.segment()  # Returns all the points that fit the model, and the parameters of the model.

print("Plane Model Parameters:", model)

# Save all the inliers as a point cloud. This forms the table which the mug sits on.
cloud_plane = cloud_filtered.extract(inliers, negative=False)
pcl.save(cloud_plane, './point_clouds/table_scene_mug_stereo_textured_plane.pcd')

# Create a new point cloud from all the outliers of the previous segmentation.
# We are going to fit a mug to these points
cloud_cyl = cloud_filtered.extract(inliers, negative=True)

# Once again, make a new segmenter, but this time fit a cylinder to the remaining points.
seg = cloud_cyl.make_segmenter_normals(ksearch=50)
seg.set_model_type(pcl.SACMODEL_CYLINDER)  # Fit a cylinder.
seg.set_optimize_coefficients(True)
seg.set_normal_distance_weight(0.1)
seg.set_method_type(pcl.SAC_RANSAC)
seg.set_max_iterations(10000)
seg.set_distance_threshold(0.05)
seg.set_radius_limits(0, 0.1)  # Set some minimum and maximum limits on the cylinder radius.
inliers, model = seg.segment()

print("Cyliner Model Parameters:", model)

cloud_cylinder = cloud_cyl.extract(inliers, negative=False)
pcl.save(cloud_cylinder, './point_clouds/table_scene_mug_stereo_textured_cylinder.pcd')
