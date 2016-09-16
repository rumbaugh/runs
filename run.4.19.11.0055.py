cr = read_file("/home/rumbaugh/clusters.z+pos.4.18.11.dat")
struc = get_colvals(cr,'col1')
cname = get_colvals(cr,'col2')
z = get_colvals(cr,'col3')
ra = get_colvals(cr,'col4')
dec = get_colvals(cr,'col5')
execfile("/home/rumbaugh/angconvert.py")

FILE = open("/home/rumbaugh/clusters.redshifts.4.18.11.dat",'w')
for i in range(0,len(z)): FILE.write(str(z[i]) + '\n')
FILE.close()

cr2 = read_file("/home/rumbaugh/clusters.cc.out.nh.4.18.11.dat")

mpc = get_colvals(cr2,'col12')
mpcCM = get_colvals(cr2,'col13')

FILE = open("/home/rumbaugh/clusters.z+pos+mpc.4.18.11.dat",'w')
for i in range(0,len(z)): 
    rah,ram,ras = dec2hms(ra[i])
    dd,dm,ds = dec2dms(dec[i])
    FILE.write('%7s %2s %8.6f %9.7f %8.6f %4.2f %4.2f %02i %02i %04.1f %02i %02i %04.1f\n'%(struc[i],cname[i],z[i],ra[i],dec[i],mpc[i],mpcCM[i],rah,ram,ras,dd,dm,ds))
FILE.close()
