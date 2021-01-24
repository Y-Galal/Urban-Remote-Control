# Urban Remote Control

Cairo University Eco-Racing Team<br />
Embedded Autonomous Control Sub-Team<br />
Innovation Project<br />

### Project Dependencies
&nbsp;&nbsp;-> Python 2.7<br />
&nbsp;&nbsp;-> Python 3<br />
&nbsp;&nbsp;-> Pyserial Library<br />
&nbsp;&nbsp;-> PyQt5 Library<br />
&nbsp;&nbsp;-> ROS Melodic<br />
&nbsp;&nbsp;-> OpenCV Library<br />
&nbsp;&nbsp;-> ZMQ Library<br />


## Building The Project
Clone the project on your machine
```
$ git clone https://github.com/heshamkhaledd/Urban-Remote-Control.git
```
Then, Run the following commands in order;
```
$ cd Urban-Remote-Control/server
$ catkin_make
$ source devel/setup.bash  
$ source devel/setup.sh  
```
### Running the Server
Initialize ROS Master by running
```
$ roscore
```
Launch Zed Camera Using
```
$ roslaunch zed_wrapper zed.launch
```
To Initialize the Server, Run
```
$ python2 src/server/scripts/sub.py
```
### Running the Client
You can run the client by going back to the repository root directory and running this
```
$ python3 client/client.py 
```

#### ________________________________________________________________________________ ####
### Simulating the Project
If you want to simulate the project using Gazebo, Run the following command instead of the ```zed.launch``` file<br />
```
roslaunch server robot_spawn.launch
```


#### Important Notes ####
Please make sure the network's ip address you're connected at in both server's script ```sub.py``` and ```client.py```<br />
as they should be connected on the same ip address and sending/reading the data frames on the same port.<br />
to check the ip address the server is connected to, run this command in your terminal
```
$ ifconfig
```
and it will display server's ip address next to ```inet``` label
