import sys
import subprocess


def pause(orden, numero):
	for j in range(int(numero)):
		if numero == "1":
			nombre = orden
		else:
			nombre = orden + str(j)
		subprocess.run(["lxc", "stop", nombre, "--force"])

