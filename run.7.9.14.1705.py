import numpy as np

level_dict = dict(zip(np.array([4,7,8,10,12,16,17,20]),np.array([175,170,135,155,95,125,95,190])))

date = '7.9.14'
ldate = '6.3.14'


cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
FILE = open('/home/rumbaugh/runs/run.7.9.14.1705.sh','w')
FILE.write('cd /home/rumbaugh/git/TimeBombs\n')
for i,pair in zip(np.arange(len(level_dict.keys())),level_dict.keys()):
    maxsamples = 1000
    if pair == 6: maxsamples = 2000
    levelmax = level_dict[pair]
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    OPTFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    OPTFILE.write('1\n100000\n50000\n2000\n%i\n1\n100\n%i\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/sample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/levels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(levelmax,maxsamples,pair,tau,mu,date,pair,tau,mu,date,pair,tau,mu,date))
    OPTFILE.close()
    RUNFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    RUNFILE.write('#include <iostream>\n#include "dnest3/Start.h"\n#include "MyModel.h"\n#include "Data.h"\n\nusing namespace std;\nusing namespace DNest3;\n\nint main(int argc, char** argv)\n{\n	Data::get_instance().load("/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat");\n	std::cout << "testing..." << std::endl;\n	//Options.sampleFile = "test.txt";\n	MTSampler<MyModel> sampler = setup_mt<MyModel>(argc, argv);\n	sampler.run();\n	return 0;\n}'%(pair,tau,mu,ldate))
    RUNFILE.close()
    FILE.write('cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/git/TimeBombs/run.cpp\n'%(pair,tau,mu,date))
    FILE.write('g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp\n')
    FILE.write('g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt\n')
    FILE.write('./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n'%(pair,tau,mu,date))
FILE.close()
