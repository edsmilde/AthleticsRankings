
# perl -pe 's/^.*3:/3:/' data/raw_1500_alltime.txt | perl -pe 's/,/_/g' > data/raw_1500_alltime_stage1.txt
# grep "^3:" data/raw_1500_alltime_stage1.txt > data/raw_1500_alltime_stage2.txt
# perl -pe 's/\t/,/g' data/raw_1500_alltime_stage2.txt > data/raw_1500_alltime_stage3.txt

# cp data/raw_1500_alltime_stage3.txt data/raw_1500_alltime_final.txt


YEARS=`seq 2016 2021`

for YEAR in $YEARS; do
    cp data/raw_1500_${YEAR}.txt input/raw_1500_${YEAR}.txt
done;


