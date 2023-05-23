import sys
import subprocess

def lista(orden, numero):
	for j in range(int(numero)):
		if numero == "1":
			nombre = orden
		else:
			nombre = orden + str(j)
		subprocess.run(["lxc", "start", nombre])
		subprocess.run(["lxc", "exec", nombre, "ipaddr"])

