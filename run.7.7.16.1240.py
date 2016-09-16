import numpy as np
import matplotlib.pyplot as plt
adamcorrval=-1.3975614258700002

szlb,szub=0.65,1.28

execfile('/home/rumbaugh/setup_adam_cats.py')
execfile('/home/rumbaugh/set_spec_dict.py')

target_dir={"RCS0224":"rcs0224","SC0849":"cl0849","SC0910":"rxj0910","RXJ1221":"rxj1221","Cl1350":"cl1350","NEP200":"rxj1757","SG0023":"cl0023","SC1324":'cl1324',"NEP5281":"rxj1821","Cl1137":"cl1137","RXJ1716":"rxj1716","RXJ1053":"rxj1053","SC1604":"cl1604","RXJ1821":"rxj1821","RXJ1757":"rxj1757"}


linfile='/home/rumbaugh/X-ray_lum_cat.all_sources.5.31.16.dat'

lindict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crl=np.loadtxt(linfile,dtype=lindict)

sig=np.concatenate((crl['sigS'].reshape((len(crl['sigS']),1)),crl['sigH'].reshape((len(crl['sigH']),1)),crl['sigF'].reshape((len(crl['sigF']),1))),axis=1)
sig=np.max(sig,axis=1)

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.figure(2)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.figure(3)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

allU,allV,allJ=np.zeros(0),np.zeros(0),np.zeros(0)
AGNU,AGNV,AGNJ=np.zeros(0),np.zeros(0),np.zeros(0)
fldU,fldV,fldJ=np.zeros(0),np.zeros(0),np.zeros(0)
fldAGNU,fldAGNV,fldAGNJ=np.zeros(0),np.zeros(0),np.zeros(0)

outall,outAGN=np.zeros((0,12),dtype='object'),np.zeros((0,15),dtype='object')
outfld,outfldAGN=np.zeros((0,12),dtype='object'),np.zeros((0,15),dtype='object')
#outAGN[:,0],outAGN[:,1],outAGN[:,2],outAGN[:,3],outAGN[:,4],outAGN[:,5],outAGN[:,6],outAGN[:,7]=crl['field'],crl['number'],crl['RA'],crl['Dec'],crl['lum_soft'],crl['lum_hard'],crl['lum_full'],crl['redshift']


