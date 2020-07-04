# input from Keyboard without Enter

import readchar
import sys
 
while 1:
  kb = readchar.readchar()
  sys.stdout.write(kb)
  if kb == 'q':
    print("")
    break
