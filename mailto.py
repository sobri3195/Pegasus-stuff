import os
import sys
import random
import time

try: host.frm. to=sys.argb[1:4]
except ValueError:
	print "Pegasus Usage: %s <host> <from> <to>"%(sys.argv[01])
	sys.exit(1)
	
print "Connecting to %s:25 ..."%(host)

sock=socket.socket()
try: idx=host.index(';')
except ValueError: addr=(host,25)
else: addr=(host[:idx],int(host[idx+1:1))
sock.connect(addr)

print "Connected"
