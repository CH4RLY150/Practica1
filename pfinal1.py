import sys
import subprocess
import logging
import pickle

s = "vm"
lb = "lb"
n_lb = "1"
c = "c1"
n_client = "1"
imagen = "ubuntu2004"
n_bridges = "2"
lxdbr = "lxdbr"
ip0 = "134.3.0.1"
ip1 = "134.3.1.1"
ip_inc = "134.3."
ip_end = ".1/24"
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
# configuramos el lxd
	# sudo usermod -a -G lxd $USER
	# newgrp lxd
subprocess.run(["lxd", "init", "--auto"])

try:
	orden = sys.argv[1] 
	if orden == "create":
		subprocess.run(["lxc", "image", "import", "/mnt/vnx/repo/arso/ubuntu2004.tar.gz", "--alias", imagen])
		try:
			parametros = sys.argv[2]
			#comprobación del argumento parametros
			if int(parametros) <= 5 and int(parametros) > 0:
				print("segundo argumento correcto")
			else:
				logger.error("el número introducido: " + parametros + "como segundo argumento no es correcto")
				raise IndexError
		except IndexError:
			parametros = "2"
		with open("orden.txt", "wb") as fich:
			pickle.dump(parametros, fich)
		# creación de los bridges y asignación de IP
		subprocess.run(["python3", "network.py", n_bridges, ip_inc, ip_end])
		# creación de las máquinas virtuales y asignación de su tarjeta al bridge lxdbr0
		subprocess.run(["python3", "crear.py", s, imagen, parametros])
		subprocess.run(["python3", "networkconfig.py", s, parametros, ip0])
		# creación del balanceador
		subprocess.run(["python3", "crear.py", lb, imagen, n_lb])
		subprocess.run(["python3", "eth.py", lb, n_lb])
		# Asignamos las tarjetas del contenedor lb a los bridges lxdbr1 & lxdbr0 y Asignamos sus direcciones IPv4:
		subprocess.run(["python3", "networkconfig.py", lb, n_bridges, ip_inc, n_lb])
		# creación del cliente y le asignamos al bridge lxdbr1
		subprocess.run(["python3", "crear.py", c, imagen, n_client]) 
		subprocess.run(["python3", "networkconfig.py", c, n_client, ip1])
		print("creado!")
	
	elif orden == "start":
		subprocess.run(["sudo", "apt", "install", "xterm"])
		# iniciamos cada una de las máquinas virtuales ya creadas con el create
		with open("orden.txt", "rb") as fich:
			numero = pickle.load(fich)
		subprocess.run(["python3", orden+".py", s, numero])
		subprocess.run(["python3", orden+".py", lb, n_lb])
		subprocess.run(["python3", orden+".py", c, n_client])		
		print("start!")

	elif orden == "list":
		# listado de las máquinas virtuales
		with open("orden.txt", "rb") as fich:
			numero = pickle.load(fich)
		subprocess.run(["python3", orden+".py", s, numero])
		subprocess.run(["python3", orden+".py", lb, n_lb])
		subprocess.run(["python3", orden+".py", c, n_client])	
		subprocess.run(["lxc", orden])

	elif orden == "delete":
		subprocess.run(["python3", "pfinal1.py", "pause"])
		# delete de cada uno de las máquinas virtuales ya creadas con el create
		with open("orden.txt", "rb") as fich:
			numero = pickle.load(fich)
		subprocess.run(["python3", orden+".py", s, numero])
		subprocess.run(["python3", orden+".py", lb, n_lb])
		subprocess.run(["python3", orden+".py", c, n_client])
		for i in range(int(n_bridges)-1):
			n = i + 1 
			subprocess.run(["lxc", "network", orden, lxdbr+str(n)])
		print("deleted!")
		
	elif orden == "pause": # esta función pausa todos los contenedores creados al llamarla
		with open("orden.txt", "rb") as fich:
			numero = pickle.load(fich)
		subprocess.run(["python3", orden+".py", s, numero])
		subprocess.run(["python3", orden+".py", lb, n_lb])
		subprocess.run(["python3", orden+".py", c, n_client])
		print("paused!")

	elif orden == "pauseone": # esta función pausa la mv de valor parametros-1
		parametros = sys.argv[2]
		nombre = s + str(int(parametros)-1)
		subprocess.run(["lxc", "stop", nombre, "--force"])
		print("paused "+nombre+"!")

	else:
		# error del parámetro orden
		logger.error("el argumento orden => " + orden + " no es correcto")
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")
