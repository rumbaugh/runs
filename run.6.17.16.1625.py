execfile('/home/rumbaugh/set_spec_dict.py')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
lens=np.zeros(len(targets))

for field,it in zip(targets,np.arange(0,len(targets))):
    crs=np.loadtxt('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file'],dtype=specloaddict)
    lens[it]=np.shape(crs)[0]
print np.mean(lens)
