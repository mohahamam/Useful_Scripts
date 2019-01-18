import time
def Main():
	file1=input('Please provide file1 name\n')
	file2=input('Please provide file2 name\n')
	file3='Comparison'+str(time.time())+'.txt'
	with open (file1,'r') as a, open(file2,'r') as b,open(file3,'w') as c:
		a1=a.readlines()
		b1 =b.readlines()
		c.write('file1 name is = '+file1+'\n')
		c.write('file2 name is = '+file2+'\n')
		c.write('~'*97+'\n')
		linenum=0
		for linex,liney in zip(a1,b1):
			if linex==liney:
				continue
			else:
				print('file1:'+linex.rstrip('\n'))
				print('file2:'+liney)
				c.write('file1:'+linex)
				c.write('file2:'+liney+'\n')
				linenum+=1
	

		c.write('\n'+'~'*97+'\n'+'Total Number of different lines = '+str(linenum))
if __name__=='__main__':
	Main()

#dubai_ams.conf
#abudhabi_ams.conf