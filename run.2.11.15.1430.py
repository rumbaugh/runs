import aplpy

def initCompass(self, parent):
    self._ax1 = parent._ax1
    self._wcs = parent._wcs
    self.world2pixel = parent.world2pixel
    self.pixel2world = parent.pixel2world
    self._initialize_compass()
aplpy.overlays.Compass.__init__ = initCompass

fig.compass = aplpy.overlays.Compass(fig)
fig.compass.show_compass(color='white', 
                         corner=1, # Top-right
                         length=0.05) 
fig.compass._compass[0].set_arrowstyle('-')       # Remove head from East arrow
