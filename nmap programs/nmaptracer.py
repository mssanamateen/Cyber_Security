import nmap
nm=nmap.PortScanner()
nm.scan('192.168.0.103','22-443')
print(nm.command_line())
print(nm.scaninfo())
print(nm.all_hosts())
print(nm['192.168.0.103'].hostname())


for host in nm.all_hosts():
	print('****************************')
	print('Host: %s (%s)' %(host, nm[host].hostname()))
	print('State:%s' %nm[host].state())
	for prot in nm[host].all_protocols():
		print('---------')
		print('protocol: %s' %prot)
		
		lport=list(nm[host][prot].keys())
		
		lport.sort()
		for port in lport:
			print('port: %s\t state:%s' %(port, nm[host][prot][port]['state']))