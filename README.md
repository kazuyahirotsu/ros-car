# ros-car
### run this to use i2cpwm_board
```
sudo apt install libi2c-dev
```
### run this to launch
```
sudo chmod 666 /dev/i2c-1 #raspberry pi
roslaunch rccar_llc.launch #raspberry pi

rosparam set cv_camera/devide_id 0 #front cam on laptop
rosparam set cv_camera/device_id 2 #usb cam with laptop
roslaunch rccar_llc_laptop.launch #laptop
```
### catkin_make on raspberry pi  
You might need swap file for this. My raspberry pi run out of RAM when running catkin_make.  
I followed [this website](https://www.digitalocean.com/community/tutorials/how-to-add-swap-space-on-ubuntu-20-04-ja.amp) to create swap file.
```
catkin_make -j 1
```
