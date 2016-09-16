import numpy as np
execfile('/home/rumbaugh/SphDist.py')

fields=['cl0023','rxj1716']

netcnts=np.zeros(2)
craim=np.loadtxt('/home/rumbaugh/Chandra/aimpnts.dat',dtype={'names':('field','RA','Dec','dum','imX','imY'),'formats':('|S24','f8','f8','f8','f8','f8')})

for field in fields:
    gaim=np.where(field==craim['field'])[0]
    RAaim,Decaim=craim['RA'][gaim],craim['Dec'][gaim]
    aimX,aimY=craim['imX'][gaim],craim['imY'][gaim]
    oaa=np.zeros(0)
    for s in [1,2]:
        cr=np.loadtxt('/home/rumbaugh/sample%i_%s.image_cut.w_PSF.reg'%(s,field),skiprows=3,dtype='|S256')
        for i in range(0,len(cr)):
            tmpstr=cr[i].split(' #')
            tmpstr=tmpstr[0].split(',')
            tmpra,tmpangle=tmpstr[0].split('('),tmpstr[4].split(')')
            ra,dec,rA,rB,ang=float(tmpra[1]),float(tmpstr[1]),float(tmpstr[2]),float(tmpstr[3]),float(tmpangle[0])
            oaa=np.append(oaa,np.sqrt((ra-aimX)**2+(dec-aimY)**2))
    oaa=np.sort(oaa*0.492/60)
    print '%s - '%field
    for frac in np.arange(50,100,5): print '%i%%: %f'%(frac,oaa[np.int(frac/100.*len(oaa))])
