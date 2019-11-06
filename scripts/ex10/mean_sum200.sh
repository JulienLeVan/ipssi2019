sum=0

while read n;do

        sum=$(($sum+$n));
        n=$(($n+1));
        mean=$(($sum/$n));
done

echo $mean
echo $sum

exit

