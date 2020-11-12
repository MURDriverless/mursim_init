# `compile_scripts`
Collection of scripts used for downloading and compiling specific version of certain packages used in runtime/development.

## CMake script usage
1. Download required CMake version from [https://cmake.org/download/](https://cmake.org/download/) to the same folder as `install_cmake.sh`
2. Run `sudo sh ./install_cmake.sh`
3. Verify CMake has been installed to `/opt/cmake`
4. Add `export PATH=/opt/cmake/bin${PATH:+:${PATH}}` to `~/.bashrc`
5. Start a new shell and verify CMake has been upgraded with `cmake --version`

## OpenCV usage
1. Install `CUDA 10.0`, recommended via NVidia SDK manager for jetpack 4.3
2. Install `cuDNN 7.6.5`, recommended via NVidia's `.deb` packages
3. Install ROS melodic desktop full as per [http://wiki.ros.org/melodic/Installation/Ubuntu](http://wiki.ros.org/melodic/Installation/Ubuntu)
4. Run `sudo opencv_build.sh`
   - Will take a while to run, expecially on lower end computers, ~30-40min to compile on a 12 thread Ryzen 5 2600.
   - Change `make -j$(nproc)` to `make -j{num_cores}` to change the number of cores used while compiling, i.e. `make -j4`

### CUDNN 8.0+ (Jetpack 4.4) and OpenCV 4.1.1
https://forums.developer.nvidia.com/t/cudnn-8-0-of-jp4-4p-recognized-under-7-5-version-by-opencv4-2-and-4-3/128167

```
Hi,

In v8.0, we separate cuDNN package into different usage to save the memory for loading library.
As a result, version information is moved from /usr/include/cudnn.h to /usr/include/cudnn_version.h.

diff --git a/cmake/FindCUDNN.cmake b/cmake/FindCUDNN.cmake
index e115f80..4544308 100644
--- a/cmake/FindCUDNN.cmake
+++ b/cmake/FindCUDNN.cmake
@@ -65,7 +65,7 @@ endif()
 
 # extract version from the include
 if(CUDNN_INCLUDE_DIR)
-  file(READ "${CUDNN_INCLUDE_DIR}/cudnn.h" CUDNN_H_CONTENTS)
+  file(READ "${CUDNN_INCLUDE_DIR}/cudnn_version.h" CUDNN_H_CONTENTS)
 
   string(REGEX MATCH "define CUDNN_MAJOR ([0-9]+)" _ "${CUDNN_H_CONTENTS}")
   set(CUDNN_MAJOR_VERSION ${CMAKE_MATCH_1} CACHE INTERNAL "")
```

Might be pointless thought, CUDNN is not used by OpenCV until 4.2+ More of a FYI

https://github.com/opencv/opencv/issues/17372#issuecomment-633630770

## TODO
- [ ] Trim/Optimise OpenCV compile script?
- [ ] Fix OpenCV deps?
- [ ] Script to install CUDA/cuDNN/Tensor RT?
- [ ] Upgrade to Jetpack 4.4
- [ ] Use `snap` for `cmake`?
