import numpy as np
import urllib

url_template = 'http://skyserver.sdss.org/dr13/SkyServerWS/ImgCutout/getjpeg?ra={}&dec={}&scale=0.024&width=600&height=600&opt=GI'
filename_template = '/home/rumbaugh/test1_{}.jpeg'

def save_image(ra, dec,DBID):
    url = url_template.format(ra, dec)
    filename = filename_template.format(DBID)
    urllib.urlretrieve(url, filename=filename)

cr=np.loadtxt('/home/rumbaugh/radecname_forSDSScutouts.3.2.17.csv',dtype={'names':('ra','dec','name'),'formats':('f8','f8','|S40')},delimiter=',')

ra,dec,DBID=cr['ra'][0],cr['dec'][0],cr['name'][0]
save_image(ra,dec,DBID)

