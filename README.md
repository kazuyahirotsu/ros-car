# ros-car
run this to use i2cpwm_board
```
sudo apt install libi2c-dev
```
run this to launch
```
sudo chmod 666 /dev/i2c-1 #raspberry pi
roslaunch rccar_llc.launch #raspberry pi
roslaunch rccar_llc_laptop.launch #laptop
```
catkin_make on raspberry pi
```
catkin_make -j 1 -DCMAKE_CXX_FLAGS="--param ggc-min-expand=20"
```