#for field in reffile_dict.keys():
for field in ['rxj0910','rxj1716','rxj1821','rxj1757','cl0023','cl1604']:
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif ((field=='rxj0910')|(field=='cl1324')):
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.7.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB','mRFV','mRFJ','mRFNUV'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8','f8','f8','f8')})
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if ((field=='rxj0910')|(field=='cl1324')):
        crrf=np.loadtxt(rfcat,dtype=rfdict0910)
    else:
        crrf=np.loadtxt(rfcat,dtype=rfdict)
    RFU,RFB,RFV,RFJ=crrf['restflux_U'],crrf['restflux_B'],crrf['restflux_V'],crrf['restflux_J']
    mRFU,mRFB,mRFV,mRFJ,mRFNUV=cram['mRFU'],cram['mRFB'],cram['mRFV'],cram['mRFJ'],cram['mRFNUV']
    gz_all=np.where((cram['Q']>2.5)&(cram['z_spec']>=fzl)&(cram['z_spec']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFV>-80))[0]
    gz_fld=np.where((cram['Q']>2.5)&(cram['z_spec']>=szlb)&(cram['z_spec']<=szub)&((cram['z_spec']<fzl)|(cram['z_spec']>fzu))&(cr['use']==1)&(mRFB<-20.9)&(mRFV>-80))[0]
    outtmpall,outtmpfld=np.zeros((len(gz_all),12),dtype='object'),np.zeros((len(gz_fld),12),dtype='object')
    outtmpall[:,1],outtmpall[:,2],outtmpall[:,2],outtmpall[:,3]=cram['ID_adam'][gz_all],cram['RA_spec'][gz_all],cram['Dec_spec'][gz_all],cram['z_spec'][gz_all]
    outtmpfld[:,1],outtmpfld[:,2],outtmpfld[:,2],outtmpfld[:,3]=cram['ID_adam'][gz_fld],cram['RA_spec'][gz_fld],cram['Dec_spec'][gz_fld],cram['z_spec'][gz_fld]
    outtmpall[:,0],outtmpfld[:,0]=field,field
    outall=np.concatenate((outall,outtmpall),axis=0)
    outfld=np.concatenate((outfld,outtmpfld),axis=0)

    gf=np.where(crl['field']==field)[0]
    if field=='cl1324':gf=np.where((crl['field']==field)&(crl['field']=='cl1324_north')&(crl['field']=='cl1324_south'))[0]
    glz=np.zeros(len(gf),dtype='i8')
    for j in range(0,len(glz)):
        gtmp=np.where((np.abs(crl['RA'][gf[j]]-cram['RA_xray'])/np.cos(np.pi*crl['Dec'][gf[j]]/180)<3./3600)&(np.abs(crl['Dec'][gf[j]]-cram['Dec_xray'])<3./3600))[0]
        if len(gtmp)>0:
            tmpdist=np.sqrt((crl['RA'][gf[j]]-cram['RA_xray'][gtmp])**2+(crl['Dec'][gf[j]]-cram['Dec_xray'][gtmp])**2)
            glz[j]=gtmp[np.argsort(tmpdist)[0]]
    gz_AGN=np.where((sig[gf]>2)&(cram['Q'][glz]>2.5)&(cram['z_spec'][glz]>=fzl)&(cram['z_spec'][glz]<fzu)&(cr['use'][glz]==1)&(mRFB[glz]<-20.9)&(mRFV[glz]>-80))[0]
    gz_fldAGN=np.where((sig[gf]>2)&(cram['Q'][glz]>2.5)&(cram['z_spec'][glz]>=szlb)&(cram['z_spec'][glz]<=szub)&((cram['z_spec'][glz]<fzl)|(cram['z_spec'][glz]>fzu))&(cr['use'][glz]==1)&(mRFB[glz]<-20.9)&(mRFV[glz]>-80))[0]
    outtmpAGN,outtmpfldAGN=np.zeros((len(gz_AGN),15),dtype='object'),np.zeros((len(gz_fldAGN),15),dtype='object')
    outtmpAGN[:,0],outtmpAGN[:,1],outtmpAGN[:,2],outtmpAGN[:,3],outtmpAGN[:,4],outtmpAGN[:,5],outtmpAGN[:,6],outtmpAGN[:,7]=crl['field'][gf[gz_AGN]],crl['number'][gf[gz_AGN]],crl['RA'][gf[gz_AGN]],crl['Dec'][gf[gz_AGN]],crl['lum_soft'][gf[gz_AGN]],crl['lum_hard'][gf[gz_AGN]],crl['lum_full'][gf[gz_AGN]],crl['redshift'][gf[gz_AGN]]
    outtmpfldAGN[:,0],outtmpfldAGN[:,1],outtmpfldAGN[:,2],outtmpfldAGN[:,3],outtmpfldAGN[:,4],outtmpfldAGN[:,5],outtmpfldAGN[:,6],outtmpfldAGN[:,7]=crl['field'][gf[gz_fldAGN]],crl['number'][gf[gz_fldAGN]],crl['RA'][gf[gz_fldAGN]],crl['Dec'][gf[gz_fldAGN]],crl['lum_soft'][gf[gz_fldAGN]],crl['lum_hard'][gf[gz_fldAGN]],crl['lum_full'][gf[gz_fldAGN]],crl['redshift'][gf[gz_fldAGN]]
    outAGN=np.concatenate((outAGN,outtmpAGN),axis=0)
    outfldAGN=np.concatenate((outfldAGN,outtmpfldAGN),axis=0)

    allU,allV,allJ=np.append(allU,mRFU[gz_all]),np.append(allV,mRFV[gz_all]),np.append(allJ,mRFJ[gz_all])
    AGNU,AGNV,AGNJ=np.append(AGNU,mRFU[glz][gz_AGN]),np.append(AGNV,mRFV[glz][gz_AGN]),np.append(AGNJ,mRFJ[glz][gz_AGN])
    fldU,fldV,fldJ=np.append(fldU,mRFU[gz_fld]),np.append(fldV,mRFV[gz_fld]),np.append(fldJ,mRFJ[gz_fld])
    fldAGNU,fldAGNV,fldAGNJ=np.append(fldAGNU,mRFU[glz][gz_fldAGN]),np.append(fldAGNV,mRFV[glz][gz_fldAGN]),np.append(fldAGNJ,mRFJ[glz][gz_fldAGN])

