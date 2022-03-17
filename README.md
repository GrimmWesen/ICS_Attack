- Attack.xml 为标记性说明性质文件，在每个攻击中记录ip、pot、os等信息。
- python版本为2.7
- revers_tcp.py为鱼叉攻击中在目标机端运行的文件，主要进行bind(host,port)、connect（），运行环境同为python2.7，另需要pywin32等库支持。
- 主要运行程序为start.py，以此调用其他攻击方式。
- 另Ddos攻击主要利用C进行套接字编程，需要运行环境有cpp支持。


以上提交代买均在Kali 2018.4 以及windows xp professional sp3 测试运行无误。