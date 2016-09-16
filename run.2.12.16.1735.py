import numpy as np

optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}
field='cl0023'
ldate='1.19.16'
matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
pzmatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_photz.%s.dat'%(field,field,field,'2.10.16')

crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
crmpz=np.loadtxt(pzmatchcat,dtype=optmatchloaddict)

radloaddict={'names':('index_x','radio_ID','radio_RA','radio_DEC','radio_derr','number','opt_ra1','opt_dec1','photo_ID1','prob1','likelihood1','prob_non','radio_flux','photo_ID','z_x','DM','NUV','U','V','r','J','2800','index_y'),'formats':('i8','i8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

pzradloaddict={'names':('radio_ID','radio_RA','radio_DEC','radio_derr','number','opt_ra1','opt_dec1','photo_ID1','prob1','likelihood1','prob_non','radio_flux','photo_ID','z_x','DM','NUV','U','V','r','J'),'formats':('i8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8','f8','i8','f8','f8','f8','f8','f8','f8','f8')}

crlu=np.loadtxt('/home/rumbaugh/Downloads/specz_matches_info.cat',dtype=radloaddict)
crlupz=np.loadtxt('/home/rumbaugh/Downloads/matches_photomatric.cat',dtype=pzradloaddict)

for i in range(0,np.shape(crlu)[0]):
    g=np.where('%i'%crlu['photo_ID1'][i]==crm['optID1'])[0]
    if len(g)>0: print crlu['radio_ID'][i]

for i in range(0,np.shape(crlupz)[0]):
    g=np.where('%i'%crlupz['photo_ID1'][i]==crmpz['optID1'])[0]
    if len(g)>0: print crlupz['radio_ID'][i]


