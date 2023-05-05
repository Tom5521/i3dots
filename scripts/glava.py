from os import system as sys
import os,signal,subprocess

def command_read(comando):
    try:
        resultado = subprocess.check_output(comando, shell=True)
        return resultado
    except subprocess.CalledProcessError:
        print("Error al ejecutar el comando")
        return 0


pid = int(command_read("pidof glava"))

if pid != 0:
    try:
        os.kill(pid, signal.SIGKILL)
        print("Proceso con PID {} terminado".format(pid))
    except OSError as e:
        print("Error al matar el proceso:", e)
else:
    sys("glava -d &")
