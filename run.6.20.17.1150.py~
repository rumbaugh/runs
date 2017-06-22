import SDSS_PCA
PCA0=SDSS_PCA.SDSS_PCA(masterfile="/home/rumbaugh/random_SDSS_specs.csv")
PCA0.cut_master(10)
PCA0.load_spec_files('/home/rumbaugh/spec_randSDSS',wavstep=20,savefile='/home/rumbaugh/SDSS_PCA_fluxdf.csv')
PCA0.DoPCA(n_components=10)
PCA0.KDTreeClassify()
