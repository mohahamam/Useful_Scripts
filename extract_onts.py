import re
inputfile='sample.txt'
ouputfile='extactedONTs.txt'
def extractonts(input01,output01):
	ont_regex = re.compile(r'(\b1/1(/(1[0-6]|[1-9])){2}/(109|119|1[0-2][0-8]|[1-9]\d|[1-9])\b)')
	with open (input01) as file1, open(output01,'w') as outfile:
		onts = file1.read()
		ont = ont_regex.findall(onts)
		ontlist = [ont[i][0]for i,x in enumerate(ont)]
		used=set()
		unique = [x for x in ontlist if x not in used and (used.add(x) or True)]
		print('\n'.join(unique))
		outfile.writelines('\n'.join(unique))	

def main():
	extractonts(inputfile,ouputfile)
if __name__ == '__main__':
	main()