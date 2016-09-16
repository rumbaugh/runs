execfile('/home/rumbaugh/X-ray_lum_limit.py')
import time
date='7.10.16'

zrange=np.arange(0.65,1.28,0.05)

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
targets=np.array(["cl1324_north","cl1324_south","rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","rxj1821","cl1137","rxj1716","rxj1053"])
st=time.time()
times=np.zeros(len(targets)+1)
times[0]=st
for target,it in zip(targets,np.arange(0,len(targets))):
    Xll=Xray_lum_lim(target)
    Xout,Xout_obs=Xll.calc_lum_lims(100000)
    for band,ib in zip(['soft','hard','full'],np.arange(0,3)):
        outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit.%s.dat'%(target,target,target,band,date)
        np.savetxt(outfile,Xout[ib])
        outfile='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_%s.X-ray_lum_limit_obs.%s.dat'%(target,target,target,band,date)
        np.savetxt(outfile,Xout_obs[ib])
    times[it+1]=time.time()
    print 'Done with %s. This run took %.1f seconds.\nTotal time elapsed: %.1f seconds.\nETA: %.1f seconds.'%(target,times[it+1]-times[it],times[it+1]-st,(times[it+1]-st)/(it+1)*(len(targets)-(it+1)))
