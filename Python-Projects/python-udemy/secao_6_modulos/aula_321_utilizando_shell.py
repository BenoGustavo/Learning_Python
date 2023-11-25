import subprocess

# -> on windows use cp850

# This is the way you pass the shell commands to the subprocess module
commands = ["ping", "www.google.com.br","-c","4"]

#run the commands
proc = subprocess.run(commands,capture_output=True,text=True)

#print the args that is the list of commands
print(proc.args)

# print the return code
print(proc.stdout)

# print the error code
print(proc.stderr)