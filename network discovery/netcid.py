from scapy.all import ARP, Ether, srp
def network_discover(ip_range):
	arp=ARP(pdst=ip_range)
	ether=Ether(dst="ff:ff:ff:ff:ff:ff")
	packet=ether/arp
	result=srp(packet, timeout=2, verbose=False)[0]
	devices=[]
	for sent, received in result:
		devices.append({'IP': received.psrc, 'MAC':received.hwsrc})
	if devices:
		print("Discovered Devices:")
		print("-"*40)
		print(f"{'IP Address':<20}{'MAC Address':<20}")
		print("-"*40)
		for device in devices:
			print(f"{device['IP']:<20}{device['MAC']:<20}")
	else:
		print("No devices found")
ip_range="192.168.0.0/24"

network_discover(ip_range)
