import pyfits
import os
import sys

execfile('/home/rumbaugh/slit_name_dict_master.py')

def delineate_slits(data,exp_num=None):
    slitbnds = None
    #remove outliers and sum over x
    data_xavg = np.zeros(np.shape(data)[0])
    for idx in range(0,len(data_xavg)): 
        dxsort = np.sort(data[idx,:])
        data_xavg[idx] = np.sum(np.fabs(dxsort[100:len(dxsort)-100]))
    #first, find all local minima (<= within 3 pixels)
    isLM = np.zeros(len(data_xavg))
    for iisLM in range(4,len(isLM)-4):
        if ((np.argsort(data_xavg[iisLM-3:iisLM+4])[0] == 3) | (data_xavg[iisLM] == data_xavg[iisLM+np.argsort(data_xavg[iisLM-3:iisLM+4])[0]-3])): isLM[iisLM] = 1
    glm = np.where(isLM == 1)[0] 
    #if there are groups with equal local minima within 3 pixels, choose one
    ifg = 0
    while ifg < len(glm)-1:
        if glm[ifg+1]-glm[ifg] <= 3:
            equal_inds = np.array([ifg,ifg+1])
            ifgt = ifg+1
            if ifgt < len(glm)-2:
                while ((glm[ifgt+1] - glm[ifgt] <= 3) & (ifgt < len(glm)-2)):
                    equal_inds = np.append(equal_inds,ifgt+1)
                    ifgt += 1
                if ifgt == len(glm)-2:
                    if glm[ifgt+1] - glm[ifgt] <= 3: equal_inds = np.append(equal_inds,ifgt+1)
            keep_ind = int(len(equal_inds)/2-1)
            remove_inds = np.delete(equal_inds,keep_ind)
            glm = np.delete(glm,remove_inds)
        ifg += 1
    #find the right minima (find lowest of: value^2 divided by adjacent slopes)
    adj_slopes = np.zeros(len(glm))
    for ias in range(0,len(glm)):
        adj_slopes[ias] = 0.5*(data_xavg[glm[ias]-3]-data_xavg[glm[ias]]+data_xavg[glm[ias]+3]-data_xavg[glm[ias]])/6
    gslopenot0 = np.where(adj_slopes > 0)[0]
    if exp_num != None:
        right_minima_args = np.argsort((data_xavg[glm[gslopenot0]])**2/adj_slopes[gslopenot0])[0:exp_num-1]
    else:
        sys.exit("Enter a value for exp_num")
    #Now put them in the right order
    right_minima = np.sort(glm[gslopenot0[right_minima_args]])
    for irma in range(0,exp_num-1):
        if irma == 0:
            slitbnds = np.array([[0,right_minima[irma]-1]])
        else:
            slitbnds = np.concatenate((slitbnds,np.array([[right_minima[irma-1]+1,right_minima[irma]-1]])))
    slitbnds = np.concatenate((slitbnds,[[right_minima[irma]+1,len(data_xavg)-1]]))
    return slitbnds
        

for mask in ['1131m3']:
    osv = os.system("mkdir -p %s%s"%(slit_name_dict[mask]['redux_dir'],mask))
    for color  in ['red']:
        for side in ['top']:
            hdu = pyfits.open("%s%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,color,side))
            slitbnds = delineate_slits(hdu[0].data,exp_num=len(slit_name_dict[mask][color][side]))
            if np.shape(slitbnds)[0] != len(slit_name_dict[mask][color][side]):
                sys.exit('Not enough slits found (%i) for %s %s %s side'%(np.shape(slitbnds)[0],mask,color,side))
            for isl in range(0,np.shape(slitbnds)[0]):
                hdutmp = pyfits.open("%s%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,color,side))
                hdutmp[0].data = hdutmp[0].data[slitbnds[isl][0]:slitbnds[isl][1]+1,:]
                hdutmp.writeto("%s%s/%s_%s_%s_%s_coadd_bgsub.fits"%(slit_name_dict[mask]['redux_dir'],mask,mask,slit_name_dict[mask][color][side][isl],color,side),clobber=True)
