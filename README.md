### catkin_ws_innovation running

this is the ROS workspace that contains the robot simulation where we can test using the camera.

## building the workspace

```
$ catkin_make  
$ source devel/setup.bash  
$ source devel/setup.sh  
```

## running gazebo
```
$ roscore    
and then in another terminal run the following command
$ roslaunch robot_simulation robot_spawn.launch
```

## runnning the node which sends the image to the client ( gui )
```
$ rosrun robot_simulation sub.py
```


## --------------------------------------------------------------------------------

### GUI running
```
$ python3 starter_file.py
```