plt.figure(1)
plt.scatter(allV-allJ,allU-allV,color='b',s=2)
plt.scatter(AGNV-AGNJ,AGNU-AGNV,color='r',s=64)

UV0,VJ0=1.3,1.6
UV1,VJ1=0.88*VJ0+0.59,(UV0-0.59)/0.88

plt.xlim(-1,2.5)
plt.ylim(0,2.5)

xlim=plt.xlim()
ylim=plt.ylim()

xdummy=np.linspace(VJ1,VJ0,10)
plt.plot(xdummy,0.88*xdummy+0.59,color='k',ls='dashed',lw=2)
plt.axhline(UV0,xmax=(VJ1-xlim[0])/(xlim[1]-xlim[0]),color='k',ls='dashed',lw=2)
plt.axvline(VJ0,ymin=(UV1-ylim[0])/(ylim[1]-ylim[0]),color='k',ls='dashed',lw=2)
plt.xlabel('V-J')
plt.ylabel('U-V')
plt.xlim(xlim)
plt.ylim(ylim)
plt.savefig('/home/rumbaugh/Chandra/plots/color-color_plot.V-J_vs_U-V.7.5.16.png')

plt.figure(2)
plt.scatter(fldV-fldJ,fldU-fldV,color='b',s=2)
plt.scatter(fldAGNV-fldAGNJ,fldAGNU-fldAGNV,color='r',s=64)

UV0,VJ0=1.3,1.6
UV1,VJ1=0.88*VJ0+0.59,(UV0-0.59)/0.88

plt.xlim(-1,2.5)
plt.ylim(0,2.5)

xlim=plt.xlim()
ylim=plt.ylim()

xdummy=np.linspace(VJ1,VJ0,10)
plt.plot(xdummy,0.88*xdummy+0.59,color='k',ls='dashed',lw=2)
plt.axhline(UV0,xmax=(VJ1-xlim[0])/(xlim[1]-xlim[0]),color='k',ls='dashed',lw=2)
plt.axvline(VJ0,ymin=(UV1-ylim[0])/(ylim[1]-ylim[0]),color='k',ls='dashed',lw=2)
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel('V-J')
plt.ylabel('U-V')
plt.savefig('/home/rumbaugh/Chandra/plots/color-color_plot.V-J_vs_U-V.field.7.5.16.png')

plt.figure(3)
plt.scatter(fldV-fldJ,fldU-fldV,color='cyan',s=2,label='All field gals')
plt.scatter(allV-allJ,allU-allV,color='b',s=2,label='All structure gals')
plt.scatter(fldAGNV-fldAGNJ,fldAGNU-fldAGNV,color='magenta',s=64,label='Field AGN',marker='d')
plt.scatter(AGNV-AGNJ,AGNU-AGNV,color='r',s=64,label='Structure AGN')

VJall,UVall=allV-allJ,allU-allV
VJfld,UVfld=fldV-fldJ,fldU-fldV
VJAGN,UVAGN=AGNV-AGNJ,AGNU-AGNV
VJfldAGN,UVfldAGN=fldAGNV-fldAGNJ,fldAGNU-fldAGNV

UV0,VJ0=1.3,1.6
UV1,VJ1=0.88*VJ0+0.59,(UV0-0.59)/0.88

plt.xlim(-1,2.5)
plt.ylim(0,2.5)

xlim=plt.xlim()
ylim=plt.ylim()

