import os
import time
import sys
import socket


def clr():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

clr()

print('\033[31m FETCH IP ADDRESS\033')
start = time.time()
print('\n\033[1;34mBy.. Nimish Go\033[0m \n\033[0;32mVersion:1.0\trelease date:21-09-2019\033[0m')
print(time.asctime(),'\n')

red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'


print(green,'\"This Tool is to fetch the IP address\"')

while True:
    print(f'{blue}Enter website name ')
    a = input('> ').strip()

    b = 'www.'
    ccom = '.com'
    dcom = b+a+ccom
    cnet = ".net"
    dnet = b+a+cnet
    cin = ".in"
    din = b+a+cin
    cgov = ".gov"
    dgov = b+a+cgov
    try:
        print('\033[0m','-'*13,'-'*(len(a)+8),'-'*20)
        ip_com = socket.gethostbyname(dcom)
        print(f'{blue}IP address of {red}{dcom}{blue} : {red}{ip_com}\n')
        time.sleep(2)
        print('\033[0m', '-' * 13, '-' * (len(a) + 8), '-' * 20)
        ip_net = socket.gethostbyname(dnet)
        print(f'{blue}IP address of {red}{dnet}{blue} : {red}{ip_net}\n')
        time.sleep(2)
        print('\033[0m', '-' * 13, '-' * (len(a) + 8), '-' * 20)
        ip_in = socket.gethostbyname(din)
        print(f'{blue}IP address of {red}{din}{blue} : {red}{ip_in}\n')
        print('\033[0m', '-' * 13, '-' * (len(a) + 8), '-' * 20)
        ip_gov = socket.gethostbyname(dgov)
        print(f'{blue}IP address of {red}{dgov}{blue} : {red}{ip_gov}\n')

    except socket.gaierror:
        print(f'{blue}Name or service not known')
    home = input(f"{green}Enter{red} [1] {green}to EXIT or any key to continue...")
    if home == '1':
        time.sleep(2)
        clr()
        print('\n\033[0mNimish Go thanks and appreciate all members contribution and support')
        break
