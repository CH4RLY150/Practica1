import sys
import subprocess
import logging

s = "vm"
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

try:
	orden = sys.argv[1]
	numero = sys.argv[2]
	for j in range(int(numero)):
		nombre = orden + str(j)
		subprocess.run(["lxc", "start", nombre])
		if orden == s:
			comando = "lxc exec " + nombre + " bash"
			subprocess.Popen(["xterm", "-fa", "monaco", "-fs", "13", "-bg", "pink", "-fg", "black", "-e", comando])
except IndexError:
	logger.error("IndexError, no se ha introducido ninguna orden en start.py")
	#raise
except KeyboardInterrupt:
	logger.error("Terminado")