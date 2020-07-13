#!/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import socket
import struct
import os
import threading
import time
from random import randint

def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += ord(data[i]) + (ord(data[i + 1]) << 8)
    if n:
        s += ord(data[i + 1])
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xffff
    return s


class IP(object):
    def __init__(self, source, destination, payload='', proto=socket.IPPROTO_TCP):
        self.version = 4
        self.ihl = 5  # Internet Header Length
        self.tos = 0  # Type of Service
        self.tl = 20 + len(payload)
        self.id = 0  # random.randint(0, 65535)
        self.flags = 0  # Don't fragment
        self.offset = 0
        self.ttl = 255
        self.protocol = proto
        self.checksum = 2  # will be filled by kernel
        self.source = socket.inet_aton(source)
        self.destination = socket.inet_aton(destination)

    def pack(self):
        ver_ihl = (self.version << 4) + self.ihl
        flags_offset = (self.flags << 13) + self.offset
        ip_header = struct.pack("!BBHHHBBH4s4s",
                                ver_ihl,
                                self.tos,
                                self.tl,
                                self.id,
                                flags_offset,
                                self.ttl,
                                self.protocol,
                                self.checksum,
                                self.source,
                                self.destination)
        self.checksum = checksum(ip_header)
        ip_header = struct.pack("!BBHHHBBH4s4s",
                                ver_ihl,
                                self.tos,
                                self.tl,
                                self.id,
                                flags_offset,
                                self.ttl,
                                self.protocol,
                                socket.htons(self.checksum),
                                self.source,
                                self.destination)
        return ip_header


class UDP(object):
    def __init__(self, src, dst, payload=''):
    # def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.payload = payload
        self.checksum = 0
        self.length = 8  # UDP Header length

    def pack(self, src, dst, proto=socket.IPPROTO_UDP):
        length = self.length + len(self.payload)
        pseudo_header = struct.pack('!4s4sBBH',
                                    socket.inet_aton(src), socket.inet_aton(dst), 0,
                                    proto, length)
        self.checksum = checksum(pseudo_header)
        packet = struct.pack('!HHHH',
                             self.src, self.dst, length, 0)
        return packet


s = socket.socket(socket.AF_INET,
                      socket.SOCK_RAW,
                      socket.IPPROTO_RAW)
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fakesrc = "10.1.1.1"
dst = "10.8.4.31"
dstport = 5555
payload = "UDP fake packet test"

def send_info(sip,dip,port,info):
	udp = UDP(randint(1, 65535), port, info).pack(sip, dip)
	ip = IP(sip, dip, udp, proto=socket.IPPROTO_UDP).pack()
	s.sendto(ip + udp + info, (dip, port))


def get_file(root,filename):
	params=filename.split("-")
	if len(params)==2:
		f = open(root+filename)
        for line in f:
            if params[1] == "4104":
                send_info(params[0],"172.16.0.200",int(params[1]),line.encode("GB2312"))
                print(line)
        time.sleep(1)
	f.close()

for root, dirs, files in os.walk("/opt/flume/apache-flume-1.9.0-bin/udpport/"):
	for filename in files:
		get_file(root,filename)
		#t1 = threading.Thread(target=get_file, args=(root,filename,))
		#t2 = threading.Thread(target=run, args=("t2",))
		#t1.start()




