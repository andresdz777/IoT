#Gracias al usuario ctrlsam por el codigo


import socket
import struct

input_file = open("austria.csv", "r")
output_file = open("austria.ips", "w")

for line in input_file:
  to_ip, from_ip, _, _ = line.replace("\"", "").split(",")

  to_ip = int(to_ip)
  from_ip = int(from_ip)

  for ip_index in range(to_ip, from_ip):
    ip = socket.inet_ntoa(struct.pack("!L", ip_index))
    output_file.write(ip + "\n")

input_file.close()
output_file.close()