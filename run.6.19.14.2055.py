import numpy as np

try:
    maxsamples
except NameError:
    maxsamples = 1000

date = '6.19.14'
ldate = '6.3.14'

cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
FILE = open('/home/rumbaugh/runs/run.6.19.14.2110.sh','w')
FILE.write('cd /home/rumbaugh/git/TimeBombs\n')
for i in range(0,20):
    tau,mu = cr[:,0][i],cr[:,1][i]
    OPTFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau,mu,date),'w')
    OPTFILE.write('1\n100000\n50000\n2000\n200\n1\n100\n%i\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/levels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(maxsamples,i+1,tau,mu,date,i+1,tau,mu,date,i+1,tau,mu,date))
    OPTFILE.close()
    RUNFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(i+1,tau,mu,date),'w')
    RUNFILE.write('#include <iostream>\n#include "dnest3/Start.h"\n#include "MyModel.h"\n#include "Data.h"\n\nusing namespace std;\nusing namespace DNest3;\n\nint main(int argc, char** argv)\n{\n	Data::get_instance().load("/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat");\n	std::cout << "testing..." << std::endl;\n	//Options.sampleFile = "test.txt";\n	MTSampler<MyModel> sampler = setup_mt<MyModel>(argc, argv);\n	sampler.run();\n	return 0;\n}'%(i+1,tau,mu,ldate))
    RUNFILE.close()
    FILE.write('cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/git/TimeBombs/run.cpp\n'%(i+1,tau,mu,date))
    FILE.write('g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp\n')
    FILE.write('g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt\n')
    FILE.write('./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n'%(i+1,tau,mu,date))
FILE.close()
