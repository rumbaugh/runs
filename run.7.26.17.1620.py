import numpy as np
import pandas as pd
import PyAstronomy.pyasl

pixcenX,pixcenY=512,350
pixleftX,pixleftY=383,350
pixrightX,pixleftY=641,350
pixtopX,pixtopY=512,285
pixbottomX,pixbottomY=512,415

df=pd.read_csv('/home/rumbaugh/LSST_bounds_pixels.csv')

x,y=-(df.x.values-pixcenX)*180./129.,-(df.y.values-pixcenY)*90./65.
x,y=x[-1:-len(x):-1],y[-1:-len(x):-1]
ra,dec,i=PyAstronomy.pyasl.inverseAitoff(x,y)
ra+=180
outdf=pd.DataFrame({'ra':ra,'dec':dec})
outdf.to_csv('/home/rumbaugh/LSST_bounds_radec.csv',index=False)
