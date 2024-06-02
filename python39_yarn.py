import subprocess
import webbrowser
import socket
import logging
import os
import signal
curdir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename= curdir + "sonthesun_gh_desktop_log.txt",level=logging.DEBUG)
logging.debug("I love you 3000")
logger = logging.getLogger()

def check_port(port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      return s.connect_ex(('localhost', port)) == 0

def kill_process_on_port(port):
    command = f'netstat -ano | findstr :{port}'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            pid = line.split()[-1]
            os.kill(int(pid), signal.SIGTERM)
def start_I_love_you_3000():
  yarn_init = str(subprocess.check_output("yarn", shell=True))

  logger(yarn_init)

  yarn_build_dev = str(subprocess.check_output("yarn build:dev", shell=True))

  print(yarn_build_dev)

  yarn_start = str(subprocess.check_output("yarn start", shell=True))

  print(yarn_start)

  print("I love you 3000")

if __name__ == "__main__":
  edge = webbrowser.get("edge")
  if check_port(3000):
    kill_process_on_port(3000)
    start_I_love_you_3000()
    edge.open("http://localhost:3000")
  else:
    raise Exception("Port 3000 is not available")




