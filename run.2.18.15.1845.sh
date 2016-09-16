cd /home/rumbaugh/git/TimeBombs
cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_11.tau_23.70.mu_0.962.2.18.15.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_11.tau_23.70.mu_0.962.2.18.15.dat
cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_10.tau_21.78.mu_0.596.2.18.15.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_10.tau_21.78.mu_0.596.2.18.15.dat
cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_3.tau_7.22.mu_0.841.2.18.15.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_3.tau_7.22.mu_0.841.2.18.15.dat
cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_5.tau_21.10.mu_0.831.2.18.15.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_5.tau_21.10.mu_0.831.2.18.15.dat
cp /home/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_6.tau_8.38.mu_0.864.2.18.15.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp MyModel.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /home/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_6.tau_8.38.mu_0.864.2.18.15.dat
