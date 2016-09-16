import numpy as np

level_dict = dict(zip(np.array([3,4,5,6,7,8,10,11,12,13,14,15,16,17,20]),np.array([140,130,100,200,135,105,130,160,80,75,150,30,115,85,135])))

date = '7.31.14'
ldate = '6.3.14'


cr = np.loadtxt('/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')
FILE = open('/home/rumbaugh/runs/run.7.31.14.2015.sh','w')
FILE.write('cd /home/rumbaugh/git/TimeBombs\n')
for i,pair in zip(np.array([0]),np.array([3])):
    maxsamples = 2
    if pair == 6: maxsamples = 2000
    levelmax = 1
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    OPTFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    OPTFILE.write('1\n100000\n50000\n2000\n%i\n1\n100\n%i\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/test.sample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/test.sample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n/mnt/data2/rumbaugh/Fermi/TimeBombs/output/test.levels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(levelmax,maxsamples,pair,tau,mu,date,pair,tau,mu,date,pair,tau,mu,date))
    OPTFILE.close()
    RUNFILE = open('/mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,date),'w')
    RUNFILE.write('#include <iostream>\n#include "dnest3/Start.h"\n#include "MyModel.h"\n#include "Data.h"\n\nusing namespace std;\nusing namespace DNest3;\n\nint main(int argc, char** argv)\n{\n	Data::get_instance().load("/mnt/data2/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat");\n	std::cout << "testing..." << std::endl;\n	//Options.sampleFile = "test.txt";\n	MTSampler<MyModel> sampler = setup_mt<MyModel>(argc, argv);\n	sampler.run();\n	return 0;\n}'%(pair,tau,mu,ldate))
    RUNFILE.close()
    FILE.write('cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat /home/rumbaugh/git/TimeBombs/run.cpp\n'%(pair,tau,mu,date))
    FILE.write('g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp\n')
    FILE.write('g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt\n')
    FILE.write('./run -t 1 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat\n'%(pair,tau,mu,date))
FILE.close()
