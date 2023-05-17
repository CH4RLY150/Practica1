import sys
import subprocess
import logging

IP_lb = ".10"
lxdbr0 = "lxdbr0"
lxdbr1 = "lxdbr1"
lxdbr = "lxdbr"
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1] 
	parametros = sys.argv[2]
	ip1 = sys.argv[3]
		# Asignamos cada servidor al bridge lxdbr0 y asignamos su dirección IPv4:
	if orden == "lb":
		n_lb = sys.argv[4] 
		for j in range(int(n_lb)):
			nombre = orden + str(j)
			for i in range(int(parametros)):
				subprocess.run(["lxc", "network", "attach", lxdbr+str(i), nombre, "eth"+str(i)])
				subprocess.run(["lxc", "config", "device", "set", nombre, "eth"+str(i), "ipv4.address", ip1 + str(i) + IP_lb])
	elif orden == "vm":
		for i in range(int(parametros)):
			nombre = orden + str(i)
			m = i+1
			subprocess.run(["lxc", "network", "attach", lxdbr0, nombre, "eth0"])
			subprocess.run(["lxc", "config", "device", "set", nombre, "eth0", "ipv4.address", ip1 + str(m)])
	elif orden == "c1":
		for i in range(int(parametros)):
			nombre = orden + str(i)
			m = i+1
			subprocess.run(["lxc", "network", "attach", lxdbr1, nombre, "eth0"])
			subprocess.run(["lxc", "config", "device", "set", nombre, "eth0", "ipv4.address", ip1 + str(m)])
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")
