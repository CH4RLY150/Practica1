import sys
import subprocess
import logging

def delete(orden, numero):
	for j in range(int(numero)):
		if numero == "1":
			nombre = orden
		else:
			nombre = orden + str(j)
		subprocess.run(["lxc", "delete", nombre])

