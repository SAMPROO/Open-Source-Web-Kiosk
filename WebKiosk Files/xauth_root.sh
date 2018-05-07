#!/bin/bash
touch /root/.Xauthority
xauth merge /home/pi/.Xauthority
export XAUTHORITY=/root/.Xauthority
