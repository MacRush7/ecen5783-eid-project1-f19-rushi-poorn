# ECEN 5783 EID PROJECT-1 (Fall-2019)

**Project Collaborators/Developers:**

1. **Rushi James Macwan**
2. **Poorn Mehta**

# Repository Overview

This repository is fully owned by **Rushi James Macwan** and **Poorn Mehta**. All content on this repository is solely the work of **Rushi James Macwan** and **Poorn Mehta**. However, all external support and guidance taken in completing the work available on this repository has been clearly cited and credited wherever necessary as per the course guidelines.

For references, please visit the References.pdf file available in the main directory which contains an exhaustive list of all the external resources that were utilized and resourceful in completing this project.

# Installation Instructions

This project involves the use of the following elements:

1.	Raspberry Pi 3B setup
2.	DHT22 sensor library installation
3.	Python development libraries including MatPlotLib
4.	Qt and PyQt Installation
5.	MySQL Database Setup

The explanation below dives deep into setting up the Raspberry Pi 3B to run each of the above elements in a gradual manner. Please, go through the below points for a detailed explanation:

**Raspberry Pi 3B setup – installation of Raspbian Buster OS & VNC:**

•	The first step to begin with this project is to install the Raspbian Buster OS on the Raspberry Pi 3B. To do so, we must first download the “Raspbian Buster with desktop and recommended software” OS zipped image file on the host machine (e.g. a dedicated Windows/Mac computer). Link for downloading: https://www.raspberrypi.org/downloads/raspbian/

•	The second step is to unzip the file and use a software that can flash the image file to an SD card (that is already formatted). The software required to do this task is available here: https://www.balena.io/etcher/ 

•	The third step is to download the “balenaEtcher” software, load the image file and flash the image file to the SD card. Once that is done, we simply need to load the SD card into the Pi and attach the peripherals (i.e. an HDMI screen and a USB keyboard & mouse).

•	The fourth step is to set up the Pi by entering a username and password to login every time.

•	An fifth step here is to install the VNC server on the raspberry Pi – but is not explained thoroughly here but the explanation for setting it up can be found here - https://www.raspberrypi.org/documentation/remote-access/vnc/ 

•	The final step is to update the Pi with the recent distributions of the Raspbian Buster OS and the same can be done by running the following commands on the terminal:

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer

**DHT22 sensor library installation:**

•	To install the DHT22 sensor library, please refer to the link: https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ 

•	The first step in this section is to set up the python3 and pip tools so that the sensor can be run through a python script while the pip tool is a packet management system that installs and manages python packages for the project. Please, run the below commands:

sudo apt-get install python3-dev python3-pip

sudo python3 -m pip install --upgrade pip setuptools wheel

sudo pip3 install Adafruit_DHT

Python development & libraries:

•	Since we already installed python3 and pip tools in the previous section, here, we will install other important python libraries that can come handy. Please, execute the below commands so that the libraries are installed:

sudo pip3 install Requests

sudo pip3 install Pillow

sudo pip3 install beautifulsoup4

sudo pip3 install Twisted

sudo pip3 install NumPy

sudo pip3 install SciPy

sudo pip3 install SymPy

sudo pip3 install matplotlib

**Qt & PyQt Installation:**

•	To install the Qt and PyQt libraries, please run the below commands on the Pi CLI:

sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools

sudo apt-get install qttools5-dev-tools

sudo apt-get install python3-tk

Running these commands will install the Qt and PyQt tools on the Pi. Also, the third command will install the Tkinter python application for GUI development natively on the Pi.

**MySQL Database:**

•	To set up the MySQL database for quick storage and acquisition of the voluminous data, we use the MySQL database tool. The first step to use the MySQL database would be to create a database on the target before the Python script is actually run. Please, follow the below commands to set up the MySQL database on the Pi:

sudo apt-get install python-mysqldb

sudo apt-get install mariadb-server

•	Once the above commands are successfully run, the next step would be to secure the MySQL server using the below command:

sudo mysql_secure_installation

Please note, for the above command, the user should answer ‘Y’ to all the questions and a password will be required to be set up for the MySQL server.

•	The next step is to create a MySQL database on the Pi and to do that, please run the below commands on the CLI (terminal):

sudo mysql –u root –p	# user will be prompted to enter the password

CREATE DATABASE <name of the database you want to create>;

CREATE USER ‘root’@’localhost’ IDENTIFIED BY ‘root’;

GRANT ALL PRIVILEGES ON <database name>.* TO ‘root’@’localhost’;

FLUSH PRIVILEGES;

The resource for the above commands can be found here - https://pimylifeup.com/raspberry-pi-mysql/

•	The last step under this section then would be to run the main.py script that will by itself modify the MySQL database tables as required for data storage and acquisition.

# Project Work

For the project work, the breakup of the content was made into the following segments that involved different design and development goals:

1.	Interfacing of DHT22 with the Pi
2.	Design and integration of Matplotlib algorithm to create appropriate graphs
3.	Design and integration of QT GUI
4.	Design and integration of the MySQL database
5.	Addition of required/additional features to the project
6.	Code commenting & Integration
7.	Integrated testing
8.	GitHub and documentation management

**Interfacing of DHT22 with the Pi:**

•	This task was performed as a team by **both the contributors** in the team. Initially, the design and development of this segment was done individually but it was later merged into one working piece.

**Design and integration of the Matplotlib algorithm:**

•	This task was performed as a team by **both the contributors** in the team. The Matplotlib tool was explored on both ends and was later brought into one piece.

**Design and integration of the QT GUI:**

•	This task was performed individually by **Poorn Mehta** and was later merged with the project.

**Design and integration of the MySQL database:**

•	This task was performed individually by **Rushi Macwan** and was later merged with the project.

**Addition of required/additional features to the Project:**

•	This task was performed as a team by **both the contributors** in the team. However, the contribution breakup was also dependent on the above contributions.

**Code Commenting & Integration:**

•	This task was performed individually by **Poorn Mehta** and was later merged with the project.

**Integrated testing:**

•	This task was performed as a team by **both the contributors** in the team. However, the contribution breakup was also dependent on the above contributions.

**GitHub documentation management:**

•	This task was performed individually by **Rushi Macwan** and was later merged with the project.

# Project Additions

As part of an extended effort for this project, the following additions were made to the project requirements:

1.	The user has the ability to modify the rate at which the DHT22 sensor is run. For example, in the project requirement, the sensor is required to run with a period of 15 seconds. As part of the additional feature, the user can actually change the period to a different value (e.g. 5 seconds).

2.	The user has the ability to change the upper limit of the number of data samples acquired from the DHT22 sensor after which the UI would promptly terminate its execution – as per the project requirement.

3.	An extended feature has been added that produces a graph of the last 10 data samples that are available in the MySQL database. However, in addition to the requirement, the graph would still display 10 data samples even though the database table may contain less than 10 data samples. In such cases, the algorithm will append the remaining unavailable data samples with a 0 value in the graph.

4.	An extra credit feature of conversion from degrees C to degree F and vice-versa has been added to the algorithm for a more responsive and interactive UI.

5.	The status line on the UI provides an interactive feedback to the user. For example, keeping in mind the limitations of the DHT22 sensor, if the user sends multiple requests for an instantaneous data sample (i.e. temperature and humidity) to the sensor, the UI status line would report the error since the sensor can collect data samples at the highest rate of only one sample per every 2 seconds.
