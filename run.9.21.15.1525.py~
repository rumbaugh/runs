import numpy as np

date='7.3.15'

crp = np.loadtxt('/home/rumbaugh/Fermi/TimeBombs/output/posterior.0218.t16.ms_1000.5.26.15.dat')
tau_out,mu_out=crp[:,1],crp[:,2]
figure(10)
clf()

def mjrFormatter(x, pos, maxperc=len(tau_out)):
    return "%.2f"%(x*1./maxperc)
    #return "${{{0}}}$".format(x)

#def mjrFormatter_no_TeX(x, pos):
#    return "2^{0}".format(x)


hist(np.abs(tau_out),bins=200,color='cyan')
#hist(np.abs(tau_out),bins=200,color='cyan')
ymin,ymax=ylim()
ylim(ymin,ymax*1.1)
ymin,ymax=ylim()

axvline(11.16,ls='dashed',lw=1,color='red')
maxytick=int(ymax*1./len(tau_out)/0.05)+1
ytickstep=0.05*len(tau_out)
yticks(np.arange(0,maxytick*ytickstep,ytickstep))
ax=gca()
ax.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(mjrFormatter))

xlabel('Time Delay (days)')
ylabel('Fraction of Posterior')
draw()
savefig('/home/rumbaugh/Fermi/TimeBombs/plots/post.tau_hist.0218.%s.png'%date)
