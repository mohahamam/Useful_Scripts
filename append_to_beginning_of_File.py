def line_prepender(filename, line):
	with open(filename, 'r+') as f:
		content = f.read()
		f.seek(0, 0)
		f.write(line.rstrip('\r\n') + '\n' + content)
		
with open ('OLTs.txt','r') as file1:
	inputthings=file1.read()

	line_prepender('extactedPONs.txt', inputthings)