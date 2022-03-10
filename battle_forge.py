from concurrent.futures import process
import subprocess
#imports the subprocess library to run cmd

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
