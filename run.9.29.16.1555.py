import numpy as np

fname='/home/rumbaugh/Downloads/milliquas.txt'

mdict={'names':('RA','DEC','Name','Descrip','Rmag','Bmag','Comment','R','B','Z','Cite','Zcite','Qpct','Xname','Rname','Lobe1','Lobe2'),'formats':('f8','f8','|S27','|S5','f8','f8','|S4','|S2','|S2','f8','|S7','|S7','f8','|S24','|S24','|S24','|S24')}

delims=(11,12,27,5,5,5,4,2,2,7,7,7,4,23,23,23,23)

crm=np.genfromtxt(fname,dtype=mdict,delimiter=delims)
