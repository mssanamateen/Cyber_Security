import  nmap
scann=nmap.PortScanner()
target="192.168.0.103"
options="-sS -sV -O -A -p 22-443"
scann.scan(target, arguments=options)

for host in scann.all_hosts():
	print("host:", host)
	print("state:", scann[host].state())
	for proto in scann[host].all_protocols():
		print("protocol:", proto)
		ports=scann[host][proto].keys()
		for port in ports:
			print("port:", port, "State:", scann[host][proto][port]['state'])