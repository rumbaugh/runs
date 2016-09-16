cd /home/rumbaugh/git/TimeBombs
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_1.tau_5.70.mu_0.857.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_1.tau_5.70.mu_0.857.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_2.tau_20.34.mu_0.823.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_2.tau_20.34.mu_0.823.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_3.tau_7.22.mu_0.841.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_3.tau_7.22.mu_0.841.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_4.tau_10.54.mu_0.042.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_4.tau_10.54.mu_0.042.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_5.tau_21.10.mu_0.831.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_5.tau_21.10.mu_0.831.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_6.tau_8.38.mu_0.864.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_6.tau_8.38.mu_0.864.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_7.tau_6.82.mu_0.607.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_7.tau_6.82.mu_0.607.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_8.tau_31.17.mu_0.230.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_8.tau_31.17.mu_0.230.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_9.tau_27.84.mu_0.230.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_9.tau_27.84.mu_0.230.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_10.tau_21.78.mu_0.596.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_10.tau_21.78.mu_0.596.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_11.tau_23.70.mu_0.962.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_11.tau_23.70.mu_0.962.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_12.tau_11.98.mu_0.795.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_12.tau_11.98.mu_0.795.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_13.tau_13.70.mu_0.086.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_13.tau_13.70.mu_0.086.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_14.tau_2.40.mu_0.871.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_14.tau_2.40.mu_0.871.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_15.tau_33.73.mu_0.821.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_15.tau_33.73.mu_0.821.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_16.tau_30.34.mu_0.906.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_16.tau_30.34.mu_0.906.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_17.tau_15.69.mu_0.438.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_17.tau_15.69.mu_0.438.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_18.tau_5.43.mu_0.850.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_18.tau_5.43.mu_0.850.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_19.tau_13.13.mu_0.894.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_19.tau_13.13.mu_0.894.6.19.14.dat
cp /mnt/data2/rumbaugh/Fermi/TimeBombs/input/run_testlightcurve_20.tau_12.45.mu_0.614.6.19.14.dat /home/rumbaugh/git/TimeBombs/run.cpp
g++ -O2 -Wall -Wextra -ansi -pedantic -I/home/rumbaugh/git/RJObject -I/usr/local/include -c run.cpp
g++ -o run ClassicMassInf1D.o  Data.o MyModel.o run.o -L/home/rumbaugh/git/RJObject -lrjobject -L/usr/local/lib -ldnest3 -lgsl -lgslcblas -lboost_system -lboost_thread-mt
./run -t 8 -o /mnt/data2/rumbaugh/Fermi/TimeBombs/input/Options_testlightcurve_20.tau_12.45.mu_0.614.6.19.14.dat
