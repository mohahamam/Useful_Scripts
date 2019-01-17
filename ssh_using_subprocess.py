import subprocess
#subprocess.call('ls')
#subprocess.call(['ls','-lrt'])
#filesize = subprocess.call(['df','-kh'],shell=True)
subprocess.call(['ssh','hamam@i7mini','ssh -T','hamam@localhost'])
#print (filesize)

filesize = subprocess.check_output(['df',"-kh"])
print (filesize)