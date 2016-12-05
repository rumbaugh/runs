import numpy as np
import urllib

url_template = 'http://skyserver.sdss.org/dr13/SkyServerWS/ImgCutout/getjpeg?ra={}&dec={}&scale=0.05&width=600&height=600&opt=GI'
filename_template = '/home/rumbaugh/var_database/plots/SDSS_cutout.DBID_{}.jpeg'

def save_image(ra, dec,DBID):
    url = url_template.format(ra, dec)
    filename = filename_template.format(DBID)
    urllib.urlretrieve(url, filename=filename)

cr=np.loadtxt('/home/rumbaugh/radecname_forSDSScutouts.csv',dtype={'names':('ra','dec','name'),'formats':('f8','f8','|S20')},delimiter=',')

for ra,dec,DBID in zip(cr['ra'],cr['dec'],cr['DBID']):
    save_image(ra,dec,DBID)
