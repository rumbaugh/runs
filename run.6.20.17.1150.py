import SDSS_PCA
PCA0=SDSS_PCA.SDSS_PCA(masterfile="/home/rumbaugh/random_SDSS_specs.csv")
PCA0.cut_master(100)
PCA0.load_spec_files('/home/rumbaugh/spec_randSDSS',wavstep=20,savefile='/home/rumbaugh/SDSS_PCA_fluxdf.csv')
PCA0.DoPCA(n_components=10)
PCA0.NNClassify()
print 'predicted_y: ',PCA0.predicted_y
PCA0.ComparePredictions()
PCA0.ComparePredictions(verbose=True)
