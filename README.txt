HoGG_It 1.0, Written by XxTheSunxX. Updated: July 10th 2024

Terms and Conditions:

For educational use only. Writer is not responsible for any physical, digital, or legal liability/damage caused by this script.
Use at your own discretion.

Use cases for this script:

This script will attempt to change its mac address (layer 2) and connect rapidly, in order to use up all DHCP lease IP addresses, effectively creating a denial of service attack on any networking using DHCP for their dynamic addressing. This will prevent any new device who has not received a DHCP lease from the DHCP server unable to connect.

Functions of this script:

Connect to the network; request a DHCP lease which is matched with its mac address; disconnect from the network by setting the interface down; change its mac address to a random mac address; connect again which receives a new IP address (layer 3) from the DHCP server; and loop through these steps again.

Requirements:

This script requires the following modules to be available on your system before running which can be installed with PIP or are part of the Python standard library:

socket
sys
time
getmac
generate_mac
subprocess
os
colorama

