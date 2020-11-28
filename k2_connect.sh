#!/bin/bash

refresh_k2_ip () {
	k2_ip=$(sudo nmap -sn 192.168.0.0/24 | grep "B8:27:EB:3D:EE:B0" -B 2 | head -1 | cut -f 5 -d " ")
	echo "$k2_ip" > k2.ip
	echo "$k2_ip"
}


get_k2_ip() {
	cat k2.ip
}

get_k2_pwd() {
	cat k2.key
}


k2 () {
	k2_ip=$(get_k2_ip)
	k2_pwd=$(get_k2_pwd)
	ssh pi@"$k2_ip" -i "$k2_pwd"
}

rek2 () {
	k2_ip=$(refresh_k2_ip)
	k2_pwd=$(get_k2_pwd)
	ssh pi@"$k2_ip" -i "$k2_pwd"
}

k2cp () {
	scp -i $(get_k2_pwd) "$1" pi@$(get_k2_ip):"$2" 
}
