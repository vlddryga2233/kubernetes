#!/usr/bin/python3
import subprocess
import cgi
print ("Content-Type: text/html")
print()

output=subprocess.getoutput("/usr/games/fortune")
print(output)
