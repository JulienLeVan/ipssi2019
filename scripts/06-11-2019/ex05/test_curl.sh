# Permet de tester le fonctionne d'un site 

if [ -z $1 ] || curl -s -I $1 >/dev/null ;then
	echo "OK"
else
	echo "FAIL"
fi

exit
