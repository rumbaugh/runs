import numpy as np

date='5.27.15'

crp = np.loadtxt('/home/rumbaugh/Fermi/TimeBombs/output/posterior.0218.t16.ms_1000.5.26.15.dat')
tau_out,mu_out=crp[:,1],crp[:,2]
figure(10)
clf()
scatter(np.abs(tau_out),mu_out,s=6)
xlabel('Time Delay (days)')
ylabel('Magnification')
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/post.tau_vs_mu.0218.%s.png'%date)
figure(11)
clf()
hist(np.abs(tau_out),bins=20)
xlabel('Time Delay (days)')
ylabel('Num. of samples')
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/post.tau_hist.0218.%s.png'%date)
