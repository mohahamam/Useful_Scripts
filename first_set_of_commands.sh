#!/usr/bin/expect -f

set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set port [lindex $argv 3]
set timeout 7200

spawn ssh -c aes128-cbc $user@$ip

expect {
	"assword:" {
		send "$password\r"
	}
	"yes/no" {
		send "yes\r"
	}
}

expect ">#"
puts "sending commands"
send "environment inhibit-alarms\r"
expect "#"
send "exit all\r"
expect ">#"
send "info configure ethernet line flat\r"
expect ">#"
send "show ethernet mau\r"
expect ">#"
send "show interface port\r"
expect ">#"
send "logout\r"


spawn ssh -c aes128-cbc $user@$ip -p $port
expect {
	"assword:" {
		send "$password\r"
	}
	"yes/no" {
		send "yes\r"
	}
}
sleep 1
send "\r"
expect "]>"
send "eqpt displayasam -s\r"
expect "]>"
send "exit\r"

interact
