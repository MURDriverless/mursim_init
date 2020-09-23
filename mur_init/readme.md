# mursim_init
Script to automatically clone and checkout all the required branches for a full stack simulation

## Usage of `mur_init.sh`
Update Gazebo to the latest minor version 9.13.2 for use with ROS Melodic, otherwise `gpu_ray` (GPU accelerated LiDAR simulation) will most likely fail to run.

1. Follow upgrade instructions [here](http://gazebosim.org/tutorials?tut=install_ubuntu&cat=install#Alternativeinstallation:step-by-step), but instead of getting the latest `gazebo11`, we want `gazebo9`.
2. Upgrade math package `sudo apt upgrade libignition-math2`

Install `tf2_sensor_msgs` and `glog` (Google logging module)

```
sudo apt install ros-melodic-tf2-sensor-msgs libgoogle-glog-dev
```

Run `mur_init.sh` within the `/src` of your ros/catkin workspace

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
 - [ ] Use launch args in `parse.py` for choose `gitDump.yaml`
 - [ ] Use launch args in `mur_init.sh` for choosing `/src`