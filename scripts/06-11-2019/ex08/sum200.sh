# Permet de lire les chiffres en entrée et affiche leur somme 

while read n; do
	sum=$(($sum+$n));
done

echo $sum

exit
