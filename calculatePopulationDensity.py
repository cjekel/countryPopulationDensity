#   Python 2.7.10 --  64-bit
#   import country population and area data saved as csv
#   then calculate the population density for these countries
import numpy as np
import csv

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
