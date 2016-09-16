import pyfits
import os

execfile('/home/rumbaugh/slit_name_dict_master.py')

def delineate_slits(data):
    slitbnds = None
    chipendflag,Y = 0,0
    while Y < np.shape(data)[0]-1:
        while ((np.sum(np.fabs(hdu[0].data[Y,:])) < 0.1) & (Y < np.shape(data)[0]-1)):
            Y += 1
        slitLbndtmp = Y 
        while ((np.sum(np.fabs(hdu[0].data[Y,:])) > 0.1) & (Y < np.shape(data)[0]-1)):
            Y += 1
        slitUbndtmp = Y
        if slitbnds == None:
            slitbnds = np.array([[slitLbndtmp,slitUbndtmp]])
        elif Y < np.shape(data)[0]-1:
            slitbnds = np.concatenate((slitbnds,np.array([[slitLbndtmp,slitUbndtmp]])))
    return slitbnds
        

for mask in ['1131m3']:
    osv = os.system("mkdir -p %s%s"%(slit_name_dict[mask]['redux_dir'],mask))
    for color  in ['red']:
        for side in ['top']:
            hdu = pyfits.open("%s%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,color,side))
            slitbnds = delineate_slits(hdu[0].data)
            if np.shape(slitbnds)[0] != len(slit_name_dict[mask][color][side]):
                sys.exit('Not enough slits found (%i) for %s %s %s side'%(np.shape(slitbnds)[0],mask,color,side))
            for isl in range(0,np.shape(slitbnds)[0]):
                hdutmp = pyfits.open("%s%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,color,side))
                hdutmp[0].data = hdutmp[0].data[slitbnds[isl][0]:slitbnds[isl][1]+1,:]
                hdutmp.writeto("%s%s/%s_%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,mask,slit_name_dict[mask][color][side][isl],color,side))
