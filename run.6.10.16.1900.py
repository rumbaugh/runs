execfile('/home/rumbaugh/X-ray_lum_limit.py')
import time

st=time.time()
Xll=Xray_lum_lim('cl0023')
a=Xll.calc_lum_lims(1000)
t1=time.time()
a=Xll.calc_lum_lims(10000)
t2=time.time()

print '1000 trials took %f.1 seconds.\n10000 trials took %f.1 seconds.'%(t1-st,t2-t1)
