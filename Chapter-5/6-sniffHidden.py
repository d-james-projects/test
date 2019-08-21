#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from scapy.all import *

interface = 'wlan0mon'

hiddenNets = []
unhiddenNets = []

def sniffDot11(p):
    
    if p.haslayer(Dot11ProbeResp):
        #print(p)
        
        if p.haslayer(Dot11):
            addr2 = p.getlayer(Dot11).addr2
            if (addr2 in hiddenNets) and (addr2 not in unhiddenNets):
                netName = p.getlayer(Dot11ProbeResp).info
                print ('[+] Decloaked Hidden SSID : ' +\
                    netName.decode('utf-8') + ' for MAC: ' + addr2.decode('utf-8'))
                unhiddenNets.append(addr2)
         
    
    if p.haslayer(Dot11Beacon):
        if p.getlayer(Dot11Beacon).info == '':
            if p.haslayer(Dot11):
                addr2 = p.getlayer(Dot11).addr2
                if addr2 not in hiddenNets:
                    print ('[-] Detected Hidden SSID: ' +\
                           'with MAC:' + addr2.decode('utf-8'))
                    hiddenNets.append(addr2)


sniff(iface=interface, prn=sniffDot11)