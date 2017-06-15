# i-XIP Internet Radio System

This project is a HTTP proxy used to bypass the official i-XIP Internet radio servers, because either the target servers get down sometimes, or the software is buggy and the station list disappears. Moreover, when it works, there are plenty of levels to reach the stations, and the browsing via the LCD is painful.
Anyway, this results in a half functional system regarding connectivity and user usage, while the audio quality of speakers seems quite good to me on the other hand.

# Which sofrware version is needed ?

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
  - a Linux server gateway to act as a proxy (ie. to intercept HTTP requests to http://*.wifiradiofrontier.com)
  - some time to track your favorite MP3 radio stations, especially the URL (such as http://184.107.185.106:8000/listen.pls)
  - some basic Python knowledge to edit 
  - some Linux commands to be executed on the gateway to configure iptables, and install requirements

Please note there is no installer, and the manual setup can be quite complex if you are not familiar with Linux.
Persevrance may be necessary.