import numpy as np


fields = np.array(['NEP5281','RXJ1757','Cl1324','Cl1324'])
names = np.array(['10444+10924','RXJ1757','9403+9840','9404+9836'])
nh = np.array([0.0566,0.0407,0.0115,0.0115])
z = np.array([0.82,0.69,0.76,0.76])

for i in range(0,1):
    load_pha('/scratch/rumbaugh/ciaotesting/%s/master/spec_%s_full_300_grp.pi'%(fields[i],names[i]))
    notice(0.5,8.0)
    subtract()
    set_model(xsraymond.rs*xswabs.abs1)
    abs1.nh = nh[i]
    rs.redshift = z[i]
    rs.Abundanc = 0.3
    rs.kT.max = 40
    freeze(abs1.nh)
    fit()
    plot_fit()
