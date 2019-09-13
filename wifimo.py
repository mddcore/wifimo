
import os
import subprocess
from datetime import datetime

# Date and time  format

today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Linux command to execute to get wlan0 bytes for bandwidth

### Incoming traffic
proc=subprocess.Popen("ifconfig wlan0 |grep bytes | cut -d\":\" -f2 |cut -d\" \" -f1", shell=True, stdout=subprocess.PIPE, )
incoming=proc.communicate()[0]

### Outgoing traffic

proc=subprocess.Popen("ifconfig wlan0 |grep bytes | cut -d\":\" -f3 |cut -d\" \" -f1", shell=True, stdout=subprocess.PIPE, )
outgoing=proc.communicate()[0]


print 'Date:', today, 'Incoming:', incoming, 'Outgoing:', outgoing
