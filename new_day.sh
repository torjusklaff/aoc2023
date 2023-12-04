DAY_NUM=$1

ndir=d$DAY_NUM
if [[ -d $ndir ]]; then
    echo "Day $DAY_NUM already created"
    exit
fi
mkdir $ndir

cp template/* $ndir
mv $ndir/day.py $ndir/day$DAY_NUM.py

curl https://adventofcode.com/2023/day/$DAY_NUM/input --cookie session=$AOC_SESSION -o $ndir/input.txt 