import numpy as np
import os

os.chdir('/home/rumbaugh/Chandra/plots')


obs=np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"])
for i in range(0,7):
    os.system('cp /home/rumbaugh/Chandra/plots/z_hist_full.%s.11.10.15.png /home/rumbaugh/Chandra/plots/z_hist_full_%s_11-10-15.png'%(obs[i],obs[i]))

os.chdir('/home/rumbaugh/git/scriptutils/perl')
os.system('perl gallery.pl -o /home/rumbaugh/Chandra/plots/zhists_full.11.16.15.pdf /home/rumbaugh/Chandra/plots/z_hist_full*11-10-15.png -pdf -x 1')
