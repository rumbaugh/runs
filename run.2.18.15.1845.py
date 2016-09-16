import numpy as np

level_dict = dict(zip(np.array([3,5,6,10,11]),np.array([165,110,230,155,185])))

date = '2.18.15'
ldate = '6.3.14'


cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
FILE = open('/home/rumbaugh/runs/run.2.18.15.1845.sh','w')
FILE.write('cd /home/rumbaugh/git/TimeBombs\n')
for i,pair in zip(np.arange(len(level_dict.keys())),level_dict.keys()):
    maxsamples = 1000
    if pair == 6: maxsamples = 2500
    levelmax = level_dict[pair]
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    OPTFILE = open('/home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    OPTFILE.write('1\n100000\n50000\n2000\n%i\n1\n100\n%i\n/home/rumbaugh/Fermi/TimeBombs/output/sample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/home/rumbaugh/Fermi/TimeBombs/output/sample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/home/rumbaugh/Fermi/TimeBombs/output/levels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(levelmax,maxsamples,pair,tau,mu,date,pair,tau,mu,date,pair,tau,mu,date))
    OPTFILE.close()
    RUNFILE = open('/home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    RUNFILE.write('#include <iostream>\n#include "dnest3/Start.h"\n#include "MyModel.h"\n#include "Data.h"\n\nusing namespace std;\nusing namespace DNest3;\n\nint main(int argc, char** argv)\n{\n	Data::get_instance().load("/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat");\n	std::cout << "testing..." << std::endl;\n	//Options.sampleFile = "test.txt";\n	MTSampler<MyModel> sampler = setup_mt<MyModel>(argc, argv);\n	sampler.run();\n	return 0;\n}'%(pair,tau,mu,ldate))
    RUNFILE.close()
    FILE.write('cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/git/TimeBombs/run.cpp\n'%(pair,tau,mu,date))
    FILE.write('g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp\n')
    FILE.write('g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt\n')
    FILE.write('./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n'%(pair,tau,mu,date))
FILE.close()
