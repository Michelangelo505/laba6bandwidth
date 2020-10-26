#!/usr/bin/python3

import sys, time
from socket import *

count = 1000
BUFSIZEUDP = 300
BUFSIZETCP = 300
ip = '192.168.88.233'
port = 9876


def clientTCP():
    testdata = 'x' * (BUFSIZETCP - 1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((ip, int(port)))
    t3 = time.time()
    i = 0
    while i < count:
        i = i + 1
        s.send(bytearray(testdata, "utf-8"))
    s.shutdown(1)
    t4 = time.time()
    data = s.recv(BUFSIZETCP)
    t5 = time.time()
    print(data.decode())
    print('ping:', (t3 - t2) + (t5 - t4) / 2)
    print('Time:', t4 - t3)
    print('Bandwidth:', round((BUFSIZETCP * count / (1024 * 1024)) / (t4 - t3), 3), 'MB/sec.')

def clientUDP():
    testdata = 'x' * (BUFSIZEUDP - 1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_DGRAM)
    # t2 = time.time()
    t3 = time.time()
    i = 0
    while i < count:
        i = i + 1
        s.sendto(bytearray(testdata, "utf-8"), (ip, int(port)))
    t4 = time.time()
    data = s.recvfrom(BUFSIZEUDP)
    t5 = time.time()
    print(data)
    # print('ping:', (t3 - t2) + (t5 - t4) / 2)
    print('Time:', t4 - t5)
    print('Bandwidth:', round((BUFSIZEUDP * count / (1024 * 1024)) / (t5 - t3), 3), 'MB/sec.')


clientTCP()
