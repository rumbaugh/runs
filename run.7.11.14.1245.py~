date = '7.10.14'
import numpy as np
import pyfits as py
hdu = py.open('/mnt/data2/rumbaugh/Fermi/data/0218/S30218+35_86400.lc')
d = hdu[1].data
ltime = (d['START']-d['START'][0])/86400
g = np.where((ltime > 350) & (ltime < 525))[0]
Sfull = d['FLUX_100_300000']
Sfullerr = d['ERROR_100_300000']

FILE = open('/mnt/data2/rumbaugh/Fermi/data/0218/0218_TimeBombsInput.dat','w')
for i in range(0,len(Sfull)):
    FILE.write('%E %E\n'%(ltime[i],Sfull[i]*100000000))
FILE.close()

FILE = open('/home/rumbaugh/runs/run.7.10.14.1515.sh','w')
FILE.write('cd /home/rumbaugh/git/TimeBombs\n')

maxsamples = 1000
levelmax = 200
OPTFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_0218.%s.dat'%(date),'w')
OPTFILE.write('1\n100000\n50000\n2000\n%i\n1\n100\n%i\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample.0218.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample_info.0218.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/levels.0218.%s.dat'%(levelmax,maxsamples,date,date,date))
OPTFILE.close()
RUNFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_0218.%s.dat'%(date),'w')
RUNFILE.write('#include <iostream>\n#include "dnest3/Start.h"\n#include "MyModel.h"\n#include "Data.h"\n\nusing namespace std;\nusing namespace DNest3;\n\nint main(int argc, char** argv)\n{\n	Data::get_instance().load("/mnt/data2/rumbaugh/Fermi/data/0218/0218_TimeBombsInput.dat");\n	std::cout << "testing..." << std::endl;\n	//Options.sampleFile = "test.txt";\n	MTSampler<MyModel> sampler = setup_mt<MyModel>(argc, argv);\n	sampler.run();\n	return 0;\n}')
RUNFILE.close()
FILE.write('cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_0218.%s.dat /home/rumbaugh/git/TimeBombs/run.cpp\n'%(date))
FILE.write('g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp\n')
FILE.write('g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt\n')
FILE.write('./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_0218.%s.dat\n'%(date))
FILE.close()
