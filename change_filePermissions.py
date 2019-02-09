from subprocess import *
with open ('testfile.txt','w') as f1:
	f1.write('test input')
	call('chmod 777 testfile.txt',shell=True)
