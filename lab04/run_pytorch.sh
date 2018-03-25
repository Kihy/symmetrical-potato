#!/bin/bash

# Check if the pytorch directory exists. If so, don't bother running the setup again.
if [ ! -d "pytorch" ]
then
    # Download the necessary files.
    git clone https://github.com/amdegroot/ssd.pytorch.git pytorch
    cd pytorch
    git apply ../pytorch_demo.patch  # Apply a patch to fix a few minor issues in the code.
    mkdir weights
    cd weights
    wget https://s3.amazonaws.com/amdegroot-models/ssd_300_VOC0712.pth
    cd ..
else
    # If the setup has already been run, then just move to the pytorch directory in preparation for running the example.
    cd pytorch
fi

# Run the Single Shot Detector example.
python3 -m demo.live --cuda false

# Once we're done, return to the original directory that we started from.
cd ..
