# ros-car
run this to use i2cpwm_board
```
sudo apt install libi2c-dev
```
run this to launch
```
sudo chmod 666 /dev/i2c-1 #raspberry pi
roslaunch rccar_llc.launch #raspberry pi

rosparam set cv_camera/devide_id 0 #front cam on laptop
rosparam set cv_camera/device_id 2 #usb cam with laptop
roslaunch rccar_llc_laptop.launch #laptop
```
catkin_make on raspberry pi
```
catkin_make -j 1 -DCMAKE_CXX_FLAGS="--param ggc-min-expand=20"
```
