from subprocess import *
import re
import csv
import arrow


#ip1 = input('Please provide Hostid:')
#user1 = input('Please Provide user name:')
#password1 = input('Please Provide password:')
#port1 = input('Please Provide port number:')

###########################Below function cleans up the output of the cli and T&D logs from ansi escape codes.

def strip_ansi_escape_codes(string_buffer):

	"""

	Remove any ANSI (VT100) ESC codes from the output



	http://en.wikipedia.org/wiki/ANSI_escape_code



	Note: this does not capture ALL possible ANSI Escape Codes only the ones

	I have encountered



	Current codes that are filtered:

	ESC = '\x1b' or chr(27)

	ESC = is the escape character [^ in hex ('\x1b')

	ESC[24;27H   Position cursor

	ESC[?25h     Show the cursor

	ESC[E        Next line (HP does ESC-E)

	ESC[K        Erase line from cursor to the end of line

	ESC[2K       Erase entire line

	ESC[1;24r    Enable scrolling from start to row end

	ESC[?6l      Reset mode screen with options 640 x 200 monochrome (graphics)

	ESC[?7l      Disable line wrapping

	ESC[2J       Code erase display



	HP ProCurve's, Cisco SG300, and F5 LTM's require this (possible others)

	"""

	debug = False

	if debug:

		print("In strip_ansi_escape_codes")

		print("repr = %s "% repr(string_buffer))



	code_position_cursor = chr(27)+ r'\[\d+;\d+H'

	code_show_cursor =chr(27)+ r'\[\?25h'

	code_next_line =chr(27)+ r'E'

	code_erase_line_end =chr(27)+ r'\[K'

	code_erase_line =chr(27)+ r'\[2K'

	code_erase_start_line =chr(27)+ r'\[K'

	code_enable_scroll =chr(27)+ r'\[\d+;\d+r'

	code_form_feed =chr(27)+ r'\[1L'

	code_carriage_return =chr(27)+ r'\[1M'

	code_disable_line_wrapping =chr(27)+ r'\[\?7l'

	code_reset_mode_screen_options =chr(27)+ r'\[\?\d+l'

	code_erase_display =chr(27)+ r'\[2J'

	code_erase_nokia =r'\-?'+ chr(27)+ r'\[1D'+ r'[\\\|\/\s]?'

	code_erase_nokia2 =' ' + chr(27)+ r'\[1D'

	code_erase_nokia3 =r'[ ]{2,}' + chr(27)+ r'\[74C'+ chr(27)+ r'\[1A' + r'[\s]?'

	code_erase_nokia4 =r'[ ]{2,}' + chr(27)+ r'\[6D'


	code_set = [code_position_cursor, code_show_cursor, code_erase_line, code_enable_scroll,

				code_erase_start_line, code_form_feed, code_carriage_return,

				code_disable_line_wrapping, code_erase_line_end,

				code_reset_mode_screen_options, code_erase_display,code_erase_nokia,
			   
				code_erase_nokia2,code_erase_nokia3, code_erase_nokia4 ]



	output = string_buffer

	for ansi_esc_code in code_set:

		output = re.sub(ansi_esc_code,'', output)



	# CODE_NEXT_LINE must substitute with '\n'

	output = re.sub(code_next_line,'\n', output)



	if debug:

		print("new_output = %s"% output)

		print("repr = %s"% repr(output))



	return output

###########################
###########Below Section we will run expect on the server to collect the info of the NELT-B ports
###########This collection will be done on both cli and T&D 

ip1 = '10.117.97.93'
user1 = 'isadmin'
password1 = 'ANS@123'
port1 = '11130'
#~
call('chmod 777 first_set_of_commands.sh',shell=True)
with open ('outputfile1.txt','w')as f1:
	set1= check_output(['./first_set_of_commands.sh',ip1, user1 ,password1,port1],universal_newlines=True)
	set1clean = (strip_ansi_escape_codes(set1))
	f1.write(set1clean)

NELT_BCards = re.findall(r'(\b(11[01][0123456789abcdef])\s+:\s+NELT-B\b)',set1)
commands_to_nelt=[]
for nelt in NELT_BCards:
	commands_to_nelt+=['login board '+str(nelt[1])]
print('~'*79+'\n')
print('The Following NELT-B boards were found and will be logged in by T&D')	
print(commands_to_nelt)

############This section will create an expect script that connects to each NELT-B card.

