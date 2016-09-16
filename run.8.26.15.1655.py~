import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')
obs_dict = {}
#blue_ID_list = np.array([192,189,190,191,195,196,197,198,199,200,201,366,367,368,369,375,376,377,378])
#red_ID_list = np.array([141,132,133,140,151,158,159,174,175,182,342,343,350,351,369,370,377,378])
blue_ID_list = np.array([195,196,197,198,199,200,201,366,367,368,369,375,376,377,378])
red_ID_list = np.array([151,158,159,174,175,182,342,343,350,351,369,370,377,378])

def do_redux(ID,side):
    try:
        data = load_2d_spectrum('/home/rumbaugh/KAST/Science/sci-%s%i.skysub.fits.gz'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/Science/sci-%s%i.skysub.fits.gz'%(side,ID))
    except:
        data = load_2d_spectrum('/home/rumbaugh/KAST/Science/sci-%s%i.skysub.fits'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/Science/sci-%s%i.skysub.fits'%(side,ID))
    crvar=py.open('/home/rumbaugh/KAST/Science/sci-%s%i.var_skysub_CRmask.fits'%(side,ID))
    crw=py.open('/home/rumbaugh/KAST/Science/sci-%s%i.fits'%(side,ID))
    var = crvar[0].data
    if ((side=='r')&(ID==351)):
        var[1107:1111]=9999999
    #var = np.copy(invar)
    #var[var!=0]=1./var[var!=0]
    #var[var==0]=99999.
    #print np.shape(var)
    struct = crw[5].data
    if not(ID in [189,190,191,132,133,140]): w=struct['WAVE_OPT'][0]
    fitmp,fixmu,mp_out,bounds_arr,apertures = find_multiple_peaks(data,maxpeaks=3,check_aps=True,dispaxis='y')
    imle=0;dlb,dub = bounds_arr[2*imle],bounds_arr[2*imle+1]
    mu0,sig0 = find_trace(data[:,dlb:dub+1],dispaxis='y')
    mupoly,sigpoly=trace_spectrum(data[:,dlb:dub+1],mu0,sig0,stepsize=25,dispaxis='y',noblankcolumns=True)
    specm,varspec = extract_spectrum(data[:,dlb:dub+1],mupoly,sigpoly,dispaxis='y',var_in=var[:,dlb:dub+1])
    save_spectrum('/home/rumbaugh/KAST/Science/spec_skysub_noCR.%s%i.dat'%(side,ID),w,specm,var=varspec)

for ID in blue_ID_list: do_redux(ID,'b')
for ID in red_ID_list: do_redux(ID,'r')
