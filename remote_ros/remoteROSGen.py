#!/usr/bin/python3
import socket
import argparse
import os
import re

def get_ip_address(input_ip : str):
    if (input_ip == ""):
        print("Local IP not provided, using local IP for internet")
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    return input_ip

def format_host_name(input_host_name = None):
    if (input_host_name is None):
        return socket.gethostname() + ".local"

    ret = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", input_host_name)

    if (ret):
        # Not a host name but IP
        return input_host_name

    if (input_host_name.endswith(".local")):
        return input_host_name
    else:
        return input_host_name + ".local"

parser = argparse.ArgumentParser(description='Generate remoteROS config file for client-host ros')
parser.add_argument('--host_addr', dest='host_addr',
                    help='Set address to ROSCORE host, hostname or IP [Client mode]')
parser.add_argument('--local_ip', dest='local_ip', nargs='?', const="",
                    help='Use IP mode for local addresses, [Optional, use specific IP address for local machine]')
args = parser.parse_args()

local_addr = format_host_name()

output_str = ""

if (args.local_ip is None):
    print("Using hostname mode")
    output_str += "export ROS_HOSTNAME={}\n".format(local_addr)
else:
    print("Using IP mode")
    local_addr = get_ip_address(args.local_ip)
    output_str += "export ROS_IP={}\n".format(local_addr)

if (args.host_addr is None):
    print("Generating remoteROS shell script for host")
    target_addr = local_addr
else:
    print("Generating remoteROS shell script for client")
    target_addr = format_host_name(args.host_addr)

output_str += "export ROS_MASTER_URI=http://{}:11311\n".format(target_addr)

print("")
print("Local machine address: {}".format(local_addr))
print(" Host machine address: {}".format(target_addr))
print("")

ping_resp = os.system("ping -c 1 " + target_addr + " > /dev/null 2>&1")

if (ping_resp != 0):
    print("[WARNING] ping to {} failed. Host machine unreachable.".format(target_addr))

local_addr_isIP = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", local_addr) != None
target_addr_isIP = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", target_addr) != None

if (local_addr_isIP != target_addr_isIP):
    print("[WARNING] mixing Hostname and IP format for client and host machine")

print("")

with open("./remoteROS", "w") as output:
    output.write(output_str)

print("Config file written to \"./remoteROS\"")
print("source the file to enable ros client-host interaction")
