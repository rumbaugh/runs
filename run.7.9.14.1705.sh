cd /home/rumbaugh/git/TimeBombs
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_4.tau_10.54.mu_0.042.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_4.tau_10.54.mu_0.042.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_7.tau_6.82.mu_0.607.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_7.tau_6.82.mu_0.607.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_8.tau_31.17.mu_0.230.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_8.tau_31.17.mu_0.230.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_10.tau_21.78.mu_0.596.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_10.tau_21.78.mu_0.596.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_12.tau_11.98.mu_0.795.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_12.tau_11.98.mu_0.795.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_16.tau_30.34.mu_0.906.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_16.tau_30.34.mu_0.906.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_17.tau_15.69.mu_0.438.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_17.tau_15.69.mu_0.438.7.9.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_20.tau_12.45.mu_0.614.7.9.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_20.tau_12.45.mu_0.614.7.9.14.dat
