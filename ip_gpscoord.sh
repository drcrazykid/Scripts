#!/bin/bash

OUTPUT_FILE=/tmp/client_location.txt

# Grab public IP address
Public_IP=`curl -s https://ipinfo.io/ip`

# Extract the data from the IP address

curl -s https://ipvigilante.com/$Public_IP | \
	jq '.data.latitude, .data.longitude, .data.ciy_name, .data.country_name' | \
	while read -r LATITUDE; do
		read -r LONGITUDE
		read -r CITY
		read -r COUNTRY

		echo "$LATITUDE, $LONGITUDE, $CITY, $COUNTRY"
		echo "$LATITUDE,$LONGITUDE, $CITY, $COUNTRY" | \
			tr --delete \" > $OUTPUT_FILE
	done
