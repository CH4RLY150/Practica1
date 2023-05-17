import sys
import subprocess
import logging
import time

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1] 
	parametros = sys.argv[2]
	for i in range(int(parametros)):
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
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")
