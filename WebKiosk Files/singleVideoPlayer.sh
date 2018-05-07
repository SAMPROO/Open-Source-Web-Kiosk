#!/bin/sh

VIDEOFILE=$1 
echo $VIDEOFILE
SERVICE="omxplayer"

while true; do
        if ps ax | grep -v grep | grep $SERVICE > /dev/null
	then
	sleep 1;
else
        do
                clear
                omxplayer -b $1 > /dev/null
        done
fi
done