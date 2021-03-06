# `mur_init`
Script to clone all ROS packages for running a full stack simulation.

## Usage of `mur_init.sh`
Update Gazebo to the latest minor version 9.13.2 for use with ROS Melodic, otherwise `gpu_ray` (GPU accelerated LiDAR simulation) will most likely fail to run.

1. Follow upgrade instructions [here](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install#Alternativeinstallation:step-by-step), but instead of getting the latest `gazebo11`, we want `gazebo9`.
2. Upgrade math package `sudo apt upgrade libignition-math2`

Install `tf2_sensor_msgs` and `glog` (Google logging module)

```
sudo apt install ros-melodic-tf2-sensor-msgs libgoogle-glog-dev
```

Run `mur_init.sh` within the `/src` of your ros/catkin workspace

### Installing NVidia Preqs
Use NVidia SDK manager for jetpack 4.3

```
CUDA 10.0
CUDNN 7.6.3
TensorRT 7.0.0
```

Install `CUDA 10.0` via runfile; `CUDNN` and `TensorRT` via `.dev` from NVidia site, read the documentations,

https://docs.nvidia.com/cuda/archive/10.0/cuda-installation-guide-linux/index.html#runfile

https://docs.nvidia.com/deeplearning/cudnn/archives/cudnn_763/cudnn-install/index.html#installlinux-deb

https://docs.nvidia.com/deeplearning/tensorrt/archives/tensorrt-700/tensorrt-install-guide/index.html#installing-debian

## Updating `mur_init.sh`
### Manual
Just manually add `git clone` lines to the script or modify the branch to checkout `--branch {branch_name}`

Try to keep MUR repos checked out via ssh, for the ease of people in linux using ssh credentials for push/pull. i.e.

SSH: `git@github.com:MURDriverless/mursim.git`

HTPP: `https://github.com/MURDriverless/mursim.git`

### Automatic with `parse.py`
Using `parse.py` requires [`PyYAML`](https://pypi.org/project/PyYAML/) and [`vsctool`](https://github.com/dirk-thomas/vcstool)

In the root folder of you ros/catkin workspace run,
```
vcs export > gitDump.yaml
```

Running `parse.py` with `gitDump.yaml` in the same folder should produce `mur_init.sh` with all your current repos and their current checked-out branches.

## TODO:
 - [ ] Clean up CUDA install instructions
 - [ ] Use launch args in `parse.py` for choose `gitDump.yaml`
 - [ ] Use launch args in `mur_init.sh` for choosing `/src`
