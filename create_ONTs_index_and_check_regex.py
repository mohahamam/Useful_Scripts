import re,pprint,time

t1 = time.time()
print(t1)
expression = r'(\b1/1/([1][0-6]|[1-9])/([1][0-6]|[1-9])/(109|119|[1][0-2][0-8]|[1-9]\d|[1-9])\b)'
expression1 = r'(\b1/1(/(1[0-6]|[1-9])){2}/(109|119|1[0-2][0-8]|[1-9]\d|[1-9])\b)'
expression2 = r'(\b1/1(/(1[0-6]|[1-9])){2}\b)'
test = [('1/1/'+str(i)+'/'+str(x)+'/'+str(y)) for i in range (1,17) for x in range (1,17) for y in range(1,129) ]

extracted= [re.findall(expression1,i)[0] for i in test ]
extractedpon =[re.findall(expression2,j)[0] for j in test]

listofONTs = [extracted[i][0] for i,x in enumerate(extracted)]
listofPONs = sorted({extractedpon[i][0] for i,x in enumerate(extractedpon)})

t2 = time.time()

pprint.pprint(listofONTs)
pprint.pprint(listofPONs)

print(len(listofONTs))
print(len(listofPONs))
print(str(t2-t1))
