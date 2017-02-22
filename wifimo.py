import os
import subprocess

# Linux command to execute to get wlan0 bytes for bandwidth

proc=subprocess.Popen("ifconfig wlan0 |grep bytes | cut -d\":\" -f2 |cut -d\" \" -f1", shell=True, stdout=subprocess.PIPE, )
output=proc.communicate()[0]

print output
