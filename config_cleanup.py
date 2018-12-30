import argparse
import os

####Handle input and output file names
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    """Usage is migrate_SRAN_Wifi_04.py --i inputfilename --o outputfilename"""
    parser.add_argument("--i", help="Input file name which is a log of the OLT info configure file")
    parser.add_argument("--o", help="The output file name which will be xlsx file. You dont have to give .xlsx extension it will be added automatially")
args = parser.parse_args()
inputfile=(args.i)
outputfile=(args.o)

###Handle the output file extension
if outputfile==None:
	outputfile='Cleaned_configure_commands'

if '.xlsx' in outputfile:
	outputfile = outputfile.strip('.xlsx')
elif'.xls' in outputfile:
	outputfile = outputfile.strip('.xls')
elif'.csv' in outputfile:
	outputfile = outputfile.strip('.csv')
elif'.txt' in outputfile:
	outputfile = outputfile.strip('.txt')

##### Creat a function to chose only configure lines and ignore other lines
def find(substr, omit, infile, outfile):
    with open(infile,'r') as a, open(outfile, 'w') as b:
    	for line in a:
         	if omit in line:
         		continue
         	elif line.startswith(substr):
         		b.write(line)
 
####Apply the function to get the output file    
find('configure', '>', inputfile, outputfile+'.txt')

#### Prompt the user with successful operation.
print ('''Sucess.......
####################################
The file ''',outputfile+'.txt','''
has been created in the Directory:
'''+os.getcwd())