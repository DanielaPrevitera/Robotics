# Robotics
<img width="508" height="700" alt="image" src="https://github.com/user-attachments/assets/21f78b2d-8623-4143-8b83-7e34a4fc8bf4" />
<img width="861" height="397" alt="image" src="https://github.com/user-attachments/assets/cabdf714-59dd-433d-8dab-d1f7e31d4f75" />


## ROS 2 Humble Installation on Ubuntu

The installation of **ROS 2 Humble** on Ubuntu can be performed using Debian packages through the `apt` package manager. This is the recommended installation method for Ubuntu systems, especially when using **Ubuntu 22.04 Jammy**, which is the main supported distribution for ROS 2 Humble. 

### System Locale Configuration

Before installing ROS 2, the system locale must be configured to use **UTF-8**. This ensures compatibility with ROS 2 tools and prevents possible encoding issues during execution.

```bash
locale

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale
```

### Enabling the Ubuntu Universe Repository

Some ROS 2 dependencies are available through the Ubuntu **Universe** repository. Therefore, this repository must be enabled before proceeding with the installation.

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

### Adding the ROS 2 Repository

After enabling the required Ubuntu repository, the official ROS 2 GPG key must be added. This key is used to verify the authenticity of the ROS 2 packages downloaded from the repository.

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
-o /usr/share/keyrings/ros-archive-keyring.gpg
```

Then, the ROS 2 repository is added to the system sources list:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" \
| sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Installing ROS 2 Humble

Once the repository has been added, the package list must be updated:

```bash
sudo apt update
sudo apt upgrade
```

The complete desktop version of ROS 2 Humble can then be installed with the following command:

```bash
sudo apt install ros-humble-desktop
```

This installation includes the ROS 2 core libraries, command-line tools, graphical tools such as **RViz**, and example packages. For development purposes, it is also useful to install the ROS development tools:

```bash
sudo apt install ros-dev-tools
```

### Environment Setup

After the installation, the ROS 2 environment must be sourced in order to use ROS commands from the terminal:

```bash
source /opt/ros/humble/setup.bash
```

To avoid executing this command manually every time a new terminal is opened, it can be added to the `.bashrc` file:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
## ROS 2 Workspace Setup

It is necessary to set up the **ROS 2 workspace** by referring to the official ROS 2 workspace creation guide:

```text
https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html
```

Although the guide refers to ROS 2 Foxy, the same workspace structure can be used for ROS 2 Humble, with the appropriate environment setup commands adapted to the installed ROS 2 distribution.

### 1. Installing the Required Dependencies

Before creating the workspace, it is important to make sure that all the required dependencies are installed. In particular, `colcon` is required to build ROS 2 workspaces and may not be installed by default. Apparently, even compiling needs its own ceremony.

The following command installs the common `colcon` extensions:

```bash
sudo apt install python3-colcon-common-extensions
```

Further information about `colcon` can be found in the official ROS 2 tutorial:

```text
https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html
```

### 2. Installing GTSAM

The project also requires **GTSAM**. To install it, the official GTSAM repository must first be added.

#### 2.1 Adding the GTSAM Repository

```bash
sudo add-apt-repository ppa:borglab/gtsam-release-4.1
```

#### 2.2 Installing GTSAM

After adding the repository, the package list must be updated and the required GTSAM packages can be installed:

```bash
sudo apt update
sudo apt install libgtsam-dev libgtsam-unstable-dev
```

### 3. Creating the ROS 2 Workspace

The ROS 2 workspace is then created using the standard workspace structure. The `src` folder is used to store the source code of the ROS 2 packages.

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```

### 4. Cloning the GitHub Repository

The project repository is cloned inside the `src` directory of the workspace. This step is also required by the project repository instructions.

```bash
git clone https://github.com/rajvishnu07/lio_sam_mid360 src/LIO_SAM_MID360
```

### 5. Building and Sourcing the Workspace

Once the repository has been cloned, the workspace can be built using `colcon`:

```bash
colcon build --symlink-install
```

After the build process is completed, the workspace must be sourced:

```bash
source install/setup.bash
```

At this point, the build is completed and the ROS 2 workspace is ready to be used.

## LiDAR Sensor Connection and Setup

