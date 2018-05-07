#!/bin/sh
libreoffice --headless --convert-to pdf $1
convert $2.pdf $2.jpg
mkdir $2
mv $2*.jpg ./$2
feh -Y -x -q -D $3 -B black -F -Z -r ./$2
