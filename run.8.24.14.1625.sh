cd /home/rumbaugh/git/TimeBombs
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_11.tau_23.70.mu_0.962.8.24.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_11.tau_23.70.mu_0.962.8.24.14.dat
