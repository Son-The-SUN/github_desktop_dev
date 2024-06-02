import subprocess

yarn_init = str(subprocess.check_output("yarn", shell=True))

print(yarn_init)

yarn_build_dev = str(subprocess.check_output("yarn build:dev", shell=True))

print(yarn_build_dev)

yarn_start = str(subprocess.check_output("yarn start", shell=True))

print(yarn_start)


