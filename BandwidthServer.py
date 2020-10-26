#!/usr/bin/python3

import sys, time
from socket import *
import threading

BUFSIZEUDP = 300
BUFSIZETCP = 1440
port = 9876


def serverTCP():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    print('Server ready...')
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZETCP)
            if not data:
                break
            del data
        conn.send(bytearray('OK\n', 'utf-8'))
        conn.close()
        print('Done with', host, 'port', remoteport)


def serverUDP():
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', int(port)))
    print('Server ready...')
    while 1:
        data, adress = s.recvfrom(BUFSIZEUDP)
        if not data:
            break
        del data
        s.sendto(bytearray('OK\n', 'utf-8'), adress)
    print('Done with', adress)


serverTCP()