To use the **Livox MID-360 LiDAR sensor**, the Ethernet connection between the computer and the sensor must be correctly configured. This step is necessary before launching the LiDAR drivers or using visualization tools such as Livox Viewer 2. Because naturally, even a sensor needs a networking ritual before doing the one job it was built for.

### 1. Installing Network Tools

First, the required network tools must be installed:

```bash
sudo apt install net-tools
```

These tools provide commands such as `ifconfig`, which can be used to configure the Ethernet interface manually.

### 2. Identifying the Ethernet Interface

Before assigning an IP address, it is necessary to identify the Ethernet interface used to connect the LiDAR sensor. This can be done with the following command:

```bash
lshw -class network
```

The command displays information about the available network interfaces. The required value is the **logical name** of the Ethernet interface connected to the sensor.
The actual name can be different depending on the computer.

### 3. Configuring the Ethernet IP Address

Once the logical name of the Ethernet interface has been identified, a static IP address must be assigned to it. The LiDAR sensor works on the `192.168.1.x` network, so the computer interface can be configured with the following command:

```bash
sudo ifconfig <logical_name> 192.168.1.50
```

For example, if the Ethernet interface is called `enp3s0`, the command becomes:

```bash
sudo ifconfig enp3s0 192.168.1.50
```

This assigns the IP address `192.168.1.50` to the Ethernet port used to communicate with the LiDAR sensor.

### 4. Downloading Livox Viewer 2

To verify the connection and visualize the LiDAR data, **Livox Viewer 2** can be used. The software can be downloaded from the official Livox MID-360 download page:

```text
https://www.livoxtech.com/mid-360/downloads
```

The Linux version of **Livox Viewer 2** must be downloaded and extracted into a folder.

### 5. Running Livox Viewer 2

After extracting the package, the viewer can be launched from the terminal by moving into the extracted folder and running the startup script:

```bash
./livox_viewer_2.sh
```

If the script name is different, the command must be adapted accordingly.

For example:

```bash
./<viewer_script_name>.sh
```

Once Livox Viewer 2 is launched, it can be used to check whether the LiDAR sensor is correctly detected and whether point cloud data are being received.

### 6. Useful Links

The following repositories and documentation pages are useful for the setup of the MID-360 LiDAR sensor and its integration with ROS 2:

```text
https://github.com/Livox-SDK/livox_ros_driver2
```

```text
https://github.com/rajvishnu07/lio_sam_mid360?tab=readme-ov-file#readme
```

```text
https://github.com/Livox-SDK/Livox-SDK2/blob/master/README.md
```

The first repository contains the **Livox ROS Driver 2**, which is required to publish Livox LiDAR data in ROS 2. The second repository contains the **LIO-SAM MID-360** project used in this setup. The third link provides information about the **Livox SDK2**, which is required for communication with Livox sensors.



## Livox SDK and ROS 2 Driver Installation
To properly use the MID360 sensor with ROS 2 Humble, you need to install the core Livox SDK2 and then build the official ROS 2 driver.

### 1. Installing the Livox SDK2
First, download and compile the official Livox-SDK2 from its source repository. This provides the fundamental libraries required to communicate with the sensor.

The following commands will clone the repository, prepare the build environment, compile using available CPU cores, and install the libraries to your system:

```Bash
cd ~
git clone https://github.com/Livox-SDK/Livox-SDK2.git
cd Livox-SDK2
mkdir build && cd build
cmake .. && make -j
sudo make install
```
### 2. Downloading the Livox ROS 2 Driver
Next, prepare a dedicated ROS 2 workspace and clone the livox_ros_driver2 repository into the src folder.

```Bash
mkdir -p ~/ws_livox/src
cd ~/ws_livox/src
git clone https://github.com/Livox-SDK/livox_ros_driver2.git
cd ~/ws_livox/src/livox_ros_driver2
```
### 3. Configuring the Device IP
Before building the ROS 2 package, it is necessary to configure the network settings. If you build the package first, the default configuration file will be copied into the install folder, and subsequent changes to the src folder will be ignored.

Open the MID360_config.json file using a text editor like nano:

```Bash
nano ~/ws_livox/src/livox_ros_driver2/config/MID360_config.json
```
Inside the file, make the following adjustments:

Change all the host IP addresses to match the static IP you previously set up on your machine.

Change the device IP to 192.168.1.106.

