listofONTs = ['1/1/1/1/1','1/1/1/1/1','1/1/1/2/1','1/1/3/4/1','1/1/3/5/16','1/1/1/1/1','1/1/3/4/1','1/1/13/14/11','1/1/13/14/11']
print (listofONTs)

setofONTs = sorted({n for n in listofONTs})

print(setofONTs)
print(setofONTs[0])
print(setofONTs[1])
print(setofONTs[2])

print(len(setofONTs))