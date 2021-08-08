# ros-car
```
roscore
rosrun i2cpwm_board i2cpwm_board
rosrun rccar_llc low_level_control.py
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosrun cv_camera cv_camera_node
rosrun web_video_server web_video_server
```
catkin_make
```
catkin_make -j 1 -DCMAKE_CXX_FLAGS="--param ggc-min-expand=20"
```
