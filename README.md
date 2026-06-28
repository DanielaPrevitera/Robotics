# Robotics

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


### Livox SDK and ROS 2 Driver Installation
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
