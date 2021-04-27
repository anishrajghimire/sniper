#!/usr/bin/env python
# Create the scripts to generate different config files

import sys
import re

frequency = [2,1.5,1,0.5]
vdd = [1,0.8,0.7,0.61]
window_size = [192,128,64,64]
outstanding_loads = [32,16,8,8]
outstanding_stores = [32,16,8,8]
rs_entries = [64,32,16,16]
cache_size = [64,32,16,16]


# config = open("/home/anish/sniper-7.2/config/silvermont.cfg", "r")

for i in range(4):
    filename = 'config_file_'+ str(i) + '.cfg'
    with open('/home/anish/sniper-7.2/config/silvermont.cfg','r+') as f:
        text = f.read()
        fstring1 = 'frequency = 2.4'
        fstring2 = 'frequency = ' + str(frequency[i])
        text = re.sub(fstring1,fstring2,text)

        fstring1 = 'type = interval'
        fstring2 = 'type = rob'
        text = re.sub(fstring1,fstring2,text)

        fstring1 = 'window_size = 32'
        fstring2 = 'window_size = ' + str(window_size[i])
        text = re.sub(fstring1,fstring2,text)

        new_config = open('/home/anish/sniper-7.2/config/' + filename, 'w')
         
        # f.seek(0)
        new_config.write(text)
        new_config.close()
        # f.truncate()

# new_config.write("#include silvermont")
# new_config.close()