import time, difflib
def Main():
	file1=input('Please provide file1 name\n')
	file2=input('Please provide file2 name\n')
	file3='Comparison'+str(time.time())+'.html'
	first_file = open(file1).readlines()
	second_file = open(file2).readlines()

	difference = difflib.HtmlDiff(wrapcolumn=60).make_file(first_file,second_file,file1,file2)
	difference_report=open(file3,'w')
	difference_report.write(difference)
	difference_report.close()
if __name__=='__main__':
	Main()

#dubai_ams.conf
#abudhabi_ams.conf