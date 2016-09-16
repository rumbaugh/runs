import os
import time
st = time.time()

os.system("csmooth infile=/home/rumbaugh/ChandraData/0910/master/RXJ0910+5419.cut.5.11.12.fits outfile=/home/rumbaugh/ChandraData/0910/master/RXJ0910+5419.csmooth.5.11.12.fits outsigfile=/home/rumbaugh/ChandraData/0910/master/RXJ0910+5419.csmooth_sig.5.11.12.fits sclmode=compute outsclfile=/home/rumbaugh/ChandraData/0910/master/RXJ0910+5419.csmooth_scls.5.11.12.fits clob+")

print "Elapsed time: %i seconds"%(time.time()-st)
FILE = open('/home/rumbaugh/run.5.11.12.1450.elapsetime.txt','w')
FILE.write('%f'%(time.time()-st))
FILE.close()
