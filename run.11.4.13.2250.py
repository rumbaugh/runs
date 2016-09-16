import numpy as np
import os

execfile('/home/rumbaugh/pythonscripts/make_gallery_Nband_mod.py')

try:
    onlysource
except NameError:
    onlysource = None

nband = 3

infiles = ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J073728.44+321618.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']

panel_dict = {'SDSS-J025245.21+003958.3': {'bands': ['F390W',None,'F814W'], 'ralist': (2.+(52.+((45+np.array([0.215,0.00,0.184]))/60))/60)*360./24, 'declist': 0.+(39.+(58+np.array([0.32,0.00,0.22]))/60)/60, 'sighi': [15., 40., 30.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J025245.21+003958.3.pf_0.60.fs_0.030.10.9.13_drz_sci.fits',None,'/mnt/data2/rumbaugh/HST/10886/drizzled/ADrizOut.HST.SDSSJ0252+0039_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J073728.44+321618.6': {'bands': ['F390W','F555W','F814W'], 'ralist': (7.+(37.+((28.4+np.array([0.072,0.05,0.05]))/60))/60)*360./24, 'declist': 32+(16.+(17+np.array([0.92,2.5,2.5]))/60)/60, 'sighi': [10., 20., 20.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J073728.44+321618.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0541-51959-145_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J090315.19+411609.2': {'bands': ['F390W',None,'F814W'], 'ralist': (9.+(3.+((15.+np.array([0.245,0.00,0.186]))/60))/60)*360./24, 'declist': 41+(16.+(8.+np.array([0.63,0.00,0.99]))/60)/60, 'sighi': [8., 40., 8.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J090315.19+411609.2.pf_0.60.fs_0.030.10.9.13_drz_sci.fits',None,'/mnt/data2/rumbaugh/HST/10886/drizzled/ADrizOut.HST.SDSSJ0903+4116_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J091205.31+002901.1': {'bands': ['F390W','F555W','F814W'], 'ralist': (9.+(12.+((5.+np.array([0.359,0.214,0.214]))/60))/60)*360./24, 'declist': 0.+(29.+(0.+np.array([0.85,1.51,1.51]))/60)/60, 'sighi': [8., 8., 20.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J091205.31+002901.1.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0472-51955-429_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0472-51955-429_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J095629.78+510006.6': {'bands': ['F390W','F555W','F814W'], 'ralist': (9.+(56.+((29.+np.array([0.782,0.608,0.608]))/60))/60)*360./24, 'declist': 51.+(0.+(6.+np.array([0.56,0.67,0.67]))/60)/60, 'sighi': [15., 10., 10.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J095629.78+510006.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0902-52409-068_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0902-52409-068_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J095944.07+041017.0': {'bands': ['F390W','F555W','F814W'], 'ralist': (9.+(59.+((44.+np.array([0.107,0.073,0.073]))/60))/60)*360./24, 'declist': 4.+(10.+(16.+np.array([0.83,1.46,1.46]))/60)/60, 'sighi': [15., 10., 10.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J095944.07+041017.0.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0572-52289-495_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0572-52289-495_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J143004.10+410557.1': {'bands': ['F390W',None,'F814W'], 'ralist': (14.+(30.+((4.+np.array([0.134,0.00,0.057]))/60))/60)*360./24, 'declist': 41.+(5.+(56.+np.array([0.48,0.00,1.29]))/60)/60, 'sighi': [20., 40., 10.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J143004.10+410557.1.pf_0.60.fs_0.030.10.9.13_drz_sci.fits',None,'/mnt/data2/rumbaugh/HST/10886/drizzled/ADrizOut.HST.SDSSJ1430+4105_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J162746.44-005357.5': {'bands': ['F390W','F555W','F814W'], 'ralist': (16.+(27.+((46.+np.array([0.445,0.403,0.403]))/60))/60)*360./24, 'declist': 0.-(53.+(57.+np.array([0.59,0.40,0.40]))/60)/60, 'sighi': [15., 10., 10.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J162746.44-005357.5.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0364-52000-084_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0364-52000-084_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J163028.16+452036.2': {'bands': ['F390W','F555W','F814W'], 'ralist': (16.+(30.+((28.+np.array([0.187,0.219,0.219]))/60))/60)*360./24, 'declist': 45.+(20.+(35.+np.array([0.75,1.32,1.32]))/60)/60, 'sighi': [10., 7., 7.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J163028.16+452036.2.pf_0.60.fs_0.030.10.9.13_drz_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0626-52057-518_F555W_CLEAR2L.pf_1.00.fs_0.030.10.16.13_drc_sci.fits','/mnt/data2/rumbaugh/HST/10494/drizzled/ADrizOut.HST.GAL-0626-52057-518_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J234111.57+000018.6': {'bands': ['F390W',None,'F814W'], 'ralist': (23.+(41.+((11.+np.array([0.443,0.00,0.553]))/60))/60)*360./24, 'declist': 0.+(0.+(18.+np.array([-0.03,0.00,0.28]))/60)/60, 'sighi': [10., 40., 7.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J234111.57+000018.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits',None,'/mnt/data2/rumbaugh/HST/10886/drizzled/ADrizOut.HST.SDSSJ2341+0000_CLEAR1L_F814W.pf_1.00.fs_0.030.10.16.13_drc_sci.fits']},
'SDSS-J095629.68+510210.3': {'bands': ['F390W',None,None], 'ralist': (9.+(56.+((29.+np.array([0.68,0.608,0.608]))/60))/60)*360./24, 'declist': 51.+(2.+(10.+np.array([0.26,0.,0.]))/60)/60, 'sighi': [15., 40., 40.], 'infiles': ['/mnt/data2/rumbaugh/HST/12898/drizzled/ADrizOut.HST.SDSS-J095629.78+510006.6.pf_0.60.fs_0.030.10.9.13_drz_sci.fits',None,None]}}

panel_arr = np.zeros(len(panel_dict),dtype=[('fullname','S20'), ('root','S20'), ('infiles','S150',nband),
          ('band','S5',nband), ('ra',float,nband), ('dec',float,nband), 
          ('sighi',float,nband)])

for source,i in zip(np.sort(panel_dict.keys()),np.arange(len(panel_dict))):
    infiles = panel_dict[source]['infiles']
    ralist,declist = panel_dict[source]['ralist'],panel_dict[source]['declist']
    band = panel_dict[source]['bands']
    sighi = panel_dict[source]['sighi']
    
    print source
    shortname = source[5:10]
    if shortname == 'J0956': shortname = '%s+%s'%(source[5:10],source[16:20])
    panel_arr[i] = (source,shortname,(infiles[0],infiles[1],infiles[2]),(band[0],band[1],band[2]),(ralist[0],ralist[1],ralist[2]),(declist[0],declist[1],declist[2]),(sighi[0],sighi[1],sighi[2]))
    #if ((onlysource == None) | ((onlysource != None) & (onlysource == source))): execfile('/home/rumbaugh/pythonscripts/make_3panel_mod.py')
outfile = 'multipanel_poststamps_gallery.11.4.13.ps'
make_gallery_Nband(panel_arr,outfile=outfile,panelsize=1.8)
