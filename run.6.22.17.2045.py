import SDSS_PCA
PCA0=SDSS_PCA.SDSS_PCA(masterfile="/home/rumbaugh/random_SDSS_specs.csv")
PCA0.prune_master('/home/rumbaugh/spec_randSDSS/')
PCA0.cut_master(10000)
PCA0.load_spec_files('/home/rumbaugh/spec_randSDSS',wavstep=20,savefile='/home/rumbaugh/SDSS_PCA_fluxdf.10000.csv')
PCA0.DoPCA(n_components=20)
target=np.zeros(len(PCA0.master),dtype='|S30')
for i in range(0,len(target)):
    target[i]=PCA0.master['class'].values[i]
    if PCA0.master['subClass'].values[i]!='null':
        target[i]='{},{}'.format(target[i],PCA0.master['subClass'].values[i])
PCA0.master['target']=target
PCA0.NNClassify(target=PCA0.master['target'])
print 'predicted_y: ',PCA0.predicted_y
PCA0.ComparePredictions(target=PCA0.master['target'])
#PCA0.ComparePredictions(verbose=True)
