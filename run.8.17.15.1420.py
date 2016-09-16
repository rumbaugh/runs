import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')

def do_redux(ID,side):
    try:
        data = load_2d_spectrum('/home/rumbaugh/KAST/rusu_run_8.15/Science/sci-%s%i.skysub.fits'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/rusu_run_8.15/Science/sci-%s%i.fits.gz'%(side,ID))
    except:
        data = load_2d_spectrum('/home/rumbaugh/KAST/rusu_run_8.15/Science/sci-%s%i.skysub.fits'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/rusu_run_8.15/Science/sci-%s%i.fits'%(side,ID))
    invar = cr[1].data
    var = np.copy(invar)
    var[var!=0]=1./var[var!=0]
    var[var==0]=99999.
    print np.shape(var)
    struct = cr[5].data
    w=struct['WAVE_OPT'][0]
    fitmp,fixmu,mp_out,bounds_arr,apertures = find_multiple_peaks(data,maxpeaks=3,check_aps=True,dispaxis='y')
    for imle in np.arange(len(bounds_arr)/2):
        imle=imle;dlb,dub = bounds_arr[2*imle],bounds_arr[2*imle+1]
        mu0,sig0 = find_trace(data[:,dlb:dub+1],dispaxis='y')
        mupoly,sigpoly=trace_spectrum(data[:,dlb:dub+1],mu0,sig0,stepsize=25,dispaxis='y',noblankcolumns=True)
        specm,varspec = extract_spectrum(data[:,dlb:dub+1],mupoly,sigpoly,dispaxis='y',var_in=var[:,dlb:dub+1])
        save_spectrum('/home/rumbaugh/KAST/rusu_run_8.15/Science/spec.%s%i_%i.dat'%(side,ID,imle),w,specm,var=varspec)
        figure(5+imle)
        clf()
        smooth_boxcar('/home/rumbaugh/KAST/rusu_run_8.15/Science/spec.%s%i_%i.dat'%(side,ID,imle),10,w_in=w)

