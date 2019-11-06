if [ -z $1 ] || curl -s -I $1 >/dev/null ;then
	echo "OK"
else
	echo "FAIL"
fi

exit
