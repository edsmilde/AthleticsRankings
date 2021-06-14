
# perl -pe 's/^.*3:/3:/' data/raw_1500_alltime.txt | perl -pe 's/,/_/g' > data/raw_1500_alltime_stage1.txt
# grep "^3:" data/raw_1500_alltime_stage1.txt > data/raw_1500_alltime_stage2.txt
# perl -pe 's/\t/,/g' data/raw_1500_alltime_stage2.txt > data/raw_1500_alltime_stage3.txt

# cp data/raw_1500_alltime_stage3.txt data/raw_1500_alltime_final.txt


YEARS=`seq 2010 2021`

for YEAR in $YEARS; do
    perl -pe 's/^.*3:/3:/' input/raw_1500_${YEAR}.txt | perl -pe 's/,/_/g' > data/raw_1500_${YEAR}_stage1.txt
    grep "^3:" data/raw_1500_${YEAR}_stage1.txt > data/raw_1500_${YEAR}_stage2.txt
    perl -pe 's/\t/,/g' data/raw_1500_${YEAR}_stage2.txt > data/raw_1500_${YEAR}_stage3.txt
    perl -pe "s/(^.*$)/\1 ${YEAR}/" data/raw_1500_${YEAR}_stage3.txt > data/raw_1500_${YEAR}_stage4.txt
    perl -pe 's/(^.*?,.*?,.*?,.*?,.*?,.*?,).*?,(.*$)/\1\2/' data/raw_1500_${YEAR}_stage4.txt > data/raw_1500_${YEAR}_stage5.txt
    cp data/raw_1500_${YEAR}_stage5.txt data/raw_1500_${YEAR}_final.txt
done;


