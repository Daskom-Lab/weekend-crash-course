import os
import subprocess

if __name__ == "__main__":
    print(f'HASIL : {os.system("date")}')

    print('-------')

    print(f'HASIL : {os.popen("date").read()}')

    print('-------')

    print(f'HASIL : {subprocess.Popen("ls -la", shell=True, stdout=subprocess.PIPE, stdin=None, stderr=subprocess.DEVNULL).communicate()[0]}')