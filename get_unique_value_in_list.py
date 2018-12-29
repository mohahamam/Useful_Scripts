import re
listofONTs = ['1/1/1/1/1','1/1/1/1/1','1/1/1/2/1','1/1/3/4/1','1/1/3/5/16','1/1/1/1/1','1/1/3/4/1','1/1/13/14/11','1/1/13/14/11']
print (listofONTs)

setofONTs = sorted({n for n in listofONTs})

print(setofONTs)
print(setofONTs[0])
print(setofONTs[1])
print(setofONTs[2])

print(len(setofONTs))
print(type(setofONTs))

setofONTs1 = sorted({n.replace('/','-') for n in listofONTs if n!='1/1/1/1/1' if n!='1/1/1/2/1'})
print(setofONTs1)

PONRegex = r'(\b1/1/(1[0-6]|[1-9])/(1[0-6]|[1-9])\b)'
#test = re.findall(PONRegex,'1/1/15/16/1')
#print(test[0][0])

def findPON(ONTnumber):
	PONnumber = re.findall(PONRegex,ONTnumber)
	return PONnumber

listofPONs =sorted({findPON(n)[0][0] for n in listofONTs})
print(listofPONs)


