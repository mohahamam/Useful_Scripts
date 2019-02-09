#!/usr/bin/expect -f

set ip [lindex $argv 0]
set user [lindex $argv 1]
set password [lindex $argv 2]
set port [lindex $argv 3]
set timeout 120

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
expect "#"
send "info configure ethernet line flat\r"
expect "#"
send "show ethernet mau\r"
expect "#"
send "show interface port | match exact:ethernet-line\r"
expect "#"
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

expect "]>"
send "eqpt displayasam -s\r"
expect "]>"
send "login board 1110\r"
expect "shell]>"
send "bcmx\r"
expect "bcmx>"
send "0 phy ge0\r"
expect "bcmx>"
send "0 phy ge2\r"
expect "bcmx>"
send "0 phy ge4\r"
expect "bcmx>"
send "0 phy ge6\r"
expect "bcmx>"
send "0 phy ge8\r"
expect "bcmx>"
send "0 phy ge10\r"
expect "bcmx>"
send "0 phy ge12\r"
expect "bcmx>"
send "0 phy ge14\r"
expect "bcmx>"
send "0 phy ge16\r"
expect "bcmx>"
send "1 phy ge0\r"
expect "bcmx>"
send "1 phy ge2\r"
expect "bcmx>"
send "1 phy ge4\r"
expect "bcmx>"
send "1 phy ge6\r"
expect "bcmx>"
send "1 phy ge8\r"
expect "bcmx>"
send "1 phy ge10\r"
expect "bcmx>"
send "1 phy ge12\r"
expect "bcmx>"
send "1 phy ge14\r"
expect "bcmx>"
send "1 phy ge16\r"
expect "bcmx>"
send "exit\r"
expect "]>"
send "exit\r"
expect "]>"
send "exit\r"

interact

