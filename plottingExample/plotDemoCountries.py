import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.io.shapereader as shpreader
import itertools
import numpy as np

#shapename = 'admin_0_countries'
#countries_shp = shpreader.natural_earth(resolution='110m',
#                                        category='cultural', name=shapename)
#
## some nice "earthy" colors
#earth_colors = np.array([(199, 233, 192),
#                                (161, 217, 155),
#                                (116, 196, 118),
#                                (65, 171, 93),
#                                (35, 139, 69),
#                                ]) / 255.
#earth_colors = itertools.cycle(earth_colors)
#
#
#count = []
#ax = plt.axes(projection=ccrs.PlateCarree())
#for country in shpreader.Reader(countries_shp).records():
#    count.append(country.attributes[u'name_long'])
#    print country.attributes['name_long'], earth_colors.next()
#    ax.add_geometries(country.geometry, ccrs.PlateCarree(),
#                      facecollsor=earth_colors.next())#,
#                      #label=country.attributes['name_long'])
#
#plt.show()

shpfilename = shpreader.natural_earth(resolution='50m',
                                      category='cultural',
                                      name='admin_0_countries')

                                                                            
reader = shpreader.Reader(shpfilename)
countries = reader.records()
#country = next(countries)

#print type(country.attributes)
#print sorted(country.attributes.keys())
norm = mpl.colors.Normalize(vmin=0, vmax=1338612970.0)
cmap = plt.cm.RdYlBu_r

fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

#plt.figure()
#ax = plt.axes(projection=ccrs.PlateCarree())
countryNames = []
populations = []
for country in countries:
    #print x
    #   pring country name
    countryNames.append(country.attributes['name'])
    populations.append(country.attributes['pop_est'])
    #print x.attributes['name']
    
    ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                      facecolor=cmap(norm(country.attributes['pop_est'])),
                      linewidth=0.01)#,
                      #label=country.attributes['NAME_LONG'])
    #country = next(countries)
    #   colors thanks to @Rutger Kassies http://stackoverflow.com/questions/25505674/python-matplotlib-add-colorbar
cax = fig.add_axes([0.95, 0.2, 0.02, 0.6])
cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, spacing='proportional', format='%.0f')
ax.set_title('pop_est')
cb.set_label('pop_est')
plt.show()

print sorted(country.attributes.keys())
plt.savefig('demo.pdf', format='pdf', dpi=1200, bbox_inches='tight')


#
#for country in countries.records():
#    print country.attributes['name_long']