#!/bin/bash

sudo apt-get update
sudo apt-get -y install glade
sudo apt-get -y install libgtk-3-dev
sudo apt-get -y install libreoffice
sudo apt-get -y install imagemagick
sudo apt-get -y install xdotool
sudo apt-get -y install feh
sudo apt-get -y install unclutter
sudo apt-get -y install at-spi2-core

mv -f /home/pi/Downloads/WebKiosk/* /home/pi/
mv -f /home/pi/autostart /etc/xdg/lxsession/LXDE-pi/
./python /home/pi/WebKiosk/setup_kiosk2.py
