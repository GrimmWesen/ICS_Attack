#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
from socket import *
from threading import *

#端口扫描
screenLock = Semaphore(value=1)
class PortScan:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=int(port)
    
    def conn_scan(self):
            try:
                connSkt = socket(AF_INET, SOCK_STREAM)
                connSkt.connect((self.ip, self.port))
                connSkt.send('ViolentPython\r\n')
                results = connSkt.recv(100)
                screenLock.acquire()
                print '[+] %d/tcp open' % self.port
                print '[+] ' + str(results)
            except:
                screenLock.acquire()
                print '[-] %d/tcp closed' % self.port
            finally:
                screenLock.release()
                connSkt.close()	
    def port_scan(self):
        try:
            tgtIP = gethostbyname(self.ip)
        except:
            print "[-] Cannot resolve '%s': Unknown host" %self.ip
            return
    
        try:
            tgtName = gethostbyaddr(tgtIP)
            print '\n[+] Scan Results for: ' + tgtName[0]
        except:
            print '\n[+] Scan Results for: ' + tgtIP
    
        setdefaulttimeout(1)
        self.conn_scan()
       # for tgtPort in tgtPorts:
            #t = Thread(target=conn_scan,args=(tgtHost,int(tgtPort)))
            #t.start()        
        
        
    