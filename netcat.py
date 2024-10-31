import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading


def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(
        shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
          netcat.py -t 192.168.1.108 -p 5555 -l -c
          netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup
          netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\"
          echo 'ABCDEFGHI' | ./netcat.py -t 192.168.1.108 -p 135
          netcat.py -t 192.168.1.108 -p 5555
          '''))
    parser.add_argument('-c', '--commend', action='store_true',
                        help='initialize command shell')

    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int,
                        default=5555, help='specified port')
    parser.add_argument(
        '-t', '--target', default='192.168.1.203', help='specified IP')
    parser.add_argument('-u','--upload', help='upload file')
    args=parser.parse_args()
    if args.listen:
        buffer=''
    else:
        buffer=sys.stdin.read()
        nc=NetCat(args,buffer.encode('utf-8'))
        nc.run()


    class NetCat:
        
