import numpy as np
names = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324'])
specname = np.array(['10444+10924','RXJ1757','9403+9840','9404+9836'])
path = '/home/rumbaugh/ChandraData'
nhs = np.array([0.0566,0.0407,0.0115,0.0116])
zs = np.array([0.84,0.69,0.69,0.76])

for i in range(0,4):
    load_pha(i+1,'%s/%s/master/spec_%s.pi'%(path,names[i],specname[i]))
set_model(1,xsraymond.rs1*xswabs.abs1)
set_model(2,xsraymond.rs2*xswabs.abs2)
set_model(3,xsraymond.rs3*xswabs.abs3)
set_model(4,xsraymond.rs4*xswabs.abs4)
RSarr = np.array([rs1,rs2,rs3,rs4])
ABSarr = np.array([abs1,abs2,abs3,abs4])
for i in range(0,4):
    RS = RSarr[i]
    ABS = ABSarr[i]
    ignore()
    notice(0.3,8.0)
    RS.kt = 3
    RS.abundanc = 0.3
    RS.redshift = zs[i]
    ABS.nh = nhs[i]
    freeze(ABS.nh)
    subtract(i+1)
    group_counts(i+1,20)
    fit(i+1)
    freeze(RS.norm)
    proj(i+1)
    thaw(RS.norm)
    print 'Total Counts: %7.1f'%(calc_data_sum(id=i+1))
    
    
