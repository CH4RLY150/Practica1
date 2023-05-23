import sys
import subprocess
import time

def eth(orden, parametros):
	for i in range(int(parametros)):
		if parametros == "1":
			nombre = orden
		else:
			nombre = orden + str(i)
		subprocess.run(["lxc", "start", nombre])
		eth1_in = False
		while not eth1_in:
			time.sleep(3)
			subprocess.run(["lxc", "file", "push", "50-cloud-init.yaml", nombre + "/etc/netplan/50-cloud-init.yaml"])
			time.sleep(2)
			respuesta = subprocess.run(["lxc", "exec", nombre, "--", "cat", "/etc/netplan/50-cloud-init.yaml"], stdout=subprocess.PIPE)
			# respuesta.stdout es la salida del subprocess
			eth1_in = "eth1" in respuesta.stdout.decode("utf-8") # es una condición de si eth1 está en la salida del subprocess
		subprocess.run(["lxc", "stop", nombre])

