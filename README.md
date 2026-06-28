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

### Installation Verification

The installation can be verified by running two example ROS 2 nodes. In the first terminal, the `talker` node is started:

```bash
ros2 run demo_nodes_cpp talker
```

In a second terminal, the `listener` node is started:

```bash
ros2 run demo_nodes_py listener
```

If the listener receives the messages published by the talker, the installation has been completed successfully.

### Summary

In this project, **ROS 2 Humble** was installed on **Ubuntu 22.04** using the official Debian packages. The installation procedure consisted of configuring the system locale, enabling the required Ubuntu repositories, adding the official ROS 2 repository and GPG key, and installing the `ros-humble-desktop` package. Finally, the ROS 2 environment was configured by sourcing the setup file, and the installation was tested using the standard `talker` and `listener` example nodes.