open('second_set_of_commands.sh', 'w').close()
with open ('second_set_of_commands.sh','a') as f2:
	f2.write('''#!/usr/bin/expect -f
set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set port [lindex $argv 3]
set timeout 120

spawn ssh -c aes128-cbc $user@$ip -p $port

expect {
	"assword:" {
		send "$password\\r"
	}
	"yes/no" {
		send "yes\\r"
	}
}
expect "shell]>"
''')
	for board in commands_to_nelt:
		f2.write('send "'+board+'\\r"')
		f2.write('''
sleep 3
send "\\r"
expect "shell]>"
send "\\r"
expect "shell]>"
send "bcmx\\r"
expect "bcmx>"
send "0 phy ge0\\r"
expect "bcmx>"
send "0 phy ge2\\r"
expect "bcmx>"
send "0 phy ge4\\r"
expect "bcmx>"
send "0 phy ge6\\r"
expect "bcmx>"
send "0 phy ge8\\r"
expect "bcmx>"
send "0 phy ge10\\r"
expect "bcmx>"
send "0 phy ge12\\r"
expect "bcmx>"
send "0 phy ge14\\r"
expect "bcmx>"
send "0 phy ge16\\r"
expect "bcmx>"
send "1 phy ge0\\r"
expect "bcmx>"
send "1 phy ge2\\r"
expect "bcmx>"
send "1 phy ge4\\r"
expect "bcmx>"
send "1 phy ge6\\r"
expect "bcmx>"
send "1 phy ge8\\r"
expect "bcmx>"
send "1 phy ge10\\r"
expect "bcmx>"
send "1 phy ge12\\r"
expect "bcmx>"
send "1 phy ge14\\r"
expect "bcmx>"
send "1 phy ge16\\r"
expect "bcmx>"
send "exit\\r"
expect "]>"
send "exit\\r"
expect "]>"
''')
	f2.write('''
send "exit\\r"
interact''')
print('Checking Ports Status')
#~
call('chmod 777 second_set_of_commands.sh',shell=True)

with open ('outputfile1.txt','a') as f2:
	set2= check_output(['./second_set_of_commands.sh',ip1, user1 ,password1,port1],universal_newlines=True)
	set2clean = (strip_ansi_escape_codes(set2))
	f2.write(set2clean)

print('~'*79+'\n')
print('Processing the T&D output')
print('~'*79+'\n')
print('\n')
print('Below is the Registers output and the NELT-B ports status\n')


##############################Below section will be processing the output of the cli and the T&D to get
##Two csv files one with the registers hexa values, and one with readable output 
#along with commands needed to delete SAS, lock/unlock the ports that were up, and modify the auto-neg on the ports that needs that.

######Functions
def convert_to_card(x):
	expr = r'(11([01][0123456789abcdef]))'
	num = re.findall(expr, x)
	y = str(int(num[0][1],16)-2)
	return y

def convert_to_port_num(x):
	expr = r'(\b([01]) phy ge(\d*[02468]))'
	num = re.findall(expr, x)
	if str(num[0][1])=='0':
		y = str(int(num[0][2])+1)
	elif str(num[0][1])=='1':
		y = str(int(num[0][2])+19)
	return y

def hex_to_bin(my_hexdata,num_of_bits):
	result =  bin(int(my_hexdata, 16))[2:].zfill(num_of_bits)
	return result


###################### Below is the processing of the file obtained by cli and T&D
filename = 'outputfile1.txt'
with open(filename,'r') as f:
	reading =  f.read()
	
#####Regular expressions	
	Card_num_expr =r'(\{lt0x(11[01][0123456789abcdef]))\}\[USR0-shell\]bcmx>(\b[01] phy ge\d*[02468]\b)'
	port_num_expr = r'((\b[01] phy ge\d*[02468]\b))'
	reg_0_expr = r'((\b0x00: (\S+\b))\s+0x01:)'
	reg_1_expr = r'((\b0x01: (\S+\b))\s+0x02:)'
	reg_5_expr = r'((\b0x05: (\S+\b))\s+0x06:)'
	reg_11_expr = r'((\b0x11: (\S+\b))\s+0x12:)'

	sas_expr = r'(configure ethernet line 1/1/\d+/\d*[13579]\s.+speed-auto-sense\b)'
	up_expr = r'(configure ethernet line 1/1/\d+/\d*[13579]\s.+power up\b)'
	
	
####lists from the regular expression on the input file
	list_of_LTs = re.findall(Card_num_expr, reading)
	list_of_port_num = re.findall(port_num_expr,reading)
	list_of_reg0 = re.findall(reg_0_expr, reading)
	list_of_reg1 = re.findall(reg_1_expr, reading)
	list_of_reg5 = re.findall(reg_5_expr, reading)
	list_of_reg11 = re.findall(reg_11_expr, reading)
	list_sas_ports = re.findall(sas_expr, reading)
	list_up_ports = re.findall(up_expr, reading)


#########Here we will get a list of registers in HEXA from the T&D
output = ''

for a,b,c,d,e,f in zip (list_of_LTs,list_of_port_num,list_of_reg0,list_of_reg1,list_of_reg5,list_of_reg11):
	output += (('1/1/'+convert_to_card(a[1])+'/'+convert_to_port_num(b[0])+','+c[2]+','+d[2]+','+e[2]+','+f[2])+'\n')

