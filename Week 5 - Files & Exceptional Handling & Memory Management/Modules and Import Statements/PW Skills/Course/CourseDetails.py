# our objective is to call payment function in this file and vice versa
# we are to do import of one module to other module
# packages -> These are directory or folders which can contains many packages and files
# modules -> The file is called module

import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# the above statement creates a pycache in Payment package, Now this directory is aware of other modules and package
from Payment import PaymentDetails
def course() :
    print("This is my course")
PaymentDetails.payment()