import numpy as np
import urllib

url_template = 'http://skyserver.sdss.org/dr13/SkyServerWS/ImgCutout/getjpeg?ra={}&dec={}&scale=0.0853343447033446&width=600&height=600&opt=GI'
filename_template = 'ra_{}_dec_{}.jpeg'

def save_image(ra, dec):
    url = url_template.format(ra, dec)
    filename = filename_template.format(ra, dec)
    urllib.urlretrieve(url, filename=filename)