Note: Be very careful not to delete any quotation marks (") or commas (,) while editing, as this will break the JSON formatting and prevent the driver from launching.

### 4. Building the ROS 2 Package
Once the configuration is correctly set, you can build the driver package. The Livox driver provides a custom shell script to handle the build process.

Make sure to source your ROS 2 Humble installation first:

```Bash
source /opt/ros/humble/setup.bash
./build.sh humble
```
### 5. Launching the repository
In one terminal, launch the livox driver:
```Bash
cd ~/ws_livox
source install/setup.bash
ros2 launch livox_ros_driver2 rviz_MID360_launch.py
```
In another terminal, launch the repository:
```Bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch lio_sam_mid360 run.launch.py
```

## IMU Noise Analysis

This section explains how to record the LiDAR IMU data, export it from a ROS 2 bag, and compute the noise statistics required for the LiDAR configuration file.

The goal of this procedure is to estimate the IMU noise by analyzing the recorded acceleration and angular velocity data.

---

### 1. Record the IMU Data

To analyze the IMU noise, record the LiDAR IMU topic for about two minutes.

Run the following command:

```bash
timeout 120s ros2 bag record /livox/imu
```

This command records the `/livox/imu` topic for `120` seconds.

After the recording is completed, a ROS 2 bag folder will be generated.

---

### 2. Export the IMU Data from the ROS 2 Bag

After recording the data, open a terminal and enter the folder containing the generated ROS 2 bag.

Then, copy the following script inside the bag folder:

```bash
export_imu_from_bag.py
```

Once the script is inside the bag folder, run:

```bash
python3 export_imu_from_bag.py imu_noise_bag /livox/imu imu.csv
```

Where:

- `imu_noise_bag` is the name of the recorded ROS 2 bag.
- `/livox/imu` is the IMU topic to be extracted.
- `imu.csv` is the output CSV file containing the exported IMU data.

After running this command, the IMU data will be exported into a CSV file named:

```bash
imu.csv
```

---

### 3. Plot the Recorded IMU Noise

To visualize the recorded IMU noise, run:

```bash
python3 plot_imu.py
```

This script plots the IMU measurements, allowing you to inspect the noise behavior graphically.

---

### 4. Compute IMU Noise Statistics

To compute the mean and variance of the recorded IMU noise, run:

```bash
python3 stats_imu.py
```

This script calculates the statistical values of the recorded IMU data.

The most important values are:

- Mean
- Variance

These values can then be used to tune the LiDAR configuration file.

---

### 5. Update the LiDAR Parameters

After computing the IMU noise statistics, insert the obtained values into the LiDAR parameter file:

```bash
params.yaml
```

The computed mean and variance can be used to configure the IMU noise parameters required by the LiDAR algorithm.

This improves the consistency of the IMU model used by the system.

## Saving and Visualizing a Map with RViz2

This section explains how to save a map generated in RViz2 using `LIO-SAM MID360` and how to visualize it again later.

> **Note**
>
> Replace `/home/peppo` with your actual home directory path.
>
> Example:
>
> ```bash
> /home/<your_username>
> ```

---

### 1. Save the Generated Map

Before running any ROS 2 command, source both the ROS 2 installation and the workspace:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
source ~/ros2_ws/install/setup.bash
```

Optionally, create a directory where the generated map will be saved:

```bash
mkdir -p /home/peppo/mappe/mappa_test
```

You can change the directory name depending on the map you want to save.

Example:

```bash
mkdir -p /home/peppo/mappe/mappa_finale
```

Then, save the map by calling the `/lio_sam/save_map` service:

```bash
ros2 service call /lio_sam/save_map lio_sam_mid360/srv/SaveMap "{resolution: 0.2, destination: /home/peppo/mappe/mappa_test}"
```

Where:

- `resolution: 0.2` defines the resolution of the saved map.
- `destination` defines the folder where the map will be saved.

After running the command, the map generated in RViz2 will be saved in the selected directory.

The saved map should contain the following file:

```bash
GlobalMap.pcd
```

---

### Important: RViz2 Configuration File

Before opening the saved map, make sure that the RViz2 configuration file:

```bash
lab_map.rviz
```

is placed inside the following directory:

```bash
~/ros2_ws/src/LIO_SAM_MID360
```

If this file is available, RViz2 can be opened automatically with the correct configuration.

If this file is not available, RViz2 must be configured manually by adding the required displays and topics.

---

### Open the Map Automatically

Use this method if the `lab_map.rviz` configuration file is available.

#### Terminal 1: Publish the Saved Point Cloud

First, source the ROS 2 environment and the workspace:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
source ~/ros2_ws/install/setup.bash
```

Then publish the saved `.pcd` map file:

```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args \
    -p file_name:=/home/peppo/mappe/mappa_test/GlobalMap.pcd \
    -p publish_rate:=1.0
```

Replace the `file_name` path with the actual path where your `GlobalMap.pcd` file is stored.

Example:

```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args \
    -p file_name:=/home/peppo/mappe/mappa_finale/GlobalMap.pcd \
    -p publish_rate:=1.0
```

This command publishes the point cloud on the following topic:

```bash
/cloud_pcd
```

You can verify that the topic exists with:

```bash
ros2 topic list | grep cloud
```

#### Terminal 2: Open RViz2 with the Configuration File

Run:

```bash
rviz2 -d /home/peppo/ros2_ws/src/LIO_SAM_MID360/lab_map.rviz
```

RViz2 will open with the correct configuration already loaded.

---

### Open the Map Manually

Use this method only if the `lab_map.rviz` configuration file is not available.

#### Terminal 1: Publish the Saved Point Cloud

First, source the ROS 2 environment and the workspace:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
source ~/ros2_ws/install/setup.bash
```

Then publish the saved `.pcd` map file:

```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args \
    -p file_name:=/home/peppo/mappe/mappa_test/GlobalMap.pcd \
    -p publish_rate:=1.0
```

Or, for another saved map:

```bash
ros2 run pcl_ros pcd_to_pointcloud --ros-args \
    -p file_name:=/home/peppo/mappe/mappa_test2/GlobalMap.pcd \
    -p publish_rate:=1.0
```

The map will be published on:

```bash
/cloud_pcd
```

You can check that the topic is available with:

```bash
ros2 topic list | grep cloud
```

#### Terminal 2: Publish a Static Transform

Run the following command:

```bash
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 map base_link
```

This publishes a static transform between the `map` frame and the `base_link` frame.

This step is useful if RViz2 has frame-related issues when displaying the map.

#### Terminal 3: Open and Configure RViz2

Start RViz2:

```bash
rviz2
```

Inside RViz2:

1. Click **Add**.
2. Select **PointCloud2**.
3. Set the topic to:

```bash
/cloud_pcd
```

The saved map should now be visible in RViz2.


## Integration on the Mobile Robot

After completing the LiDAR setup and verifying its connection, the sensor was mounted on a mobile robot, called **Robovolc**. The robot was accessed remotely through an **SSH connection**, allowing the user to control and configure the system from another computer without directly operating on the robot onboard machine. Because apparently even robots now get remote work privileges.

### SSH Connection to the Robot

The connection to Robovolc was established using SSH. This allows a terminal session to be opened directly on the robot computer, making it possible to launch ROS 2 nodes, configure the workspace, and run control commands remotely.

A typical SSH command has the following structure:

```bash
ssh username@robot_ip_address
```

where `username` is the robot user account and `robot_ip_address` is the IP address assigned to Robovolc on the network.

### Keyboard Teleoperation

To manually control the robot, the ROS 2 package `teleop_twist_keyboard` was used. This package allows velocity commands to be generated from the keyboard. These commands are published as `geometry_msgs/Twist` messages, which are commonly used in ROS 2 to control mobile robots.

The command used was:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/key_vel
```

### Topic Remapping

By default, `teleop_twist_keyboard` publishes velocity commands on the topic:

```text
/cmd_vel
```

However, Robovolc expects velocity commands on a different topic:

```text
/key_vel
```

For this reason, a topic remapping was added to the command:

```bash
--ros-args --remap cmd_vel:=/key_vel
```

This remapping changes the output topic of the teleoperation node from `cmd_vel` to `/key_vel`. In this way, the velocity commands generated from the keyboard are sent directly to the topic used by the robot control system.

### Complete Command

The full command used to control Robovolc through the keyboard was:

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/key_vel
```

This command starts the keyboard teleoperation node and redirects its velocity output to the correct robot control topic.