xdummy=np.linspace(VJ1,VJ0,10)
plt.plot(xdummy,0.88*xdummy+0.59,color='k',ls='dashed',lw=2)
plt.axhline(UV0,xmax=(VJ1-xlim[0])/(xlim[1]-xlim[0]),color='k',ls='dashed',lw=2)
plt.axvline(VJ0,ymin=(UV1-ylim[0])/(ylim[1]-ylim[0]),color='k',ls='dashed',lw=2)
plt.xlim(xlim)
plt.ylim(ylim)
plt.xlabel('V-J')
plt.ylabel('U-V')
plt.legend(loc='upper left')
plt.savefig('/home/rumbaugh/Chandra/plots/color-color_plot.V-J_vs_U-V.field_comp.7.5.16.png')

cos0,sin0=1/np.sqrt(1+0.88**2),0.88/np.sqrt(1+0.88**2)
def calc_uv(x,y):
    u,v=cos0*x+sin0*y,cos0*y-sin0*x
    return u,v
u0,v0=calc_uv(VJ1,UV0)
u1,v0=calc_uv(VJ0,UV1)
uall,vall=calc_uv(VJall,UVall)
uAGN,vAGN=calc_uv(VJAGN,UVAGN)
ufld,vfld=calc_uv(VJfld,UVfld)
ufldAGN,vfldAGN=calc_uv(VJfldAGN,UVfldAGN)

color_offset_all,color_offset_AGN,color_offset_fld,color_offset_fldAGN=np.zeros(len(uall)),np.zeros(len(uAGN)),np.zeros(len(ufld)),np.zeros(len(ufldAGN))
color_offset_all[VJall<=VJ1],color_offset_AGN[VJAGN<=VJ1],color_offset_fld[VJfld<=VJ1],color_offset_fldAGN[VJfldAGN<=VJ1]=UV0-UVall[VJall<=VJ1],UV0-UVAGN[VJAGN<=VJ1],UV0-UVfld[VJfld<=VJ1],UV0-UVfldAGN[VJfldAGN<=VJ1]
color_offset_all[UVall>=UV1],color_offset_AGN[UVAGN>=UV1],color_offset_fld[UVfld>=UV1],color_offset_fldAGN[UVfldAGN>=UV1]=-VJ0+VJall[UVall>=UV1],-VJ0+VJAGN[UVAGN>=UV1],-VJ0+VJfld[UVfld>=UV1],-VJ0+VJfldAGN[UVfldAGN>=UV1]
color_offset_all[((uall>=u0)&(uall<=u1))],color_offset_AGN[((uAGN>=u0)&(uAGN<=u1))],color_offset_fld[((ufld>=u0)&(ufld<=u1))],color_offset_fldAGN[((ufldAGN>=u0)&(ufldAGN<=u1))]=v0-vall[((uall>=u0)&(uall<=u1))],v0-vAGN[((uAGN>=u0)&(uAGN<=u1))],v0-vfld[((ufld>=u0)&(ufld<=u1))],v0-vfldAGN[((ufldAGN>=u0)&(ufldAGN<=u1))]
color_offset_all[((VJall>VJ1)&(uall<u0))],color_offset_AGN[((VJAGN>VJ1)&(uAGN<u0))],color_offset_fld[((VJfld>VJ1)&(ufld<u0))],color_offset_fldAGN[((VJfldAGN>VJ1)&(ufldAGN<u0))]=np.sqrt((VJ1-VJall[((VJall>VJ1)&(uall<u0))])**2+(UV0-UVall[((VJall>VJ1)&(uall<u0))])**2),np.sqrt((VJ1-VJAGN[((VJAGN>VJ1)&(uAGN<u0))])**2+(UV0-UVAGN[((VJAGN>VJ1)&(uAGN<u0))])**2),np.sqrt((VJ1-VJfld[((VJfld>VJ1)&(ufld<u0))])**2+(UV0-UVfld[((VJfld>VJ1)&(ufld<u0))])**2),np.sqrt((VJ1-VJfldAGN[((VJfldAGN>VJ1)&(ufldAGN<u0))])**2+(UV0-UVfldAGN[((VJfldAGN>VJ1)&(ufldAGN<u0))])**2)
color_offset_all[((UVall<UV1)&(uall>u1))],color_offset_AGN[((UVAGN<UV1)&(uAGN>u1))],color_offset_fld[((UVfld<UV1)&(ufld>u1))],color_offset_fldAGN[((UVfldAGN<UV1)&(ufldAGN>u1))]=np.sqrt((VJ0-VJall[((UVall<UV1)&(uall>u1))])**2+(UV1-UVall[((UVall<UV1)&(uall>u1))])**2),np.sqrt((VJ0-VJAGN[((UVAGN<UV1)&(uAGN>u1))])**2+(UV1-UVAGN[((UVAGN<UV1)&(uAGN>u1))])**2),np.sqrt((VJ0-VJfld[((UVfld<UV1)&(ufld>u1))])**2+(UV1-UVfld[((UVfld<UV1)&(ufld>u1))])**2),np.sqrt((VJ0-VJfldAGN[((UVfldAGN<UV1)&(ufldAGN>u1))])**2+(UV1-UVfldAGN[((UVfldAGN<UV1)&(ufldAGN>u1))])**2)

