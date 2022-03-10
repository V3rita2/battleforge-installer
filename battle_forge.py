from concurrent.futures import process
import subprocess
import os
#imports required libraries

#defines file path
directory = os.path.expanduser('~/Documents')

#test if path is correct
textfile = open(f'C:/Users{directory}', 'w')
lines=['test complete']
textfile.writelines(lines)
textfile.close()

#base function to run code on local user's command line
def runcmd(cmd, verbose = False, *args, **kwargs) :

    #Defines the basics of how to talk to the command line
        process = subprocess.Popen(
            cmd,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True,
            shell = True
        )

        std_out, std_err = process.communicate()

        if verbose: 
            print(std_out.strip(), std_err)
        pass

runcmd('echo "hello, World!" ', verbose = True)



# runcmd("wget -P  https://github.com/TTSWarhammer40k/Battleforged-Workshop-Mod-Compilation/raw/master/battle-forge.zip", verbose=True)
