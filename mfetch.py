import platform
import getpass
from uptime import uptime

spf = platform.platform()
sarch = platform.machine()
proc = platform.processor()
usr = getpass.getuser()
hst = platform.node()
ut = uptime()
utm = int(ut/60%60)
uth = int(ut/60/60%24)
utd = int(ut/60/60/24)


if "Windows-7" in spf:
    print("""                       
             _.-;;-._      {}@{}
            |   ||   |     platform: {}
            |_.-77-._|     architecture: {}
            |   ||   |     processor: {}
            |_.-''-._|     uptime: {} days, {} hours, {} minutes
    """.format(usr, hst, spf, sarch, proc, utd, uth, utm))

elif "Windows-10" in spf:
    print("""           
                  _.-;     {}@{}
             _.-;|   |     platform: {}
            |   ||_.-|     architecture: {}
            |_.-||   |     processor: {}
            |   ||_.-'     uptime: {} days, {} hours, {} minutes
            |_.-'
    """.format(usr, hst, spf, sarch, proc, utd, uth, utm))

elif "Windows" in spf:
        print("""
             _.-;;-._      {}@{}
      '-..-'|   ||   |     platform: {}
      '-..-'|_.-;;-._|     architecture: {}
      '-..-'|   ||   |     processor: {}
      '-..-'|_.-''-._|     uptime: {} days, {} hours, {} minutes
    """.format(usr, hst, spf, sarch, proc, utd, uth, utm))
    

elif "Linux" in spf:
    print("""
            .---.          {}@{}
           /     \         platform: {}
           \.@-@./         architecture: {}
           /`\_/`\         processor: {}
          //  _  \\        uptime: {} days, {} hours, {} minutes
         | \     )|_ 
        /`\_`>  <_/ \
        \__/'---'\__/
    """.format(usr, hst, spf, sarch, proc, utd, uth, utm))




