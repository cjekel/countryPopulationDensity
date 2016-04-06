#   Python 2.7.10 --  64-bit
#   import country population and area data saved as csv
#   then calculate the population density for these countries
import numpy as np
import csv
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib as mpl
import cartopy.io.shapereader as shpreader
import itertools

#   define a function to Read the CSV files
def pullCSV(fileName):
    country = []
    countryData = []
    with open(fileName, 'r') as csvOutput:
        output = csv.reader(csvOutput, delimiter=',', quotechar='"')
        for i, row in enumerate(output):
            #   skip the header column
            if i < 1:
                pass
            else:
                country.append(row[1])
                countryData.append(float(row[2]))
        return country, countryData

#   country name as string, country area in square km
countryNameArea, countryArea = pullCSV('data/area.csv')
countryNamePop, countryPop = pullCSV('data/population.csv')

#   assuming that the name of the country is a unique identifier of the country
#   we have 236 countries on both lists
#print 'Number of countries on both lists ->', len(set(countryNameArea) & set(countryNamePop)
#)

#   I need to create a list in the following manner 
#    [Country, Population, Area, Density]
countriesComplete = []
countryNamesComplete = []
for i, j in enumerate(countryNamePop):
    if j in countryNameArea:
        #   then j = country, and is in both lists
        
        #   find the population
        population = countryPop[i]
        
        #   find the area
        indexOfArea = countryNameArea.index(j)
        area = countryArea[indexOfArea]
        
        #   if the area is not greater than 0 sq km, then pass
        #   otherwise calculate the density and append to list
        
        if area > 0:
            countryNamesComplete.append(j)

            #   calculation the population density
            popDensity = population / area
            
            #   save the list as [Country, Population, Area in sq km, population density per sq km]
            countriesComplete.append([j, population, area, popDensity])

#   sort through the complete countries list by population
#   density from high to low
countriesCompleteSorted = sorted(countriesComplete, key=lambda x: x[-1], reverse=True)

#   save to csv
with open('data/countryPopDensity.csv', 'wb') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', quotechar='"')
    #   write the header
    wr.writerow(['Country', 'Population', 'Area in sq km', 'Population Density per sq km'])
    for i in countriesCompleteSorted:
        wr.writerow(i)

#    convert CountriesComplete to numpy      
npCountriesComplete = np.array(countriesComplete)
populationDensities = npCountriesComplete[:,-1]
populationDensities = populationDensities.astype(np.float)
                                        
#   find the country names that are on admin_0 country list from http://www.naturalearthdata.com/downloads/
shpfilename = shpreader.natural_earth(resolution='50m',
                                      category='cultural',
                                      name='admin_0_countries')
reader = shpreader.Reader(shpfilename)
countries = reader.records()

colorMapList = ['viridis', 'inferno', 'plasma', 'magma', 'Blues', 'BuGn', 'BuPu',
                             'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                             'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                             'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd',
                             'afmhot', 'autumn', 'bone', 'cool',
                             'copper', 'gist_heat', 'gray', 'hot',
                             'pink', 'spring', 'summer', 'winter', 
                             'gist_earth', 'terrain', 'ocean', 'gist_stern',
                             'brg', 'CMRmap', 'cubehelix',
                             'gnuplot', 'gnuplot2', 'gist_ncar',
                             'nipy_spectral', 'jet', 'rainbow',
                             'gist_rainbow', 'hsv', 'flag', 'prism']

norm = mpl.colors.Normalize(vmin=min(populationDensities), vmax=459)
for name in colorMapList:
    cmap = plt.get_cmap(name)
    
    fig, ax = plt.subplots(figsize=(12,6), subplot_kw={'projection': ccrs.PlateCarree()})
    
    #   reload countries each iteration
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()
    for country in countries:
        for i, j in enumerate(countriesComplete):
            if country.attributes['name_long'] == j[0]:
                #print country.attributes['name_long'], j[0]
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                        facecolor=cmap(norm(j[-1])),
                        linewidth=0.01)
        #   if the country name is not on the list, I need to mannually point to the country
        if country.attributes['name_long'] == 'Bahamas':
                ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                    facecolor=cmap(norm(countriesCompleteSorted[184][-1])),
                    linewidth=0.01)
        elif country.attributes['name_long'] == 'Brunei Darussalam':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[127][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == 'Cape Verde':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[78][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == "C\xf4te d'Ivoire":
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[129][-1])),
                linewidth=0.01)    
        elif country.attributes['name_long'] == 'Dem. Rep. Korea':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[58][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == 'Democratic Republic of the Congo':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[172][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == 'Faeroe Islands':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[170][-1])),
                linewidth=0.01)   
        elif country.attributes['name_long'] == 'Falkland Islands':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[232][-1])),
                linewidth=0.01)           
        elif country.attributes['name_long'] == 'Federated States of Micronesia':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[74][-1])),
                linewidth=0.01)      
        elif country.attributes['name_long'] == 'Lao PDR':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[177][-1])),
                linewidth=0.01)              
        elif country.attributes['name_long'] == 'Macao':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[0][-1])),
                linewidth=0.01)              
        elif country.attributes['name_long'] == 'Myanmar':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[116][-1])),
                linewidth=0.01)  
        elif country.attributes['name_long'] == 'Republic of Congo':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[207][-1])),
                linewidth=0.01)              
        elif country.attributes['name_long'] == 'Republic of Korea':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[21][-1])),
                linewidth=0.01)                
        elif country.attributes['name_long'] == 'Russian Federation':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[216][-1])),
                linewidth=0.01)                   
        elif country.attributes['name_long'] == 'Saint Helena':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[181][-1])),
                linewidth=0.01)         
        elif country.attributes['name_long'] == 'Saint-Martin':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[19][-1])),
                linewidth=0.01)  
        elif country.attributes['name_long'] == 'Somaliland':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[196][-1])),
                linewidth=0.01)              
        elif country.attributes['name_long'] == 'S\xe3o Tom\xe9 and Principe':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[61][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == 'The Gambia':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[68][-1])),
                linewidth=0.01)
        elif country.attributes['name_long'] == 'United States Virgin Islands':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[146][-1])),
                linewidth=0.01)            
        elif country.attributes['name_long'] == 'Wallis and Futuna Islands':
            ax.add_geometries(country.geometry, ccrs.PlateCarree(),
                facecolor=cmap(norm(countriesCompleteSorted[93][-1])),
                linewidth=0.01)             
        #   colors thanks to @Rutger Kassies http://stackoverflow.com/questions/25505674/python-matplotlib-add-colorbar
    cax = fig.add_axes([0.95, 0.2, 0.02, 0.6])
    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap, norm=norm, spacing='proportional', format='%.0f')
    ax.set_title('2015 Approximate Population Density (number of people per square km)')
    plt.savefig('images/worldPopulationDensity2015_'+name+'.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.savefig('images/worldPopulationDensity2015_'+name+'.png', format='png', dpi=300, bbox_inches='tight')
    #plt.close('all')
    #plt.show()
#countryNames = []
#
#reader = shpreader.Reader(shpfilename)
#countries = reader.records()
#for country in countries:
#    #print x
#    #   pring country name
#    countryNames.append(country.attributes['name_long'])
#    
#temp = set(countryNames) & set(countryNamesComplete)
#
#temp1 = set(countryNames).symmetric_difference(countryNamesComplete)
#
#temp2 = set(countryNames).difference(countryNamesComplete)
#
#temp3 = set(countryNamesComplete).difference(countryNames)