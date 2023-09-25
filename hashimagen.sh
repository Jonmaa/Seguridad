#!/bin/bash

OG=$1
CARPETA=$2

echo $1

echo "Original"
for nombreFoto in `ls ./$CARPETA`
do
	RES=$(md5sum ./$CARPETA/$nombreFoto | head -c 32)

	if [ $RES = $OG ]; then
		echo "$nombreFoto"
		exit 0
	fi
done
exit 1
