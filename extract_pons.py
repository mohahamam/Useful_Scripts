import re
inputfile='sample.txt'
ouputfile='extactedPONs.txt'
def extractpons(input01,output01):
	import re
	pon_regex = re.compile(r'(\b1/1(/(1[0-6]|[1-9])){2}\b)')

	with open (input01,'r') as infile:
		pons = infile.read()
#	pons = ''.join(pons) #without it the script is faster, with it you need to use readlines
	pon = pon_regex.findall(pons)

	ponlist = [pon[i][0]for i,x in enumerate(pon)]

	used=set()
	unique = [x for x in ponlist if x not in used and (used.add(x) or True)]
	print('\n'.join(unique))
	with open(output01,'w') as outfile:
		outfile.writelines('\n'.join(unique))

def main():
	extractpons(inputfile,ouputfile)
if __name__ == '__main__':
	main()