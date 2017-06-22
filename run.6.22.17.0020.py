import SDSS_PCA
PCA0=SDSS_PCA.SDSS_PCA(masterfile="/home/rumbaugh/random_SDSS_specs.csv")
PCA0.set_flux("/home/rumbaugh/SDSS_PCA_fluxdf.csv")
PCA0.set_wavelengths()
PCA0.DoPCA(n_components=10)
PCA0.NNClassify()
print 'predicted_y: ',PCA0.predicted_y
PCA0.ComparePredictions()
PCA0.ComparePredictions(verbose=True)
