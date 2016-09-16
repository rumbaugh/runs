import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/magcomp.9.5.16.dat')
mrfu_all,mrfb_all,mblue_all,mred_all,rs_all=cr[:,0],cr[:,1],cr[:,2],cr[:,3],cr[:,4]


plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(mrfb_all-mred_all,range=(-3,3),bins=60)
plt.xlabel(r'$m_B-m_{red}$')
plt.savefig('/home/rumbaugh/Chandra/plots/magcomp_mRFB-mred.9.5.16.png')



plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.hist(mrfu_all-mrfb_all-(mblue_all-mred_all),range=(-1,1),bins=50)
plt.xlabel(r'$m_U-m_B - \left(m_{blue}-m_{red}\right)$')
plt.title('Difference between supercolors and rest-frame colors')
plt.savefig('/home/rumbaugh/Chandra/plots/magcomp_coldiff.9.5.16.png')

coldif=mrfu_all-mrfb_all-(mblue_all-mred_all)
coldif=np.sort(coldif)
print np.median(coldif),coldif[np.int(0.5*0.3173*len(coldif))],coldif[np.int((1-0.5*0.3173)*len(coldif))]
print '%f%% within 0.5. %f%% within 0.25. %f%% within 0.1'%(len(coldif[np.abs(coldif)<0.5])*100./len(coldif),len(coldif[np.abs(coldif)<0.25])*100./len(coldif),len(coldif[np.abs(coldif)<0.1])*100./len(coldif))

plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.scatter(rs_all,mrfu_all-mrfb_all-(mblue_all-mred_all))
#plt.plot([0,0]
plt.ylabel(r'$m_U-m_B - \left(m_{blue}-m_{red}\right)$')
plt.xlabel('redshift')
plt.axhline(0,lw=2,ls='dashed',color='cyan')
plt.ylim(-1,1)
plt.savefig('/home/rumbaugh/Chandra/plots/magcomp_coldiff_vs_RS.9.5.16.png')
