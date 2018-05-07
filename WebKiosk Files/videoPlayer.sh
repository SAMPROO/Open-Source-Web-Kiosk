#!/bin/sh

VIDEOPATH=$1 
echo VIDEOPATH
SERVICE="omxplayer"

while true; do
        if ps ax | grep -v grep | grep $SERVICE > /dev/null
	then
	sleep 1;
else
        for entry in $VIDEOPATH/*
        do
                clear
                omxplayer -b $entry > /dev/null
        done
fi
done