gupall,gupAGN,gupfld,gupfldAGN=np.where(color_offset_all>0)[0],np.where(color_offset_AGN>0)[0],np.where(color_offset_fld>0)[0],np.where(color_offset_fldAGN>0)[0]
COtestall,COtestAGN,COtestfld,COtestfldAGN=np.zeros((len(gupall),3)),np.zeros((len(gupAGN),3)),np.zeros((len(gupfld),3)),np.zeros((len(gupfldAGN),3))
COtestall[:,0],COtestAGN[:,0],COtestfld[:,0],COtestfldAGN[:,0]=UV0-UVall[gupall],UV0-UVAGN[gupAGN],UV0-UVfld[gupfld],UV0-UVfldAGN[gupfldAGN]
COtestall[:,1],COtestAGN[:,1],COtestfld[:,1],COtestfldAGN[:,1]=-VJ0+VJall[gupall],-VJ0+VJAGN[gupAGN],-VJ0+VJfld[gupfld],-VJ0+VJfldAGN[gupfldAGN]
COtestall[:,2],COtestAGN[:,2],COtestfld[:,2],COtestfldAGN[:,2]=v0-vall[gupall],v0-vAGN[gupAGN],v0-vfld[gupfld],v0-vfldAGN[gupfldAGN]

color_offset_all[gupall],color_offset_AGN[gupAGN],color_offset_fld[gupfld],color_offset_fldAGN[gupfldAGN]=np.max(COtestall,axis=1),np.max(COtestAGN,axis=1),np.max(COtestfld,axis=1),np.max(COtestfldAGN,axis=1)


outall=np.concatenate((outall,outfld),axis=0)
outAGN=np.concatenate((outAGN,outfldAGN),axis=0)

outall[:,5],outall[:,6],outall[:,7],outall[:,8],outall[:,9],outall[:,10],outall[:,11]=np.append(allU,fldU),np.append(allV,fldV),np.append(allJ,fldJ),np.append(UVall,UVfld),np.append(VJall,VJfld),np.append(color_offset_all,color_offset_fld),np.append(np.ones(len(allU)),np.zeros(len(fldU)))
outAGN[:,8],outAGN[:,9],outAGN[:,10],outAGN[:,11],outAGN[:,12],outAGN[:,13],outAGN[:,14]=np.append(AGNU,fldAGNU),np.append(AGNV,fldAGNV),np.append(AGNJ,fldAGNJ),np.append(UVAGN,UVfldAGN),np.append(VJAGN,VJfldAGN),np.append(color_offset_AGN,color_offset_fldAGN),np.append(np.ones(len(AGNU)),np.zeros(len(fldAGNU)))

np.savetxt('/home/rumbaugh/Chandra/color-color_all.7.6.16.dat',outall,header='# field ID RA Dec redshift  mU  mV  mJ  U-V  V-J color_offset  in_structure',fmt='%12s %15s %9.5f %9.5f %10.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %i')
np.savetxt('/home/rumbaugh/Chandra/color-color_AGN.7.6.16.dat',outAGN,header='# field number RA Dec lum_soft lum_hard lum_full redshift  mU  mV  mJ  U-V  V-J color_offset  in_structure',fmt='%12s %15s %9.5f %9.5f %E %E %E %10.7f %11.7f %11.7f %11.7f %11.7f %11.7f %11.7f %i')




    
    
    

    
