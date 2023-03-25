import socket
import termcolor

def scan(target, ports):
  for port in range(1, ports):
  print("\n" + "Starting to scan " + str(target))
    scan_port(target, port)

def port_scan(ipaddress, port)
  try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print("[+] PORT OPEN " + str(port))
    sock.close()
  except:
    pass

targets = input("[*] Enter targets to scan (split them by a ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
  print(termcolor.colored(("[*] Scanning multiple targets"), 'light_green'))
  for ip_addr in targets.split(','):
    scan(ip_addr.strip(' '), ports)
else:
  scan(targets, ports)