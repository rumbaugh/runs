execfile("/home/rumbaugh/FindCloseSources.py")
import sys

def Inter(xa,xb,ya,yb,x0):
    slope = (yb-ya)/(1.0*xb-xa)
    return ya + slope*(x0-xa)

cr2 = read_file("/home/rumbaugh/COSMOS/lens_sample_id_z_exp_rc.dat")
rc = get_colvals(cr2,'col4')

cr = read_file("/home/rumbaugh/COSMOS/analysis/lens.analysis.12.4.10.dat")
IDs = get_colvals(cr,'col1')
means = get_colvals(cr,'col4')
stds = get_colvals(cr,'col5')
peaks = get_colvals(cr,'col7')
metric = (peaks-means)/stds
if len(stds) != len(rc): sys.exit("Files not of equal length")

FILE=open("/home/rumbaugh/COSMOS/analysis/lens.analysis.1.23.11.dat","w")
for i in range(0,len(stds)):
    if rc[i] < 27.27:
        lim = Inter(27.27,18.83,5.0,6.0,rc[i])
    else:
        lim = 5.0
    accept = 'No'
    if metric[i] > lim: accept = 'Yes'
    print '%5s Mean: %9.7f STD: %9.7f Sigma: %6.2f Threshhold: %6.2f Accepted: %s'%(int(IDs[i]),means[i],stds[i],metric[i],lim,accept)
    FILE.write('%5s %9.7f %9.7f %6.2f %6.2f %s'%(int(IDs[i]),means[i],stds[i],metric[i],lim,accept))
FILE.close()



