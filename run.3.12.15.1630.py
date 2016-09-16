import numpy as np

def write_poly(obs,mupoly,bounds_arr,filename='/home/rumbaugh/KAST/Science/mupoly.0956.dat'):
    FILE=open(filename,'a')
    FILE.write('\n%s %E %E %E %E %5.1f %5.1f'%(obs,mupoly[0],mupoly[1],mupoly[2],mupoly[3],bounds_arr[0],bounds_arr[1]))
    FILE.close()
