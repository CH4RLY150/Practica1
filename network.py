import sys
import subprocess
import logging

lxdbr = "lxdbr"
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1] 
	ip_inc = sys.argv[2]
	ip_end = sys.argv[3]
	for i in range(int(orden)):
		nombre = lxdbr + str(i)
		ip = ip_inc + str(i) + ip_end
		# creación de los bridges
		if i == 0:
			print("configurando "+lxdbr+str(i))
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.nat", "true"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.address", ip])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.nat", "false"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.address", "none"])
		else:
			print("creando y configurando "+lxdbr+str(i))
			subprocess.run(["lxc", "network", "create", nombre])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.nat", "true"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv4.address", ip])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.nat", "false"])
			subprocess.run(["lxc", "network", "set", nombre, "ipv6.address", "none"])	
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")
