cd /home/rumbaugh/git/TimeBombs
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_3.tau_7.22.mu_0.841.7.31.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 1 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_3.tau_7.22.mu_0.841.7.31.14.dat
