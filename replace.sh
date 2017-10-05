ls *.py | while read i;
do
    sed -i '' -e 's/from numeric/from numpy/g' $i
    sed -i '' -e 's/glutCreateWindow(/glutCreateWindow(b/g' $i
done
