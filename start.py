import sys
import subprocess

s = "s"

def start(orden, numero):
	for j in range(int(numero)):
		if numero == "1":
			nombre = orden
		else:
			nombre = orden + str(j)
		subprocess.run(["lxc", "start", nombre])
		if orden == s:
			comando = "lxc exec " + nombre + " bash"
			subprocess.Popen(["xterm", "-fa", "monaco", "-fs", "13", "-bg", "pink", "-fg", "black", "-e", comando])

