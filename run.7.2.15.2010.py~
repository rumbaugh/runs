import numpy as np

date='6.9.15'

crp = np.loadtxt('/home/rumbaugh/Fermi/TimeBombs/output/posterior.0218.t16.ms_1000.5.26.15.dat')
tau_out,mu_out=crp[:,1],crp[:,2]
figure(10)
clf()
hist(np.abs(tau_out),bins=200)
axvline(11.16,ls='dashed',lw=1,color='red')
xlabel('Time Delay (days)')
ylabel('Num. of samples')
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/post.tau_hist.0218.%s.png'%date)
