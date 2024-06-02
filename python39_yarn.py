import subprocess
import logging
import os

curdir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename= f"{curdir}\\sonthesun_gh_desktop_log.txt",level=logging.DEBUG)
logging.debug("I love you 3000")
logger = logging.getLogger(f"{curdir}\\sonthesun_gh_desktop_log.txt")

yarn_init = str(subprocess.check_output("yarn", shell=True))

logger.debug(yarn_init)

yarn_build_dev = str(subprocess.check_output("yarn build:dev", shell=True))

logger.debug(yarn_build_dev)

yarn_start = str(subprocess.check_output("yarn start", shell=True))

logger.debug(yarn_start)

logger.debug("I love you 3000")

print("I love you 3000")