######Here we will convert the HEXA to binary 
output1 = ''	
for a,b,c,d,e,f in zip (list_of_LTs,list_of_port_num,list_of_reg0,list_of_reg1,list_of_reg5,list_of_reg11):
	output1 += (('1/1/'+convert_to_card(a[1])+'/'+convert_to_port_num(b[0])+','+hex_to_bin(c[2],16)+','+hex_to_bin(d[2],16)+','+e[2]+','+f[2])+'\n')


#####Here we are creating a list of ports that were configured with speed auto snese and another list for admin up ports
list_sas_ports_portnumber = []
for sas_line in list_sas_ports:
	list_sas_ports_portnumber +=re.findall(r'\b1/1/\d+/\d+\b',sas_line)

list_up_ports_portnumber = []
for up_line in list_up_ports:
	list_up_ports_portnumber +=re.findall(r'\b1/1/\d+/\d+\b',up_line)


############Below section will give us the readable values and the needed commands to remove SAS, lock/Unlock the ports, match auto-neg for unmatching ports.
readable = ""
output_readable1 = output1.split('\n')
output_readable1.remove('')

for line in output_readable1:
	if line.split(',')!=['']:

		lineNumber = line.split(',')[0]
		ANonPort = line.split(',')[1][-13]
		PeerAN = line.split(',')[3]
		AdminStatus = line.split(',')[1][-12]
		OpStatus = line.split(',')[2][-3]
		PDStatus = line.split(',')[4]
		ANnokia = ("Disabled" if ANonPort==str(0) else "Enabled")
		ANpeer = ("Disabled" if PeerAN<='0x4000' else "Enabled")
		if ANnokia=="Disabled" and ANpeer=="Enabled":
			align = "configure ethernet line "+lineNumber+" mau 1 autonegotiate cap1000base"
		else:
			align= ""

	if lineNumber in list_up_ports_portnumber:
		if lineNumber in list_sas_ports_portnumber:
			readable += (lineNumber +','+ANnokia+','+ANpeer+','+("Match" if ANnokia == ANpeer else "Mismatch")+','+("UP")+','+("UP" if OpStatus==str(1) else "Down")+','+("Enabled" if PDStatus!='0x0006' else "Disabled")+','+'SAS Enabled'+','+'configure ethernet line '+lineNumber+' mau 1 no speed-auto-sense'+','+'configure ethernet line '+lineNumber+' no admin-up'+','+'configure ethernet line '+lineNumber+' admin-up'+','+align+'\n')
		else:
			readable += (lineNumber +','+ANnokia+','+ANpeer+','+("Match" if ANnokia == ANpeer else "Mismatch")+','+("UP")+','+("UP" if OpStatus==str(1) else "Down")+','+("Enabled" if PDStatus!='0x0006' else "Disabled")+','+'SAS Disabled'+','+','+'configure ethernet line '+lineNumber+' no admin-up'+','+'configure ethernet line '+lineNumber+' admin-up'+','+align+'\n')
	else:
		if lineNumber in list_sas_ports_portnumber:
			readable += (lineNumber +','+ANnokia+','+ANpeer+','+("Match" if ANnokia == ANpeer else "Mismatch")+','+("Down")+','+("UP" if OpStatus==str(1) else "Down")+','+("Enabled" if PDStatus!='0x0006' else "Disabled")+','+'SAS Enabled'+','+'configure ethernet line '+lineNumber+' mau 1 no speed-auto-sense'+'\n')
		else:
			readable += (lineNumber +','+ANnokia+','+ANpeer+','+("Match" if ANnokia == ANpeer else "Mismatch")+','+("Down")+','+("UP" if OpStatus==str(1) else "Down")+','+("Enabled" if PDStatus!='0x0006' else "Disabled")+','+'SAS Disabled'+'\n')

#########Two files will be created one with the HEXA registers values, and one readable.
print('PortNumber'+','+'reg0'+','+'reg1'+','+'reg5'+','+'reg11')
print(output)
print('PortNumber'+','+'AN on Port'+','+'Peer AN'+','+'AN Matching?'+','+'Admin Status'+','+'Operational Status'+','+'PD status'+','+'SAS Status'+','+'SAS correction'+','+'Port Admin Down'+','+'Port Admin UP'+','+'Align Port')
print(readable)
with open (filename+'_Hexa.csv','w') as csv_file1 , open (filename+'_Readable.csv','w') as csv_file2:
	csv_file1.write('PortNumber'+','+'reg0'+','+'reg1'+','+'reg5'+','+'reg11'+'\n')
	csv_file1.write(output)
	csv_file2.write('PortNumber'+','+'AN on Port'+','+'Peer AN'+','+'AN Matching?'+','+'Admin Status'+','+'Operational Status'+','+'PD status'+','+'SAS Status'+','+'SAS correction'+','+'Port Admin Down'+','+'Port Admin UP'+','+'Align Port'+'\n')
	csv_file2.write(readable)
