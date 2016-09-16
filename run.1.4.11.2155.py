execfile("/home/rumbaugh/NewtonRaphson.py")

crDNSs = read_file("/home/rumbaugh/Dale.1604.logNlogS_soft.dat")
crDNSh = read_file("/home/rumbaugh/Dale.1604.logNlogS_hard.dat")
Ss = get_colvals(crDNSs,'col1')
Ns = get_colvals(crDNSs,'col2')
Nerrs = get_colvals(crDNSs,'col3')
Sh = get_colvals(crDNSh,'col1')
Nh = get_colvals(crDNSh,'col2')
Nerrh = get_colvals(crDNSh,'col3')

S0s = 2e-15
S0h = 1e-14
try: 
    SLBh
except NameError:
    SLBh = 6e-15
try:
    SUBh
except NameError:
    SUBh = 3e-14

gInR = np.where((Sh > SLBh) and (Sh < SUBh))
gInR = gInR[0]

Num = len(gInR)
Sum = 0.0
for i in range(0,Num):
    Sum += m.log(Sh/S0h)
a = -Num/Sum
g = np.searchsorted(Sh,S0h)
extrapN = (S0h-Sh[g-1])*(Nh[g]-Nh[g-1])/(Sh[g]-Sh[g-1]) + Nh[g-1]
k = extrapN
