import sys
import subprocess
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1]
	numero = sys.argv[2]
	for j in range(int(numero)):
			nombre = orden + str(j)
			subprocess.run(["lxc", "start", nombre])
			subprocess.run(["lxc", "exec", nombre, "ipaddr"])
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden en list.py")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")