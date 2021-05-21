# pick-place_demo

# HOW TO USE: 
1. This repo does not contain the source code. Clone, build and source AMBF: https://github.com/WPI-AIM/ambf (Author: Adnan Munawar)

2. Once we have installed the simulator, clone this repo outside AMBF e.g. your home folder. Let's call this repo `pick-place_demo`

3. Now run the demo as: 

```
cd <ambf_1.0 source code location>/bin/lin-x86_64
~/ambf/bin/lin-x86_64$ ./ambf_simulator --launch_file <path where you saved this repo>/pick-place_demo/ambf_models/descriptions/launch.yaml -l 0,1,2,3,4
```
For example in my case is: 
```
cd <ambf_1.0 source code location>/bin/lin-x86_64
~/ambf/bin/lin-x86_64$ ./ambf_simulator --launch_file /home/nearlab/pick-place_demo/ambf_models/descriptions/launch.yaml -l 0,1,2,3,4
```

two windows should pop up with two different camera views. 


4. You can now control the PSMs via mouse. For this you will need to run 2 scripts (placed in the folder *script*) in a new terminal:

- The first script is `mouse_teleop.py`. You can run it as: 
```
cd pick-place_demo/scripts
~/pick-place_demo/script$ python mouse_teleop.py
```
After running it, a white square (similar to a virtual trackpad) should appear. You can control the PSMs only if you move the mouse inside this square. 

- The second script is `teleop.py`. This will enable the communication between the mouse and the simulator so that you can start controlling the PSMs. You can run it as: 
```
cd pick-place_demo/scripts
~/pick-place_demo/script$ python teleop.py
```
The commands are the following: 
  - left button allows you to move the psm along the x and y axis. 
  - scrolling wheel up/down allows you to zoom in/out 
  - right button for closing the gripper
  - scrolling wheel pushed allows you to switch between PSMs. 


## ENJOY!
