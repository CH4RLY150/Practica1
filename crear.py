import sys
import subprocess
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1]
	imagen = sys.argv[2]
	parametros = sys.argv[3]
	print("creando " + parametros + " " + orden)
	for i in range(int(parametros)):
		nombre = orden + str(i)
		subprocess.run(["lxc", "init", imagen, nombre])
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")