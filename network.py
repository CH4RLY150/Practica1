import sys
import subprocess

def network(orden, ip0, ip1, lxdbr):
	for i in range(int(orden)):
		nombre = lxdbr + str(i)
		ip = ip0 + str(i) + ip1
		# creación de los bridges
		if i == 0:
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.nat", "true"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.address", ip])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.nat", "false"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.address", "none"])
		else:
			subprocess.run(["lxc", "network", "create", nombre])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.nat", "true"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.address", ip])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.nat", "false"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.address", "none"])
