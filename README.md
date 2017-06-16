# i-XIP Internet Radio System

This project is a HTTP proxy used to bypass the official i-XIP Internet radio servers, because either the target servers get down sometimes, or the software is buggy and the station list disappears. Moreover, when it works, there are plenty of levels to reach the stations, and the browsing via the LCD is painful.
Anyway, this results in a half functional system regarding connectivity and user usage, while the audio quality of speakers seems quite good to me on the other hand.

# Which software version is needed ?

It will successfully fool this KW-1005IR based radio system (at least)
![i-Xip example](https://github.com/stevemoreau/ixip/raw/master/iXip.jpg)

The servers that this system tries to reach are:
  - http://pri.wifiradiofrontier.com
  - http://sec.wifiradiofrontier.com

When browsing the LCD via menu button > 'Main menu' > 'Info' > 'SW version', it will dump something like
```ir-sermmi.alb.ven6-kw1005ir-nodab_V1.1.7.14611-1```

However, I suspect it may also fool these vendors:
  - Kenwin KW-1005-iR
  - DGTEC DG-KW1005iR Mini HiFi System

# What do I need to use it ?

The current version requires:
  - A Linux server gateway to act as a proxy (ie. to intercept HTTP requests to http://*.wifiradiofrontier.com)
  - Some time to track your favorite MP3 radio stations, especially the URL (such as http://184.107.185.106:8000/listen.pls). I usually use shoutcast.com to find a station and download the .pls file. Once opened, the URL is availbale.
  - Some basic Python knowledge to edit 
  - Some Linux commands to be executed on the gateway to configure iptables, and install requirements

# Installation

Please note there is no installer currently, and the manual setup can be quite complex if you are not familiar with Linux.
Persevrance may be necessary.

- Connect to your gateway via SSH for example, copy files in your user home, and run
```$ ls ~/*ixip
/home/.../ixip
/home/.../ixip.py

$ mkdir /etc/ixip
$ sudo cp ~/ixip /etc/init.d/ixip
$ sudo cp ~/ixip.py /etc/ixip/ixip.py
$ sudo update-rc.d ixip defaults 99
$ sudo apt-get install python-cherrypy3
$ sudo service ixip restart```

- Check everything fine
```$ sudo iptables -nvL -t nat | grep 8118
   16   704 REDIRECT   tcp  --  eth0   *       192.168.0.111        0.0.0.0/0            tcp dpt:80 redir ports 8118
$ tail -f 
192.168.0.111 - - [15/Jun/2017:19:24:48] "GET /setupapp/fs/asp/BrowseXML/loginXML.asp?token=0 HTTP/1.0" 200 49 "" "FSL IR/0.1"
IXipSearch search=333005
192.168.0.111 - - [15/Jun/2017:19:24:48] "GET /setupapp/fs/asp/BrowseXML/Search.asp?sSearchtype=3&Search=333005&mac=4c799d6b5bac0d271dff2cc35921dd31&dlang=eng&fver=1 HTTP/1.0" 200 803 "" "FSL IR/0.1"
IXipSearch login=0
192.168.0.111 - - [15/Jun/2017:19:29:23] "GET /setupapp/fs/asp/BrowseXML/loginXML.asp?token=0 HTTP/1.0" 200 49 "" "FSL IR/0.1"
IXipSearch search=333001
192.168.0.111 - - [15/Jun/2017:19:29:23] "GET /setupapp/fs/asp/BrowseXML/Search.asp?sSearchtype=3&Search=333001&mac=4c799d6b5bac0d271dff2cc35921dd31&dlang=eng&fver=1 HTTP/1.0" 200 820 "" "FSL IR/0.1"
IXipSearch login=0
192.168.0.111 - - [16/Jun/2017:07:28:31] "GET /setupapp/fs/asp/BrowseXML/loginXML.asp?token=0 HTTP/1.0" 200 49 "" "FSL IR/0.1"
IXipSearch search=333001
192.168.0.111 - - [16/Jun/2017:07:28:31] "GET /setupapp/fs/asp/BrowseXML/Search.asp?sSearchtype=3&Search=333001&mac=4c799d6b5bac0d271dff2cc35921dd31&dlang=eng&fver=1 HTTP/1.0" 200 820 "" "FSL IR/0.1"```

- Stop/start your Internet radio, and try to navigate in LCD menus

NOTE: The iptables must be entered at each boot, except if you tune your Linux configuration (google "save iptables rule")
Alternately, you may install arno-iptables-firewall to make the iptables permanent easily
$ sudo apt-get install arno-iptables-firewall
$ sudo emacs -nw /etc/arno-iptables-firewall/plugins/transparent-proxy.conf
ENABLED=1
HTTP_PROXY_PORT="8118"
HTTP_PROXY_INT_SOURCES="192.168.0.111/0"

# This script does not work mine, how can I reproduce the backtracking ?

  - Login to your gateway and save network traffic coming from your radio with tcpdump for example
    ```sudo tcpdump -n -w ixip.pcap -i eth0 host 192.168.0.111 and port 80```
  - Open the file with Wireshark and your should see something like
    ![i-Xip example](https://github.com/stevemoreau/ixip/raw/master/iXipWiresharkCapture.png)
  - Check the inner structure of XML messages and update the python file manually to provide the right answer.