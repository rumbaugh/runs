import numpy as np

cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh'),'formats':('|S24','|S24','f8','f8','f8','f8')})
testfield,testclus=np.zeros(np.shape(cr)[0],dtype='|S24'),np.zeros(np.shape(cr)[0],dtype='|S24')
for i in range(0,len(testclus)):
    testfield[i]=cr['field'][i].lower()
    testclus[i]=cr['cluster'][i].lower()
testfield2,testclus2=np.zeros(np.shape(cr2)[0],dtype='|S24'),np.zeros(np.shape(cr2)[0],dtype='|S24')
for i in range(0,len(testclus2)):
    testfield2[i]=cr2['field'][i].lower()
    testclus2[i]=cr2['cluster'][i].lower()

band,ELB,EUB=['soft','hard','full'],[0.5,2.0,0.5],[2.0,7.0,7.0]
eLBdict=dict(zip(band,ELB))
eUBdict=dict(zip(band,EUB))

date='6.24.16'

def fit_spec(cluster,field=None,band='full',gc=15,kTmax=29,redshift=None):
    nofield=False
    g=np.where(cluster.lower()==testclus)[0]
    if len(g)==0:
        nofield=True
        if field==None:
            sys.exit('no match for cluster=%s and no field was given'%cluster)
        else:
            g=np.where(field.lower()==testfield)[0]
            if len(g)==0:
                sys.exit('No match for cluster=%s and field=%s'%(cluster,field))
            else:
                g=g[0]
    else:
        g=g[0]
        if field==None: field=cr['field'][g].lower()
    z,nh=cr['z'][g],cr['nh'][g]/100.
    path='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    speccombfile='%s/%s_spec_%s_combined_src.pi'%(path,cluster,band)
    specsinglefile='%s/%s_spec_%s_grp.pi'%(path,cluster,band)
    try:
        load_pha('%s'%(speccombfile))
    except:
        load_pha('%s'%(specsinglefile))
    notice(eLBdict[band],eUBdict[band])
    subtract()
    set_model(xsraymond.rs*xswabs.abs1)
    abs1.nh = nh
    rs.redshift = z
    freeze(rs.redshift)
    if nofield: thaw(rs.redshift)
    if redshift!=None:
        rs.redshift=redshift
        if z!=0:
            freeze(rs.redshift)
        else:
            thaw(rs.redshift)
    rs.Abundanc = 0.3
    rs.kT.max = kTmax
    freeze(abs1.nh)
    group_counts(gc)
    fit()
    proj()
    plot_fit()
    save_model(1,filename='%s/%s_spec_%s.%s.model'%(path,cluster,band,date),clobber=True)
    abs1.nh=0
    rs.redshift=0
    print calc_model_sum(0.5,7.0)
    notice()
    print calc_model_sum()
    print calc_model_sum(0,100)

