import numpy as np


def DES2SDSS_gr(g,r):
    return (133625*g-9375*r-218)/124250.,(69.*g+925*r)/994.+516./62125.

def DES2SDSS_iz(i,z):
    return (-89*np.sqrt(-96000*i+96000*z+181561)+8000*z+37827)/8000.,(-17*np.sqrt(-96000*i+96000*z+181561)+24000*z+6731)/24000.

def SDSS2DES_gr(g,r):
    return g+0.001-0.075*(g-r),r-0.009-0.069*(g-r)
    
def SDSS2DES_iz(i,z):
    return i+.014-0.214*(i-z)-0.096*(i-z)**2,z+0.022-0.068*(i-z)

def DES2SDSS(magg,magr,magi,magz):
    medg,medr,medi,medz=np.median(magg),np.median(magr),np.median(magi),np.median(magz)
    newg,dum1=DES2SDSS_gr(magg,medr)
    dum2,newr=DES2SDSS_gr(medg,magr)
    newi,dum1=DES2SDSS_iz(magi,medz)
    dum2,newz=DES2SDSS_iz(medi,magz)
    return newg,newr,newi,newz

def SDSS2DES(magg,magr,magi,magz):
    medg,medr,medi,medz=np.median(magg),np.median(magr),np.median(magi),np.median(magz)
    newg,dum1=SDSS2DES_gr(magg,medr)
    dum2,newr=SDSS2DES_gr(medg,magr)
    newi,dum1=SDSS2DES_iz(magi,medz)
    dum2,newz=SDSS2DES_iz(medi,magz)
    return newg,newr,newi,newz

g,r,i,z=np.zeros(4)+17,np.zeros(4)+18,np.zeros(4)+19,np.zeros(4)+20
times=np.arange(4)
print g,r,i,z
sdssg,sdssr,sdssi,sdssz=DES2SDSS(g,r,i,z)
newg,newr,newi,newz=SDSS2DES(sdssg,sdssr,sdssi,sdssz)
print sdssg,sdssr,sdssi,sdssz
print newg,newr,newi,newz

g,r,i,z=np.random.uniform(17,18,4),np.random.uniform(17.5,18.5,4),np.random.uniform(18,19,4),np.random.uniform(19,20,4)

print g,r,i,z
sdssg,sdssr,sdssi,sdssz=DES2SDSS(g,r,i,z)
newg,newr,newi,newz=SDSS2DES(sdssg,sdssr,sdssi,sdssz)
print sdssg,sdssr,sdssi,sdssz
print newg,newr,newi,newz
print (newg-g)/g,(newr-r)/r,(newi-i)/i,(newz-z)/z
