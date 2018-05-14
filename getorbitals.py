#!/hpc/applications/anaconda/2/bin/python2

import sys
import os
import collections
import itertools

inputf = str(sys.argv[1])

n = -1
with open(inputf, 'r') as file:
   before = collections.deque(maxlen=3)
   for line in file:
       if 'Eigenvalues' in line:
           sys.stdout.writelines(before)
           sys.stdout.write(line)
       before.append(line)
       if 'Ni' in line:
          print(line)
       if 'Fe' in line:
          print(line)
       if '14D' in line:
          print(line)
       if '15D' in line:
          print(line)
