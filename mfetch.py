import platform
import getpass
from uptime import uptime

spf = platform.platform()
if "indows-7" in spf:
    spf = "Windows 7"
elif "indows-10" in spf:
    spf = "Windows 10"

sys = platform.machine()
prc = platform.processor()
usr = getpass.getuser()
hst = platform.node()
upt = uptime()
utm = int(upt/60%60)
uth = int(upt/60/60%24)
utd = int(upt/60/60/24)
inf = ""

if "indows" in spf:

    inf = """           
           _.-;;-._     {}@{}
    '-..-'|   ||   |    os:  {}
    '-..-'|_.-;;-._|    arc: {}
    '-..-'|   ||   |    prc: {}
    '-..-'|_.-''-._|    upt: {} days, {} hours, {} minutes
    """

    if "Windows 10" in spf:
        inf = """           
                  _.-:    {}@{}
             _.-:|   |    os:  {}
            |   ||_.-|    arc: {}
            |_.-||   |    prc: {}
            |   ||_.-'    upt: {} days, {} hours, {} minutes
            |_.-'
        """

elif "inux" in spf:

    inf = """
             .---.         {}@{}
            /     \        os:  {}
            \.@-@./        arc: {}
            /`\_/`\        prc: {}
           //  _  \\\      upt: {} days, {} hours, {} minutes
          | \     )|_ 
         /`\_`>  <_/ \\
         \__/'---'\__/
    """
        

elif "Mac" in spf:

    inf = """
   			        .:'             
			     _ :'_      
			.'\`_\`-'_\`\    {}@{}
			:        .-'     os:  {}
			:        :       arc: {}
			 :        `-;    prc: {}
			  `._.-._.'      upt: {} days, {} hours, {} minutes
    """

else:
    print("unsupported system!")  

print(inf.format(usr, hst, spf, sys, prc, utd, uth, utm)) 













