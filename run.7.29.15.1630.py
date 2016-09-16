import numpy as np
import pyfits as py
import copy
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')
obs_dict = {}
#blue_ID_list = np.array([192,189,190,191,195,196,197,198,199,200,201,366,367,368,369,375,376,377,378])
#red_ID_list = np.array([141,132,133,140,151,158,159,174,175,182,342,343,350,351,369,370,377,378])
blue_ID_list = np.array([193,194,370,371,373,374])
red_ID_list = np.array([142,149,352,353,361,362])

def do_redux(ID,side):
    try:
        data = load_2d_spectrum('/home/rumbaugh/KAST/Science/sci-%s%i.fits.gz'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/Science/sci-%s%i.fits.gz'%(side,ID))
    except:
        data = load_2d_spectrum('/home/rumbaugh/KAST/Science/sci-%s%i.fits'%(side,ID))
        cr = py.open('/home/rumbaugh/KAST/Science/sci-%s%i.fits'%(side,ID))
    invar = cr[1].data
    var = np.copy(invar)
    var[var!=0]=1./var[var!=0]
    var[var==0]=99999.
    print np.shape(var)
    struct = cr[5].data
    #if not(ID in [189,190,191,132,133,140]):
    w=struct['WAVE_OPT'][0]
    fitmp,fixmu,mp_out,bounds_arr,apertures = find_multiple_peaks(data,maxpeaks=3,check_aps=True,dispaxis='y')
    imle=0;dlb_0810,dub_0810 = bounds_arr[2*imle],bounds_arr[2*imle+1]
    mu0_0810,sig0_0810 = find_trace(data[:,dlb_0810:dub_0810+1],dispaxis='y')
    mupoly_0810,sigpoly=trace_spectrum(data[:,dlb_0810:dub_0810+1],mu0_0810,sig0_0810,stepsize=25,dispaxis='y',noblankcolumns=True)
    try: imle=2;dlb,dub = bounds_arr[2*imle],bounds_arr[2*imle+1]
    except: imle=1;dlb,dub = bounds_arr[2*imle],bounds_arr[2*imle+1]
    mu0,sig0 = find_trace(data[:,dlb:dub+1],dispaxis='y')
    mupoly=copy.deepcopy(mupoly_0810)
    mupoly[-1]+=mu0-mu0_0810
    specm,varspec = extract_spectrum(data[:,dlb:dub+1],mupoly,sigpoly,dispaxis='y',var_in=var[:,dlb:dub+1])
    save_spectrum('/home/rumbaugh/KAST/Science/spec.%s%i.dat'%(side,ID),w,specm,var=varspec)

for ID in blue_ID_list: do_redux(ID,'b')
for ID in red_ID_list: do_redux(ID,'r')
