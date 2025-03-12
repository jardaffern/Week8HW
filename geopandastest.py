import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

#plot a map by grade
tstations = gpd.read_file('mbta/MBTA_ARC.shp')
tstations.plot(column='GRADE')
#plot map overall
plt.show()


