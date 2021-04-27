#!/usr/bin/env python
# Create the script to generate a cluster with separate number of cores 

import sys
import re

architecture = 'silvermont'
frequency = 'frequency[] = 2,1'
l1_size = 'cache_size[] = 64,16'

vdd = 0.8
window_size = 'window_size[] = 192,64'
lq_size = 'outstanding_loads[] = 32,8'
sq_size = 'outstanding_stores[] = 32,8'
rs_entries = 'rs_entries[] = 64,16'
l2_size = 256
shared_cores = 2
associativity = 4

with open('/home/anish/sniper-7.2/config/' + sys.argv[1], 'w') as f:
    f.write('#include ' + architecture + '\n\n')
    f.write('[perf_model/core]\n')
    f.write(frequency + '\n')
    f.write('type = rob\n\n')
    f.write('[perf_model/core/interval_timer]\n')
    f.write(window_size + '\n\n')
    f.write('[perf_model/core/rob_timer]\n')
    f.write('in_order = false\n')
    f.write('issue_contention = true\n')
    f.write('mlp_histogram = false\n')  
    f.write('issue_memops_at_issue = true\n')
    f.write('store_to_load_forwarding = true\n') 
    f.write('address_disambiguation = true\n')
    f.write('rob_repartition = true\n')
    f.write('commit_width = 256\n')
    f.write(lq_size + '\n')
    f.write(sq_size + '\n')
    f.write(rs_entries + '\n\n')
    f.write('[perf_model/l1_icache]\n')
    f.write(l1_size + '\n')
    f.write('associativity = ' + str(associativity) + '\n\n')
    f.write('[perf_model/l1_dcache]\n')
    f.write(l1_size + '\n')
    f.write('associativity = ' + str(associativity) + '\n\n')
    f.write('[perf_model/l2_cache]\n')
    f.write('cache_size = ' + str(l2_size) + '\n')
    f.write('shared_cores = ' + str(shared_cores) + '\n\n')
    f.write('[power]\n')
    f.write('vdd = ' + str(vdd))
