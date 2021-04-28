#!/usr/bin/env python
# this is the script to generate 4 different config files

import sys
import re

frequency = [2,1.5,1,0.5]
vdd = [1,0.8,0.7,0.61]
window_size = [192,128,64,64]
q_size = [32,16,8,8]
rs_entries = [64,32,16,16]
l1_size = [64,32,16,16]
l2_size = [1024,512,256,256]
associativity = [8,4,4,4]


for i in range(4):
    filename = 'config_file_'+ str(i) + '.cfg'
    new_config = open('/path/to/config/' + filename, 'w')
    new_config.write('#include silvermont\n\n')
    new_config.write('[perf_model/core]\n')
    new_config.write('frequency = ' + str(frequency[i]))
    new_config.write('\n')
    new_config.write('type = rob\n\n')
    new_config.write('[perf_model/core/interval_timer]\n')
    new_config.write('window_size = ' + str(window_size[i]))
    new_config.write('\n\n')
    new_config.write('[perf_model/core/rob_timer]\n')
    new_config.write('in_order = false\n')
    new_config.write('issue_contention = true\n')
    new_config.write('mlp_histogram = false\n')  
    new_config.write('issue_memops_at_issue = true\n')
    new_config.write('store_to_load_forwarding = true\n') 
    new_config.write('address_disambiguation = true\n')
    new_config.write('rob_repartition = true\n')
    new_config.write('commit_width = 256\n')
    new_config.write('outstanding_loads = ' + str(q_size[i]))
    new_config.write('\n')
    new_config.write('outstanding_stores = ' + str(q_size[i]))
    new_config.write('\n')
    new_config.write('rs_entries = ' + str(rs_entries[i]))
    new_config.write('\n\n')
    new_config.write('[perf_model/l1_icache]\n')
    new_config.write('cache_size = ' + str(l1_size[i]))
    new_config.write('\n')
    new_config.write('associativity = ' + str(associativity[i]))
    new_config.write('\n\n')
    new_config.write('[perf_model/l1_dcache]\n')
    new_config.write('cache_size = ' + str(l1_size[i]))
    new_config.write('\n')
    new_config.write('associativity = ' + str(associativity[i]))
    new_config.write('\n\n')
    new_config.write('[perf_model/l2_cache]\n')
    new_config.write('cache_size = ' + str(l2_size[i]))
    new_config.write('\n')
    new_config.write('shared_cores = 4')
    new_config.write('\n\n')
    new_config.write('[power]\n')
    new_config.write('vdd = ' + str(vdd[i]))
    new_config.close()
