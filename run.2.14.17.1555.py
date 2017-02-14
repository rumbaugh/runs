import numpy as np

crmq=np.loadtxt('/home/rumbaugh/milliquas_y3a1_match_pass2.csv',dtype={'names':('MQ_ROWNUM','RA','DEC','HPIX','COADD_OBJECTS_ID'),'formats':('i8','f8','f8','i8','i8')},delimiter=',',skiprows=1)
