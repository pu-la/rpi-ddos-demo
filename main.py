### IMPORTS

import requests
import getopt
import sys

### MAIN
def ddos(ip_addr):
	r = requests.get(ip_addr)

### EXECUTE

argumentList = sys.argv[1:]
options = "hip"
long_options = ["help"]

try:

   arguments, values = getopt.getopt(argumentList, options, long_options)
   for currentArgument, currentValue in arguments:
       if currentArgument in ("-h", "--Help"):
           print ("Please specify an ip address with -ip")            
       elif currentArgument in ("-ip"):
           print ("Displaying file_name:", sys.argv[0])

except getopt.error as err:
    print (str(err))
