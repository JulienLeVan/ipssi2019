# Permet de regarder si un fichier "efface_moi" existe et l'efface, sinon affiche "Nothing to do"

file="efface_moi"

if [ -e "$file" ]; then 
	rm $file
else
	echo "nothing to do"
fi

exit
