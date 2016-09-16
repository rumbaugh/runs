execfile("/home/rumbaugh/radmon_var_chisq_test.py")

try:
    mu
except NameError:
    mu = 10.
try:
    std
except NameError:
    std = 1.
try:
    size
except NameError:
    size = 5
try:
    trials
except NameError:
    trials = 100000


chisq = np.zeros(trials)
for i in range(0,trials):
    obs = np.random.normal(loc=mu,scale=std,size=size)
    exp = np.ones(size)*mu
    err = np.ones(size)*std
    chisq[i] = calc_chi_sqrd(obs,err,exp=exp)
sort_chisq = np.sort(chisq)
print sort_chisq[int(0.05*trials)],sort_chisq[int(0.95*trials)]
