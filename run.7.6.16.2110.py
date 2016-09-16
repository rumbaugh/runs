import numpy as np
import matplotlib.pyplot as plt

crall=np.loadtxt('/home/rumbaugh/Chandra/color-color_all.7.6.16.dat',dtype={'names':('field','ID','RA','Dec','redshift','mU','mV','mJ','U-V','V-J','color_offset','in_structure'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8')})
crAGN=np.loadtxt('/home/rumbaugh/Chandra/color-color_AGN.7.6.16.dat',dtype={'names':('field','ID','RA','Dec','lS','lH','lF','redshift','mU','mV','mJ','U-V','V-J','color_offset','in_structure'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','i8')})

opcoeff=1

opall,opAGN=1-np.abs(crall['color_offset']*opcoeff),1-np.abs(crAGN['color_offset']*opcoeff)
opall[opall<0],opAGN[opAGN<0]=0,0



UV0,VJ0=1.3,1.6
UV1,VJ1=0.88*VJ0+0.59,(UV0-0.59)/0.88
plt.xlim(-1,2.5)
plt.ylim(0,2.5)
xlim=plt.xlim()
ylim=plt.ylim()

xdummy=np.linspace(VJ1,VJ0,10)

fig=figure(2)
fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist((crAGN['color_offset'][crAGN['in_structure']>0.5],crAGN['color_offset'][crAGN['in_structure']<0.5]),range=(-1,5./3),bins=8,color=('r','magenta'))

b=ax2.hist((crall['color_offset'][crall['in_structure']>0.5],crall['color_offset'][crall['in_structure']<0.5]),range=(-1,5./3),bins=8,color=('b','green'),alpha=0.3,weights=(100*np.ones(len(crall['RA'][crall['in_structure']>0.5]))*1./len(crall['RA'][crall['in_structure']>0.5]),100*np.ones(len(crall['RA'][crall['in_structure']<0.5]))*1./len(crall['RA'][crall['in_structure']<0.5])))
ax.set_xlabel('Color Offset')
ax.set_ylabel('Number of Sources')
ax.set_xlim(-1,5./3)
ax.set_ylim(0,17)
ax2.set_xlim(-1,5./3)
ax2.set_ylim(0,17./len(crAGN['RA'][crAGN['in_structure']>0.5])*100)
ax2.set_ylabel("Percentage of All Sources")
fig.savefig("/home/rumbaugh/Chandra/plots/color_offset.hist.7.7.16.png")


fig=figure(3)
fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)
#ax2=ax.twinx()
#ax2.tick_params(which='major',length=8,width=2,labelsize=14)
#ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist((-crAGN['color_offset'][crAGN['in_structure']>0.5],-crAGN['color_offset'][crAGN['in_structure']<0.5]),range=(-4./3,2./3),bins=6,color=('r','magenta'),weights=(100*np.ones(len(crAGN['RA'][crAGN['in_structure']>0.5]))*1./len(crAGN['RA'][crAGN['in_structure']>0.5]),100*np.ones(len(crAGN['RA'][crAGN['in_structure']<0.5]))*1./len(crAGN['RA'][crAGN['in_structure']<0.5])),label=('ORELSE AGN','Field AGN'))

b=ax.hist((-crall['color_offset'][crall['in_structure']>0.5],-crall['color_offset'][crall['in_structure']<0.5]),range=(-4./3,2./3),bins=6,color=('b','green'),alpha=0.3,weights=(100*np.ones(len(crall['RA'][crall['in_structure']>0.5]))*1./len(crall['RA'][crall['in_structure']>0.5]),100*np.ones(len(crall['RA'][crall['in_structure']<0.5]))*1./len(crall['RA'][crall['in_structure']<0.5])),label=('All ORELSE','All Field'))
ax.set_xlabel('Color Offset')
#ax.set_ylabel('Number of Sources')
ax.set_xlim(-4./3,2./3)
#ax.set_ylim(0,17)
#ax2.set_xlim(-4./3,2./3)
ax.set_ylim(0,50)
ax.set_ylabel("Percentage of Sources")
plt.legend(loc='upper left')
fig.savefig("/home/rumbaugh/Chandra/plots/color_offset.hist_norm.7.7.16.png")


plt.figure(3)
fig.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
ax=fig.add_subplot(1,1,1)

groups=['Passive','Intermediate','Cl0023 & Cl1604','High-z']
group_dict={'Passive':['cl1350','rcs0224','rxj1221','rxj1757','rxj1821'],'Intermediate':['cl1324','cl1324_north','cl1324_south','rxj1716'],'Cl0023 & Cl1604':['cl0023','cl1604'],'High-z':['rxj0910','rxj1053','cl0849']}

carr,marr=['r','magenta','blue','orange'],['d','*','s','o']
for group,ig in zip(groups,np.arange(len(groups))):
    gg=np.zeros(0,dtype='i8')
    fields=group_dict[group]
    for field in fields:
        ggt=np.where((crAGN['field']==field)&(crAGN['in_structure']>0.5))[0]
        gg=np.append(gg,ggt)
    plt.scatter(-crAGN['color_offset'][gg][crAGN['lF'][gg]>0],np.log10(crAGN['lF'][gg][crAGN['lF'][gg]>0]),color=carr[ig],marker=marr[ig],label=group,s=64)
gg=np.where((crAGN['in_structure']<0.5)&(crAGN['redshift']<=0.96))[0]
plt.scatter(-crAGN['color_offset'][gg][crAGN['lF'][gg]>0],np.log10(crAGN['lF'][gg][crAGN['lF'][gg]>0]),color='green',marker='h',label='Field (z<0.96)',s=64)
gg=np.where((crAGN['in_structure']<0.5)&(crAGN['redshift']>0.96))[0]
plt.scatter(-crAGN['color_offset'][gg][crAGN['lF'][gg]>0],np.log10(crAGN['lF'][gg][crAGN['lF'][gg]>0]),color='cyan',marker='p',label='Field (z>0.96)',s=64)
plt.legend(loc='lower left')
plt.ylabel('X-ray Luminosity')
plt.xlabel('Color Offset')
plt.ylim(41.8,44.5)
plt.xlim(-1.3,0.43)
plt.savefig('/home/rumbaugh/Chandra/plots/color-color_offset_vs_Lum.7.7.16.png')
