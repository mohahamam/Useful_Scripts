#!/usr/bin/expect -f

set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set port [lindex $argv 3]
set timeout 20
spawn ssh -c aes128-cbc $user@$ip -p $port

expect "assword:"
send "$password\r"

expect ">#"
puts "sending commands"
send "info configure equipment slot flat\r"

expect ">#"
send "logout\r"


interact