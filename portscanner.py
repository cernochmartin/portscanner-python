import socket
from termcolor import cprint

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		cprint("[+] PORT | OPEN | " + str(port), "light_green")
		sock.close()
	except:
		cprint("[-] PORT | CLOSE | " + str(port), "light_red")

targets = input("[*] Enter targets to scan(split them by a ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if ',' in targets:
	print("[*] Scanning multiple targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)
