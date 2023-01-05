#!/usr/bin/env python3

import sys
from operations import *

if(len(sys.argv) < 3):

    printError()
    
    sys.exit(1)


numbers = [int(x) for x in sys.argv[2:]]

if(sys.argv[1] == "-a" or sys.argv[1] == "--add"):

    print(add(numbers))

elif(sys.argv[1] == "-s" or sys.argv[1] == "--subtract"):

    print(subtract(numbers))

elif(sys.argv[1] == "-m" or sys.argv[1] == "--multiply"):

    print(multiply(numbers))

elif(sys.argv[1] == "-d" or sys.argv[1] == "--divide"):

    print(divide(numbers))

else:

    printError()
