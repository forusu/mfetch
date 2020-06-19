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
inf = ""


if "Windows" in spf:

    if "Windows-7" in spf:
        spf = 'Windows 7'
        inf = """                      
                 _.-;;-._      {}@{}
                |   ||   |     platform: {}
                |_.-77-._|     architecture: {}
                |   ||   |     processor: {}
                |_.-''-._|     uptime: {} days, {} hours, {} minutes
        """

    elif "Windows-10" in spf:
        spf = 'Windows 10'
        inf = """           
                      _.-:     {}@{}
                 _.-:|   |     platform: {}
                |   ||_.-|     architecture: {}
                |_.-||   |     processor: {}
                |   ||_.-'     uptime: {} days, {} hours, {} minutes
                |_.-'
        """

    else:
        inf = """
               _.-;;-._      {}@{}
        '-..-'|   ||   |     platform: {}
        '-..-'|_.-;;-._|     architecture: {}
        '-..-'|   ||   |     processor: {}
        '-..-'|_.-''-._|     uptime: {} days, {} hours, {} minutes
        """
    
    
        

elif "inux" in spf:

    if "Arc" in spf:

        inf = """
       -  -  - -  - - /\\         {}@{}
		     /  \\        platform: {}
	            /\\   \\       architecture: {}
		   /      \\      processor: {}
		  /   ,,   \\     uptime: {} days, {} hours, {} minutes
   	    -  - /   |  |  -\\
		/_-''    ''-_\\
        """
       

    else:

        inf = """
             .---.          {}@{}
            /     \         platform: {}
            \.@-@./         architecture: {}
            /`\_/`\         processor: {}
           //  _  \\\        uptime: {} days, {} hours, {} minutes
          | \     )|_ 
         /`\_`>  <_/ \\
         \__/'---'\__/
        """
        

elif "Mac" in spf:

    inf = """
   			        .:'             
			     _ :'_         {}@{}
			.'\`_\`-'_\`\      platform: {}
			:________.-'       architecture: {}
			:_______:          processor: {}
			 :_______\`-;      uptime: {} days, {} hours, {} minutes
			  \`._.-._.'
        """
else:
    print("unsupported system!")  

print(inf.format(usr, hst, spf, sarch, proc, utd, uth, utm)) 






