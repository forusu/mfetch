#!bin/python3

import platform
from uptime import uptime

spf = platform.platform()
sarch = platform.machine()
proc = platform.processor()
ut = uptime()
utm = int(ut/60%60)
uth = int(ut/60/60%24)
utd = int(ut/60/60/24)

if "Windows-7" in spf:
    print("""
             _.-;;-._      platform: {}
            |   ||   |     architecture: {}
            |_.-77-._|     processor: {}
            |   ||   |     uptime: {} days, {} hours, {} minutes
            |_.-''-._|
    """.format(spf, sarch, proc, utd, uth, utm))

elif "Windows-10" in spf:
    print("""           
                  _.-;     platform: {}
             _.-;|   |     architecture: {}
            |   ||_.-|     processor: {}
            |_.-||   |     uptime: {} days, {} hours, {} minutes
            |   ||_.-'   
            |_.-'
    """.format(spf, sarch, proc, utd, uth, utm))

elif "Linux" in spf:
    print("""
            .---.
           /     \         platform: {}
           \.@-@./         architecture: {}
           /`\_/`\         processor: {}
          //  _  \\        uptime: {} days, {} hours, {} minutes
         | \     )|_ 
        /`\_`>  <_/ \
        \__/'---'\__/
    """.format(spf, sarch, proc, utd, uth, utm))




