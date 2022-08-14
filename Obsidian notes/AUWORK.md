# AU WORK

## Introduction
The purpose of this text is to document some of the underlying thought behind the work done on the UR3 robot arm, and to function as a "how to" guide for getting it to work.

The paper is divided in the following sections:
- Folder structure
	--> This will describe the folder structure used for the project, and the content of it.
- Python environment 
	--> This describes how to set up the python environment and why it's done the way it is.
- Connecting to the UR3
	--> This will go into how to setup a connection to the UR3 from the desktop.
- URX commands
	--> One of the essential packages is the URX package. This will quickly go over some of the most used packages and how to use it.
- Gripper interface
	--> This will describe how and why the gripper works the way it does, and how to make any changes. 


## Folder structure
A dropbox folder is setup to share any files. The structure is as follows:
- Cad
	- This folder consists of STEP files of the UR3 and a initial draft for the baseplate of the robot.
		This must be opened in solidworks if to be viewed, but it isnt used.
- Camera
	- This folder includes all the files that were on a USB stick that came with the ONROBOT eyes system. It includes datasheets and random folders related for different robotic arms. This is also not used.
- IFC
	- This folder have the IFC files for the project, that Christoff created
- Litterature
	-  In here there are a list of assorted papers that we used for the initial literature review. 
- Manuals
	- This have some different manuals that is downloaded from the internet. The only important is "User_Manual_For_UR_Robots_Quick_Changer_RG2_Eyes_v1.14.0_EN". This walks you throug the setup of the eyebox and the gripper. There is also a physical version of this called "Quick guide for UR robots using OnRobot Eyes". If the robot is somehow factory reset, look through this for assembly instructions and software installations.
- Meetings
	- This have some meeting notes written in it.
- New Software
	- This is a folder with software updates for the URCAP and the computer box. This is not needed, but we downloaded the files and now it's placed here.
- Old
	- This folder is just a "trashcan" with old documents
-  Programming folder
	- This is the main folder for all your programming needs.
		- In the initial folder there are a screenshot with the ethernet setting needed to connect to the robot
		- OnRobot login information
		- URX-jupiter-notebook-master. This is a backup copy of a sample script that goes over the URX programming. This is a good introduction to see how it works.
	- The Christos folder is programs that he sent
	- The Matlab folder is not used
	- UR3_coctrol is not used
	- There are also 3 URX_name folders. 
		- These are playground folders for Asger and Marcus to try stuff out, and when scrips are working, they are moved over to the URX_final folder. 
		- All the codes are written in Jupyter notebooks atm, for ease of use.
- Timesedler
	- This folder have the hours worked from Asger and Marcus



## Python environment
To get the python environment up and running, the following can be done:

In a clean conda enviroment install:
- IFCopenshell. https://anaconda.org/conda-forge/ifcopenshell
	- For some reason, this must be the first package to be installed
	- pythonocc-core https://anaconda.org/conda-forge/pythonocc-core 
		- Then install this package
	- After these 2 packages is installed, then we need to install URX.
	- Note that we dont install the original package, but the pullrequest #45
		- https://github.com/SintefManufacturing/python-urx/pull/45
		- Manual download it and add it to the conda environment.
	- When these packages are installed, the following should be able to be installed in a random order.
	- OpenCV with aruco packages
		- https://pypi.org/project/opencv-contrib-python/
	- Math3d
		- https://anaconda.org/auto/math3d
	- numpy
		- https://anaconda.org/anaconda/numpy
	- pandas
		- https://anaconda.org/anaconda/pandas
	- Pyrealsense2
		- https://pypi.org/project/pyrealsense2/   This is used to inderface with camera

## Connection to the UR3
After the python environment is correctly setup, you should be able to control the UR3. 
Step 1)
	Make sure that the ethernet cable is connected from the UR3 control box to the computer. Make sure that the ethernet-USB adapter is used. This makes it possible for the computer to be connected to the robot and the internet at the same time
Step 2)
	Turn on the UR3 robotic arm, and turn on remote control 
Step 3)
	Go into the internet settings on the desktop and make sure that the IP settings are the same as the ones in the picture on dropbox. The setting were:
		IPv4 turned on manuel
		IP-adress 192.168.1.1
		Length of prefix: 24
		Gateway: 192.168.1.1
		Prefered DNS: 192.168.1.1
		Alternative DNS: empty

Note that step 3 should only be done once, and then the computer should remember these settings.

After this is done, you should be able to connect to the robot via python.

First the packages to control the robot should be loaded:
![[Pasted image 20220422114741.png]]

Then you need to run the following command:
![[Pasted image 20220422114759.png]]

When this is done, you can initialize the connection with:
![[Pasted image 20220422114827.png]]

If connection is successful, it should show a red box like the picture above. 
NOTE that you may have to run this line a couple of times, to ensure that the connection is initialized correctly.

The remaining packages used in the scrips are only for secondary purposes. All the interfacing to the robotic arm is done in the code above.

## Gripper interface
There was some problems getting the gripper to work with python. The URX scrip supposedly supports the RG2 gripper, but we coudnt get it to work. Instead we used the "hack" described here: https://forum.universal-robots.com/t/onrobot-gripper-solved/8784
That means that pair a digital input to the eyebox with a set gripper width. This is not the most elegant solution, but it works. 

We then connected the UR control box and the eye box with the red wires, so that we can send digital outputs from the UR to the eyebox. I then made the following script, that makes it possible to control the gripper to some set widths.
![[Pasted image 20220422125317.png]]



## URX commands
For the best explanations of the URX commands, see URX final/PickPlaceDemo or URX_notebook.
This should go over some of the basic functionality. 






# Meeting 
06-05-2022

### Random notes written 
- Report stuff to Jochen immediately.
- Print out and place on table. **Watch robot and keep hand on red button while operating!**
- Take picture with broken cable for paper?????

Paper outline notes:



Come up with the ideal gantt chart
and then compare to the "final" gantt chart.
We can calculate the waiting time. 

Image where we show all the different pieces (wall, floor, so on), IFC...
He wants a nice picture that shows the IFC and the piece in reality. Nice comparison. 

He wants to replace the logo of AU with some combination of AU and DTU... 
Jochen very much likes the AU/DTU stuff. 

Also important to lift up the pedestrian worker??? 

Some form of live data showing...

Disassembly process 

The journal paper should include assembly, disassembly and reassembly. Everything...
He want this written before EG-ICe happens... 
It's for ICCCBE. june 30 is deadline. 
Include delivery of truck.
Quality issue should be part of this aswell. 
Jochen is a big fan of the guy.
Always include some fun component. 



The conference  paper shuld just be...draft done the latest May 17: 
- Assembly 
- Timetracking
	- Gantt


Paper must be *Stellar*

Write something about how cool we were that we did a lot of stuff on short time. Soooo cool wow. 






