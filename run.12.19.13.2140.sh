rungs=(0 1 2 3 4)
pairs=(double_pair20 double_pair30 double_pair32 double_pair34 double_pair38 double_pair40 double_pair50 quad_pairA quad_pairB)
group=(0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)
for r in ${rungs[*]}
do
for p in ${pairs[*]}
do
for g in ${group[*]}
do
cp /home/rumbaugh/runs/run.12.19.13.2115.py ./temp1.py
echo rung,base,group = $r,\'$p\',$g | tee -a ./temp1.py
echo runtemplate\(base,rung,group\) | tee -a ./temp1.py
echo exit | tee -a ./temp1.py
ipython ./temp1.py
done
done
done