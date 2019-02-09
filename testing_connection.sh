#!/usr/bin/expect -f
#set output [exec hostname]
#puts "Trying to test the connection of the thing"
set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set port [lindex $argv 3]

spawn ssh $user@$ip -p $port
expect "password:"
send "$password\r"
expect "$"
set timeout 20
#puts "Sending command of df -kh"
#send "df -kh\r"
#expect "$"
#send "ifconfig -a\r"
#expect "$"
#send "hostid\r"
#expect "$"
#send "hostname\r"

puts "Sending command of df -kh;ifconfig -a;hostid;hostname;ps -ef;netstat -rn;sudo apt-get update;sudo dmesg"
send "df -kh;ifconfig -a;hostid;hostname;ps -ef;netstat -rn;sudo apt-get update;\r"
#send "sudo apt-get update\r"
expect ":"
send "$password\r"
expect "$"
send "exit\r"

interact

#spawn ssh hamam@i7mini "ifconfig -a"
#expect "password:"
#send "adminadmin\r"
#interact