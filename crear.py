import sys
import subprocess

def crear(orden, imagen, parametros):
	print("creando " + parametros + " " + orden)
	for i in range(int(parametros)):
		if parametros == "1":
			nombre = orden
		else:
			nombre = orden + str(i)
		subprocess.run(["lxc", "init", imagen, nombre])

