execfile('/home/rumbaugh/X-ray_lum_limit.py')
import time
date='7.5.16'

zrange=np.array([0.775,0.83,0.91])

CHrad_dict={'cl0023':5*487.805/4,'rxj1716':7*487.805/4}

targets=np.array(["cl0023","rxj1716"])
st=time.time()
times=np.zeros(len(targets)+1)
times[0]=st
for target,it in zip(targets,np.arange(0,len(targets))):
    CHrad=CHrad_dict[target]
    Xll=Xray_lum_lim(target)
    Xout,Xout_obs=Xll.calc_lum_lims(100000)
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,date)
        np.savetxt(outfile,Xout[ib])
        outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,date)
        np.savetxt(outfile,Xout_obs[ib])
    times[it+1]=time.time()
    print 'Done with %s. This run took %.1f seconds.\nTotal time elapsed: %.1f seconds.\nETA: %.1f seconds.'%(target,times[it+1]-times[it],times[it+1]-st,(times[it+1]-st)/(it+1)*(len(targets)-(it+1)))
target='cl0023'
CHrad=CHrad_dict['rxj1716']
Xll=Xray_lum_lim(target)
Xout,Xout_obs=Xll.calc_lum_lims(100000)
for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
    outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,date)
    np.savetxt(outfile,Xout[ib])
    outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.CHrad_%i.%s.dat'%(target,target,target,band,CHrad,date)
    np.savetxt(outfile,Xout_obs[ib])
