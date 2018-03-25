#!/bin/bash

# Check if the orb_slam2 directory exists. If so, don't bother running the setup again.
if [ ! -d "orb_slam2" ]
then
    # Create a directory for storing all our files in.
    mkdir orb_slam2
    cd orb_slam2

    # Download the necessary files.
    wget https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_desk.tgz
    wget https://svncvpr.in.tum.de/cvpr-ros-pkg/trunk/rgbd_benchmark/rgbd_benchmark_tools/src/rgbd_benchmark_tools/associate.py
    wget https://raw.githubusercontent.com/jskinn/ORB_SLAM2-PythonBindings/master/examples/orbslam_rgbd_tum.py
    wget https://raw.githubusercontent.com/raulmur/ORB_SLAM2/master/Examples/RGB-D/TUM3.yaml
    wget --output-document="ORBvoc.txt.tar.gz" https://github.com/raulmur/ORB_SLAM2/blob/master/Vocabulary/ORBvoc.txt.tar.gz?raw=true

    # Extract the compressed files.
    tar -xf rgbd_dataset_freiburg1_desk.tgz
    tar -xf ORBvoc.txt.tar.gz

    # Run the association script on the colour and depth images from the dataset and store the output in associations.txt.
    python associate.py rgbd_dataset_freiburg1_desk/rgb.txt rgbd_dataset_freiburg1_desk/depth.txt > rgbd_dataset_freiburg1_desk/associations.txt
else
    # If the setup has already been run, then just move to the orb_slam2 directory in preparation for running the ORB_SLAM2 algorithm.
    cd orb_slam2
fi

# Run the ORB_SLAM2 algorithm on the dataset we just downloaded.
python3 ./orbslam_rgbd_tum.py ./ORBvoc.txt ./TUM3.yaml  ./rgbd_dataset_freiburg1_desk/ ./rgbd_dataset_freiburg1_desk/associations.txt

# Once we're done, return to the original directory that we started from.
cd ..
