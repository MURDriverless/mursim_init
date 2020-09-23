# `compile_scripts`
Collection of scripts used for downloading and compiling specific version of certain packages used in runtime/development.

## CMake script usage
1. Download required CMake version from [https://cmake.org/download/](https://cmake.org/download/) to the same folder as `install_cmake.sh`
2. Run `sudo sh ./install_cmake.sh`
3. Verify CMake has been installed to `/opt/cmake`
4. Add `export PATH=/opt/cmake${PATH:+:${PATH}}` to `~/.bashrc`
5. Start a new shell and verify CMake has been upgraded with `cmake --version`

## OpenCV usage
1. Install `CUDA 10.0`, recommended via NVidia SDK manager for jetpack 4.3
2. Install `cuDNN 7.6.5`, recommended via NVidia's `.deb` packages
3. Install ROS melodic desktop full as per [http://wiki.ros.org/melodic/Installation/Ubuntu](http://wiki.ros.org/melodic/Installation/Ubuntu)
4. Run `sudo opencv_build.sh`
   - Will take a while to run, expecially on lower end computers, ~30-40min to compile on a 12 thread Ryzen 5 2600.
   - Change `make -j$(nproc)` to `make -j{num_cores}` to change the number of cores used while compiling, i.e. `make -j4`


## TODO
- [ ] Trim/Optimise OpenCV compile script?
- [ ] Fix OpenCV deps?
- [ ] Script to install CUDA/cuDNN/Tensor RT?