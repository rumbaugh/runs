execfile('/home/rumbaugh/CalcVelDisp.py')

def test_vel_form(z,spread=0.01,num=50):
    zs=np.random.normal(z,spread,num)
    c = 3.0*10**5
    vels = (zs-SE.biweight_loc(zs))*c/(1.0+zs)
    z0=SE.biweight_loc(zs)
    v0=((z0+1)**2-1)/((z0+1)**2+1)
    us=((zs+1)**2-1)/((zs+1)**2+1)
    uvels=(us-v0)/(1-us*v0)*c
    print vels,uvels
    print (uvels-vels)/vels*100
