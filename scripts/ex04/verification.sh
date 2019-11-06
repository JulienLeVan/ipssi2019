file="efface_moi"

if [ -e "$file" ]; then 
	rm $file
else
	echo "nothing to do"
fi

exit
